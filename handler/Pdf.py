import core
import tornado
import os
import uuid

# 'grayscale %s' % '-g'
# -O, --orientation <orientation>     Set orientation to Landscape or Portrait
# -s, --page-size <Size>              Set paper size to: A4, Letter, etc.
# -page-height <unitreal>        Page height
# -s, --page-size <Size>              Set paper size to: A4, Letter, etc.
# --page-width <unitreal>         Page width
#  --background                    Do print background (default)
# --no-background                 Do not print background
# --disable-external-links        Do not make links to remote web pages
# --enable-external-links
# --images                        Do load or print images (default)
# --no-images                     Do not load or print images
# --disable-javascript            Do not allow web pages to run javascript
# --enable-javascript
# --javascript-delay <msec>       Wait some milliseconds for javascript
#     finish (default 200)
# --print-media-type              Use print media-type instead of screen
# --no-print-media-type           Do not use print media-type instead of screen (default)
# --disable-smart-shrinking       Disable the intelligent shrinking strategy
# used by WebKit that makes the pixel/dpi
# ratio none constant
# --enable-smart-shrinking        Enable the intelligent shrinking strategy
# used by WebKit that makes the pixel/dpi
# ratio none constant (default)
# --zoom <float>                  Use this zoom factor (default 1)


class PdfHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to generate PDF from url')

        name = '/tmp/pdf-%s.pdf' % str(uuid.uuid4())
        os.system('wkhtmltopdf %s %s' % (self.get_query_argument('url'), name))

        self.response_file(name)

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

            # -B, --margin-bottom <unitreal>      Set the page bottom margin
            # -L, --margin-left <unitreal>        Set the page left margin (default 10mm)
            # -R, --margin-right <unitreal>       Set the page right margin (default 10mm)
            # -T, --margin-top <unitreal>         Set the page top margin
        }

        # Parse if needed
        args['color'] = [int(x) for x in args['color'].split(',')] if args['color'] else WHITE
        args['resize'] = [int(x) for x in args['resize'].split('x')] if args['resize'] else None
        args['repeat'] = args['repeat'] and args['repeat'] in ['True', 'true']

        self.logger.info('Args: %s' % self._dumps(args))

        return args
