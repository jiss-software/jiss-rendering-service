from tornado.options import define
from handler.HealthCheck import HealthCheckHandler
from handler.Img import ImgHandler
from handler.Pdf import PdfHandler
from handler.Resize import ResizeHandler
from handler.Watermark import WatermarkHandler

define("port", default=33005, help="Application port")
define("max_buffer_size", default=50 * 1024**2, help="")
define("autoreload", default=False, help="Autoreload server on change")

define("log_dir", default="/var/log", help="Logger directory")
define("log_file", default="jiss-tornado-template.log", help="Logger file name")

define("font_location", default="/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", help="")

routing = [
    (r"/", HealthCheckHandler),
    (r"/img", ImgHandler),
    (r"/pdf", PdfHandler),
    (r"/resize", ResizeHandler),
    (r"/watermark", WatermarkHandler)
]
