import core
import tornado
import os
import uuid


class PdfHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to generate PDF from url')

        name = 'tmp/%s.pdf' % str(uuid.uuid4())
        os.system('wkhtmltopdf %s %s' % (self.get_query_argument('url'), name))

        self.response_file(name)
