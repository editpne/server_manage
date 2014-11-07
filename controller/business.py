#conding=utf-8

import tornado.web
import base
import model.BusinessModel


class IndexHandler(base.BaseHandler):
    @tornado.web.authenticated
    def get(self):

        self.render('business/index.html', user=self.current_user)
        pass


class AddHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render('business/add.html')
