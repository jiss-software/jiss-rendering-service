import core
import tornado
import os
import uuid


class ImgHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to generate PNG from url')

        name = 'tmp/%s.png' % str(uuid.uuid4())
        os.system('wkhtmltoimage %s %s' % (self.get_query_argument('url'), name))

        self.response_file(name)
