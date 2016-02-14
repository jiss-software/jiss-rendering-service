from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from urllib import urlopen
from cStringIO import StringIO
from tornado.options import options


def open_remote_image(url):
    url = url if url.startswith("http") else "http://%s" % url
    return Image.open(StringIO(urlopen(url).read()))


def open_image(image):
    return Image.open(StringIO(image))


def add_watermark(target, out, args):
    image = Image.new("RGBA", target.size)
    selected_font = calculate_font_size(target.size, args['text'], args['proportion'])

    draw = ImageDraw.ImageDraw(image, "RGBA")
    draw.setfont(selected_font)
    draw.text(calculate_center(selected_font.getsize(args['text']), target.size), args['text'])
    draw.rotate(45)

    image.putalpha(image.convert("L").point(lambda x: min(x, 100)))
    target.paste(image, None, image)
    target.save(out, "PNG")


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
