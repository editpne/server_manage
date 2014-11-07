#condig=utf-8
__author__ = 'zhenguoyu'

import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        passport = self.get_secure_cookie('UPASS')
        if passport:
            passport = json.loads(passport)
            if passport.get("UID") and passport.get("UNAME") and passport.get("UREALNAME"):
                return {"uid": passport["UID"], "uname": passport["UNAME"], "real_name": passport["UREALNAME"]}
        return None

