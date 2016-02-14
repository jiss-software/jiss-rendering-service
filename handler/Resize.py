import core
import tornado
import os
import uuid
from PIL import Image
from utils import open_remote_image


class ResizeHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to resize IMG from url')

        x = self.get_query_argument('x')
        y = self.get_query_argument('y')

        size = x if x else 450, y if y else 450

        name = 'tmp/%s.png' % str(uuid.uuid4())

        target = open_remote_image(self.get_query_argument('url'))
        target.thumbnail(size, Image.ANTIALIAS)
        target.save(name, "PNG")

        self.response_file(name)
