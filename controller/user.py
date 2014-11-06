#coding=utf-8
__author__ = 'zhenguoyu'

import tornado.web
import json
import hashlib
from model import UserModel


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        """
        User login template
        :return:
        """
        self.render('login.html')
        pass

    def post(self):
        """
        post to login
        :return:
        """
        output = {"status": 0, "message": ""}
        user_name = self.get_argument('username')
        passwd = self.get_argument('passwd')

        user_info = UserModel.get_one_by_uname(user_name)
        if not user_info:
            output["status"] = 1201
            output["message"] = '用户不存在'
            return self.write(json.dumps(output))
        _passwd = hashlib.md5(passwd).hexdigest()
        if user_info.passwd != _passwd:
            output["status"] = 1202
            output["message"] = '密码错误'
            return self.write(json.dumps(output))
        self.set_secure_cookie("uname", user_name)
        self.set_secure_cookie("uid", user_info.id)
        self.redirect('/')


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        pass


