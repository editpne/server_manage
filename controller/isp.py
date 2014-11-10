#coding=utf-8

import tornado.web
import base
import json
from model import IspModel, ServersModel


class IndexHandler(base.BaseHandler):

    @tornado.web.authenticated
    def get(self):
        lists = IspModel.get_all()
        self.render('isp/index.html', user=self.current_user, lists=lists)


class AddHandler(base.BaseHandler):

    @tornado.web.authenticated
    def post(self):
        _name = self.get_argument('name', '')
        _isp_id = self.get_argument('isp_id', 0)
        output = {"status": 0, "message": ''}
        if len(_name) == 0:
            output["status"] = "1105"
            output["message"] = "名称不能为空"
            return self.write(json.dumps(output))
        try:
            _isp_id = int(_isp_id)
        except ValueError:
            _isp_id = 0

        if _isp_id != 0:
            result = IspModel.update(_isp_id, name=_name)
            if result:
                output["status"] = 1
                output["message"] = "成功"
                return self.write(json.dumps(output))
        else:
            result = IspModel.create(name=_name)
            if result.id > 0:
                output["status"] = 1
                output["message"] = "成功"
                output["data"] = {}
                output["data"]["isp_id"] = result.id
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
        servers = ServersModel.get_by_isp(_id)
        if len(servers) > 0:
            output["status"] = 1301
            output["message"] = "不能删除该项，请检查服务器。"
            return self.write(json.dumps(output))

        result = IspModel.remove(_id)
        print type(result)
        if result:
            output["status"] = 1
            output["message"] = "SUCCESS"
        else:
            output["status"] = 1101
            output["message"] = "参数ID错误"
        return self.write(json.dumps(output))