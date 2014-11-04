#coding=utf-8
#main.py
import tornado.autoreload
import tornado.httpserver
import tornado.options
import tornado.ioloop
import tornado.web
import os.path
import config

from controller import servers, app, business, setting, user

from tornado.options import define, options
define("port", default=8000, type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", servers.IndexHandler),
            (r"/server/", servers.IndexHandler),
            (r"/server/add/", servers.AddHandler),
        ]
        self.config = config
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates")
        }
        tornado.web.Application.__init__(self, handlers, debug=True, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

