#coding=utf-8
__author__ = 'zhenguoyu'

import base
import json
import hashlib
import tornado.web
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
        if user_info.status != 1:
            output["status"] = 1202
            output["message"] = '用户已停用'
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


class IndexHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        lists = UserModel.get_all()
        self.render('user/index.html', lists=lists, user=self.current_user)
        pass


class AddHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        _uname = self.get_argument('uname', False)
        _passwd = self.get_argument('passwd', False)
        _real_name = self.get_argument('real_name', False)
        _status = self.get_argument('status', 1)

        status_dict = {1: "正常", 2: "停用"}

        output = {"status": 0, "message": ""}
        if not _uname or not _real_name or not _status:
            output["status"] = 1101
            output["message"] = '参数不齐'
            return self.write(json.dumps(output))
        _uid = self.get_argument('uid', False)
        if _uid:
            try:
                _uid = int(_uid)
            except ValueError:
                output["status"] = 1102
                output["message"] = '错误的用户ID'
                return self.write(json.dumps(output))
        try:
            _status = int(_status)
        except ValueError:
            _status = 1

        if _status != 1 and _status != 2:
            output["status"] = 1105
            output["message"] = '错误的用户状态'
            return self.write(json.dumps(output))

        if _passwd:
            _passwd = hashlib.md5(_passwd).hexdigest()

        if _uid > 0:
            update_params = {}
            if _real_name:
                update_params["real_name"] = _real_name
            if _status:
                update_params["status"] = _status
            if _passwd:
                update_params["passwd"] = _passwd

            result = UserModel.update(uid=_uid, **update_params)
            if result:
                output["status"] = 1
                output["message"] = 'SUCCESS'
                output["data"] = {}
                output["data"]["uid"] = _uid
                output["data"]["real_name"] = _real_name
                output["data"]["status"] = _status
                output["data"]["_status"] = status_dict[_status]
                return self.write(json.dumps(output))
        else:
            if not _passwd:
                output["status"] = 1101
                output["message"] = '请输入密码'
                return self.write(json.dumps(output))

            user_info = UserModel.get_one_by_uname(_uname)
            if user_info:
                output["status"] = 1104
                output["message"] = '用户已存在,请重新输入'
                return self.write(json.dumps(output))

            result = UserModel.create(uname=_uname, passwd=_passwd, real_name=_real_name, status=_status)
            if result:
                output["status"] = 1
                output["message"] = 'SUCCESS'
                output["data"] = {}
                output["data"]["uid"] = result.id
                output["data"]["uname"] = result.uname
                output["data"]["real_name"] = result.real_name
                output["data"]["status"] = _status
                output["data"]["_status"] = status_dict[result.status]

                return self.write(json.dumps(output))

        output["status"] = 1103
        output["message"] = '出现错误,请重试'
        return self.write(json.dumps(output))


class RemoveHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        output = {"status": 0, "message": ""}
        _id = self.get_argument('id', 0)
        try:
            _id = int(_id)
        except ValueError:
            _id = 0
        if _id == 0:
            output["status"] = 1101
            output["message"] = "参数ID错误"
            return self.write(json.dumps(output))

        result = UserModel.remove(_id)
        print type(result)
        if result:
            output["status"] = 1
            output["message"] = "SUCCESS"
        else:
            output["status"] = 1101
            output["message"] = "参数ID错误"
        return self.write(json.dumps(output))


class ResetpasswdHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        _passwd = self.get_argument('passwd', False)
        _new_passwd = self.get_argument('new_passwd', False)
        _confirm_passwd = self.get_argument('confirm_passwd', False)
        output = {"status": 0, "message": ""}
        if not _passwd or not _new_passwd or not _confirm_passwd:
            output["status"] = 1101
            output["message"] = "参数不完整"
            return self.write(json.dumps(output))
        if _confirm_passwd != _new_passwd:
            output["status"] = 1102
            output["message"] = "两次密码不一致"
            return self.write(json.dumps(output))

        users = self.current_user
        uid = users["uid"]
        _passwd = hashlib.md5(_passwd).hexdigest()
        user_info = UserModel.get_one(uid)
        if not user_info:
            output["status"] = 1104
            output["message"] = "该用户不存在"
            return self.write(json.dumps(output))
        if user_info.passwd != _passwd:
            output["status"] = 1105
            output["message"] = "原密码错误, 不允许修改"
            return self.write(json.dumps(output))

        _new_passwd = hashlib.md5(_new_passwd).hexdigest()
        result = UserModel.update(uid, passwd=_new_passwd)
        if result:
            output["status"] = 1
            output["message"] = "SUCCESS"
            return self.write(json.dumps(output))
        output["status"] = 1103
        output["message"] = "异常错误"
        return self.write(json.dumps(output))

