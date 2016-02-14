import core
import tornado
import uuid
from utils import open_remote_image, add_watermark, open_image


class WatermarkHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request watermark generation for remote file')

        name = '/tmp/%s.png' % str(uuid.uuid4())
        proportion = self.get_query_argument('proportion', default=1.5)
        text = self.get_query_argument('text', default="Test")

        add_watermark(open_remote_image(self.get_query_argument('url')), name, text, proportion)
        self.response_file(name)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        self.logger.info('Request watermark generation for request file')

        proportion = self.get_query_argument('proportion', default=1.5)
        text = self.get_query_argument('text', default="Test")

        for item in self.request.files.values():
            for file_info in item:
                name = '/tmp/%s-%s.pdf' % (time.time(), file_info['filename'])

                #with open(name, 'w') as f:
                #    f.write(file_info['body'])

                add_watermark(open_image(file_info['body']), name, text, proportion)
                self.response_file(name)
                return
