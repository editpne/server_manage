#coding=utf-8

import tornado.web
import base
import json
from model import BusinessModel, ServersModel


class IndexHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        lists = BusinessModel.get_all()
        self.render('business/index.html', user=self.current_user, lists=lists)


class AddHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        _name = self.get_argument('name', '')
        _business_id = self.get_argument('business_id', 0)
        output = {"status": 0, "message": ''}
        if len(_name) == 0:
            output["status"] = "1105"
            output["message"] = "名称不能为空"
            return self.write(json.dumps(output))
        try:
            _business_id = int(_business_id)
        except ValueError:
            _business_id = 0

        if _business_id != 0:
            result = BusinessModel.update(_business_id, name=_name)
            if result:
                output["status"] = 1
                output["message"] = "成功"
                return self.write(json.dumps(output))
        else:
            result = BusinessModel.create(name=_name)
            if result.id > 0:
                output["status"] = 1
                output["message"] = "成功"
                output["data"] = {}
                output["data"]["business_id"] = result.id
                return self.write(json.dumps(output))
        output["status"] = 1205
        output["message"] = "失败"
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
        servers = ServersModel.get_by_business(_id)
        if len(servers) > 0:
            output["status"] = 1301
            output["message"] = "不能删除该项，请检查服务器。"
            return self.write(json.dumps(output))

        result = BusinessModel.remove(_id)
        print type(result)
        if result:
            output["status"] = 1
            output["message"] = "SUCCESS"
        else:
            output["status"] = 1101
            output["message"] = "参数ID错误"
        return self.write(json.dumps(output))