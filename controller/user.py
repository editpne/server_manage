#coding=utf-8
__author__ = 'zhenguoyu'

import base
import json
import hashlib
from model import UserModel


class LoginHandler(base.BaseHandler):
    def get(self):
        """
        User login template
        :return:
        """
        if self.current_user:
            self.redirect('/')

        self.render('login.html')

    def post(self):
        """
        post to login
        :return:
        """
        output = {"status": 0, "message": ""}
        uname = self.get_argument('uname')
        passwd = self.get_argument('passwd')
        user_info = UserModel.get_one_by_uname(uname)
        if not user_info:
            output["status"] = 1201
            output["message"] = '用户不存在'
            return self.write(json.dumps(output))
        _passwd = hashlib.md5(passwd).hexdigest()

        user_info.passwd = str(user_info.passwd)
        _passwd = str(_passwd)
        if user_info.passwd != _passwd:
            output["status"] = 1202
            output["message"] = '密码错误'
            return self.write(json.dumps(output))
        passport = {"UNAME": uname, "UID": user_info.id, "UREALNAME": user_info.real_name}
        passport = json.dumps(passport)
        self.set_secure_cookie("UPASS", passport)
        output['status'] = 1
        output["message"] = "登陆成功"
        output['redirect'] = '/'
        return self.write(json.dumps(output))


class LogoutHandler(base.BaseHandler):
    def get(self):
        self.set_secure_cookie('UPASS', '')
        self.redirect('/login/')


class RegisterHandler(base.BaseHandler):
    def get(self):
        pass

    def post(self):
        pass


