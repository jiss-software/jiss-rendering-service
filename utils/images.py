from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps
from PIL import ImageEnhance
from PIL import ImageFilter
from urllib import urlopen
from cStringIO import StringIO
from tornado.options import options
import math


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def get_font(size):
    return ImageFont.truetype(options.font_location, size)


# Calculate width and height of text with selected size
def get_text_size(text, size, angle=0):
    result = ImageFont.truetype(options.font_location, size).getsize(text)

    if angle:
        angle = math.radians(angle)
        result = (
            int(result[0]*math.sin(angle) + result[1]*math.cos(angle) * 2),
            int(result[0]*math.cos(angle) - result[1]*math.sin(angle) * 2)
        )

    return result


def select_font_size(image_size, text, proportion, angle):
    size = 1

    while True:
        text_size = get_text_size(text, size, angle)

        if text_size[0] > image_size[0] * proportion or text_size[1] > image_size[1] * proportion:
            return size

        size += 1


def open_remote_image(url):
    url = url if url.startswith("http") else "http://%s" % url
    return Image.open(StringIO(urlopen(url).read()))


def open_image(image):
    return Image.open(StringIO(image))


def add_watermark(target, out, args):
    if 'font_size' not in args or not args['font_size']:
        font_size = select_font_size(target.size, args['text'], args['proportion'], args['angle'])
    else:
        font_size = int(args['font_size'])

    print "Target size (%s;%s)" % target.size

    # Get text layer
    text_size = get_text_size(args['text'], font_size, args['angle'])
    text_box_size = get_text_size(args['text'], font_size)

    print "Text size: %s rotated to %s" % (text_box_size, text_size)

    text_layer = get_text(text_box_size, font_size, args['text'])

    # Rotate
    if 'angle' in args and args['angle'] != 0:
        text_layer = text_layer.rotate(args['angle'], expand=1)

    # Fill with color
    location = calculate_position(text_size, target.size, args['position'])

    print "Location (%s;%s)" % location

    text_layer = draw_to_rgba_layer(target.size, args['color'], text_layer, (0, 0))

    if 'blur' in args and args['blur'] > 0:
        text_layer = text_layer.filter(ImageFilter.GaussianBlur(radius=2))

    if 'opacity' in args and 0 < args['opacity'] < 1:
        text_layer = set_opacity(text_layer, args['opacity'])

    target.paste(text_layer, location, text_layer)

    if 'resize' in args and args['resize']:
        target.thumbnail(args['resize'], Image.ANTIALIAS)

    target.save(out, "PNG")


def resize(target, out, args):
    if 'resize' in args and args['resize']:
        target.thumbnail(args['resize'], Image.ANTIALIAS)

    target.save(out, "PNG")


def get_text(size, font_size, text):
    text_layer = Image.new('L', size)
    d = ImageDraw.ImageDraw(text_layer)
    d.text((0, 0), text, font=get_font(font_size), fill=255)
    return text_layer


def set_opacity(im, opacity):
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def draw_to_rgba_layer(size, color, draw, position=(0, 0)):
    layer = Image.new("RGBA", size)
    layer.paste(ImageOps.colorize(draw, (0, 0, 0), color), position, draw)
    return layer


def calculate_position(text_size, image_size, loaction='center_middle'):
    hloc, vloc = loaction.split('_')

    x = 0
    y = 0

    if hloc == 'center':
        x = (image_size[0] - text_size[0]) / 3
    elif hloc == 'right':
        x = image_size[0] - text_size[0]

    if vloc == 'middle':
        y = (image_size[1] - text_size[1]) / 3
    elif vloc == 'bottom':
        y = image_size[1] - text_size[1]

    return int(x if x > 0 else 0), int(y if y > 0 else 0)
