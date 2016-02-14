import core
import tornado
from PIL import Image
from PIL import ImageDraw
import uuid
from utils import calculate_center, calculate_font_size, open_remote_image


class WatermarkHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request watermark generation for remote file')

        name = '/tmp/%s.png' % str(uuid.uuid4())
        proportion = self.get_query_argument('proportion', default=1.5)
        text = self.get_query_argument('text', default="Test")

        target = open_remote_image(self.get_query_argument('url'))
        watermark = Image.new("RGBA", target.size)
        selected_font = calculate_font_size(target.size, text, proportion)

        waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
        waterdraw.setfont(selected_font)
        waterdraw.text(calculate_center(selected_font.getsize(text), target.size), text)

        watermark.putalpha(watermark.convert("L").point(lambda x: min(x, 100)))
        target.paste(watermark, None, watermark)
        target.save(name, "PNG")

        self.response_file(name)
