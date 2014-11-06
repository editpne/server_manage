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
            (r"/server/(\d+)/", servers.AddHandler),
            (r"/server/add/", servers.AddHandler),
            (r"/server/remove/", servers.RemoveHandler),
            (r"/login/", user.LoginHandler),
        ]
        self.config = config
        self.user_id = 1
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "cookie_secret": "61oETzKXQAKaYdkL5gEmHeJJFaYh7Ecnp2XdiP1o/Vo=",
            "login_url": "/login/",
        }
        tornado.web.Application.__init__(self, handlers, debug=True, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

