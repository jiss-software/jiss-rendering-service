import core
import tornado
import uuid
import time
from utils import open_remote_image, add_watermark, open_image


class WatermarkHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request watermark generation for remote file')

        name = '/tmp/%s.png' % str(uuid.uuid4())
        args = self._get_args()

        add_watermark(open_remote_image(self.get_query_argument('url')), name, args['text'], args['proportion'])
        self.response_file(name)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.logger.info('Request watermark generation for request file')

        args = self._get_args()

        for item in self.request.files.values():
            for file_info in item:
                name = '/tmp/%s-%s.pdf' % (time.time(), file_info['filename'])

                add_watermark(open_image(file_info['body']), name, args['text'], args['proportion'])
                self.response_file(name)
                return

    def _get_args(self):
        args = {
            'proportion': int(self.request.headers.get('proportion', default=1.5)),
            'text': self.request.headers.get('X-Jiss-Text', default='Test')
        }

        self.logger.info('Args: %s' % self._dumps(args))

        return args
