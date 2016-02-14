from PIL import Image
from PIL import ImageFont
from urllib import urlopen
from cStringIO import StringIO
from tornado.options import options


def open_remote_image(url):
    url = url if url.startswith("http") else "http://%s" % url

    source = StringIO(urlopen(url).read())
    return Image.open(source)


def calculate_font_size(image_size, text, proportion=3):
    size = 1

    while True:
        selected = ImageFont.truetype(options.font_location, size)
        width, height = selected.getsize(text)

        if width * proportion > image_size[0] or height * proportion > image_size[1]:
            return selected

        size += 1


def calculate_center(font_size, image_size):
    return int(image_size[0] / 2 - font_size[0] / 2), int(image_size[1] / 2 - font_size[1] / 2)
