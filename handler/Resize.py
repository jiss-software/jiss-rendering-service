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

        x = params.get('x')
        y = params.get('y')

        size = x if x else 450, y if y else 450

        name = 'tmp/%s.png' % str(uuid.uuid4())

        target = open_remote_image(params.get('url'))
        target.thumbnail(size, Image.ANTIALIAS)
        target.save(name, "PNG")

        self.response_file(name)
