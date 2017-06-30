import core
import tornado


class HealthCheckHandler(core.BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        self.logger.info('Request to health check')

        self.response_json({
            'status': True,
            'components': {},
            'version': self.settings['version'],
            'started': self.settings['started']
        })
