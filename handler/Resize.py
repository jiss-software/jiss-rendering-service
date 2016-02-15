import core
import tornado
import uuid
import time
from utils import open_remote_image, resize, open_image


class ResizeHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to resize IMG from url')

        name = '/tmp/rs-%s.png' % str(uuid.uuid4())
        args = self._get_args()

        resize(open_remote_image(self.get_query_argument('url')), name, args)
        self.response_file(name)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.logger.info('Request to resize IMG for request file')

        args = self._get_args()

        for item in self.request.files.values():
            for file_info in item:
                name = '/tmp/rs-%s-%s.png' % (time.time(), file_info['filename'])

                resize(open_image(file_info['body']), name, args)
                self.response_file(name)
                return

    def _get_args(self):
        # Read arguments
        args = {
            'resize': self.request.headers.get('X-Jiss-Size', default=None)
        }

        # Parse if needed
        args['resize'] = [int(x) for x in args['resize'].split('x')] if args['resize'] else None

        self.logger.info('Args: %s' % self._dumps(args))

        return args
