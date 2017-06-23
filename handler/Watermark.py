import core
import tornado
import uuid
import time
from utils import open_remote_image, add_watermark, open_image, WHITE


class WatermarkHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request watermark generation for remote file')

        name = '/tmp/wm-%s.png' % str(uuid.uuid4())
        args = self._get_args()

        add_watermark(open_remote_image(self.get_query_argument('url')), name, args)
        self.response_file(name)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.logger.info('Request watermark generation for request file')

        args = self._get_args()

        for item in self.request.files.values():
            for file_info in item:
                name = '/tmp/wm-%s-%s.png' % (time.time(), file_info['filename'])

                add_watermark(open_image(file_info['body']), name, args)
                self.response_file(name)
                return

    def _get_args(self):
        # Read arguments
        args = {
            'angle': int(self.request.headers.get('X-Jiss-Angle', default=45)),
            'blur': int(self.request.headers.get('X-Jiss-Blur', default=0)),
            'color': self.request.headers.get('X-Jiss-Color', default=None),
            'position': self.request.headers.get('X-Jiss-Position', default='center_middle'),
            'proportion': float(self.request.headers.get('X-Jiss-Proportion', default=0.9)),
            'opacity': float(self.request.headers.get('X-Jiss-Opacity', default=0.3)),
            'text': self.request.headers.get('X-Jiss-Text', default='Demo'),
            'resize': self.request.headers.get('X-Jiss-Resize', default=None),
            'repeat': self.request.headers.get('X-Jiss-Repeat', default=None)
        }

        # Parse if needed
        args['color'] = [int(x) for x in args['color'].split(',')] if args['color'] else WHITE
        args['resize'] = [int(x) for x in args['resize'].split('x')] if args['resize'] else None
        args['repeat'] = args['repeat'] and args['repeat'] in ['True', 'true']

        self.logger.info('Args: %s' % self._dumps(args))

        return args
