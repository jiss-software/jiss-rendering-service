import tornado.web
import logging
from settings import routing
from tornado.options import options
import os

tornado.options.parse_command_line()

if not os.path.exists(options.log_dir):
    os.makedirs(options.log_dir)

logging.basicConfig(
    format='%(asctime)s [%(name)s] %(levelname)s: %(message)s',
    filename='%s/%s' % (options.log_dir, options.log_file),
    level=logging.DEBUG
)

ioLoop = tornado.ioloop.IOLoop.current()
app = tornado.web.Application(routing, autoreload=options.autoreload)

app.listen(options.port)

if __name__ == "__main__":
    try:
        logging.info("Starting HTTP server on port %d" % options.port)
        ioLoop.start()
    except KeyboardInterrupt:
        logging.info("Shutting down server HTTP proxy on port %d" % options.port)
        ioLoop.stop()
