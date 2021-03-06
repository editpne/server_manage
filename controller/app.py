#coding=utf-8

import tornado.web
import base
import json
from model import ApplicationModel, ServersModel


class IndexHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        lists = ApplicationModel.get_all()
        self.render('app/index.html', user=self.current_user, lists=lists)


class AddHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        _name = self.get_argument('name', '')
        _app_id = self.get_argument('app_id', 0)
        output = {"status": 0, "message": ''}
        if len(_name) == 0:
            output["status"] = "1105"
            output["message"] = "名称不能为空"
            return self.write(json.dumps(output))
        try:
            _app_id = int(_app_id)
        except ValueError:
            _app_id = 0

        if _app_id != 0:
            result = ApplicationModel.update(_app_id, name=_name)
            print 1
            print result
            if result:
                output["status"] = 1
                output["message"] = "成功"
                return self.write(json.dumps(output))
        else:
            result = ApplicationModel.create(name=_name)
            print result
            if result.id > 0:
                output["status"] = 1
                output["message"] = "成功"
                output["data"] = {}
                output["data"]["app_id"] = result.id
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
        servers = ServersModel.get_by_app(_id)
        if len(servers) > 0:
            output["status"] = 1301
            output["message"] = "不能删除该项，请检查服务器。"
            return self.write(json.dumps(output))

        result = ApplicationModel.remove(_id)
        print type(result)
        if result:
            output["status"] = 1
            output["message"] = "SUCCESS"
        else:
            output["status"] = 1101
            output["message"] = "参数ID错误"
        return self.write(json.dumps(output))