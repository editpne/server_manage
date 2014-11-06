#coding=utf-8
__author__ = 'zhenguoyu'

import tornado.web
from model import ServersModel, IspModel, IdcModel, BusinessModel, ApplicationModel
import json

"""
默认首页
"""


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        page_num = self.get_argument('page', 1)
        page_num = int(page_num)
        if page_num <= 0:
            page_num = 1
        page_size = self.application.config.page.get('size', 10)
        _name = self.get_argument('name', False)
        _ip_addr = self.get_argument('ip_addr', False)
        _isp_id = self.get_argument('isp', False)
        _idc_id = self.get_argument('idc', False)
        _environment = self.get_argument('environment', False)
        _role = self.get_argument('role', False)
        _business_id = self.get_argument('business', False)
        _head_name = self.get_argument('head_name', False)
        _status = self.get_argument('status', False)
        _cluster = self.get_argument('cluster', False)
        _app_id = self.get_argument('application', False)

        filters = {
            "name": _name,
            "ip_addr": _ip_addr,
            "head_name": _head_name,
            "cluster": _cluster,
            "isp": int(_isp_id),
            "idc": int(_idc_id),
            "environment": int(_environment),
            "business": int(_business_id),
            "status": int(_status),
            "role": int(_role),
            "application": int(_app_id)
        }
        _search_filter = []
        for f_k, f_v in filters.iteritems():
            if f_v:
                _search_filter.append('%s=%s' % (f_k, f_v))

        if len(_search_filter) > 0:
            _search_filter_query = '&'.join(_search_filter)
        else:
            _search_filter_query = ''

        search_param = {"name": "名称", "ip_addr": "IP地址", "head_name": "负责人", "cluster": "集群"}

        table_colum = [
            {
                "key": "id",
                "name": "编号"
            },
            {
                "key": "name",
                "name": "名称"
            },
            {
                "key": "ip_addr",
                "name": "IP地址"
            },
            {
                "key": "isp",
                "name": "ISP提供商"
            },
            {
                "key": "idc",
                "name": "IDC机房"
            },
            {
                "key": "environment",
                "name": "环境"
            },
            {
                "key": "business",
                "name": "业务"
            },
            {
                "key": "application",
                "name": "应用"
            },
            {
                "key": "cluster",
                "name": "集群"
            },
            {
                "key": "role",
                "name": "角色"
            },
            {
                "key": "head_name",
                "name": "负责人"
            },
            {
                "key": "status",
                "name": "状态"
            },
            {
                "key": "action",
                "name": "操作"
            }
        ]

        choose_filters = dict()

        isp_options = {}
        isp_list = IspModel.get_all()
        for isp_k, isp_v in isp_list.iteritems():
            isp_options[isp_k] = isp_v.name
        choose_filters["isp"] = isp_options

        idc_options = {}
        idc_list = IdcModel.get_all()
        for idc_k, idc_v in idc_list.iteritems():
            idc_options[idc_k] = idc_v.name
        choose_filters["idc"] = idc_options

        business_options = {}
        business_list = BusinessModel.get_all()
        for b_k, b_v in business_list.iteritems():
            business_options[b_k] = b_v.name
        choose_filters["business"] = business_options

        application_options = {}
        app_list = ApplicationModel.get_all()
        for a_k, a_v in app_list.iteritems():
            application_options[a_k] = a_v.name
        choose_filters["application"] = application_options

        choose_filters["environment"] = choose_filters["role"] = self.application.config.environment
        choose_filters["status"] = self.application.config.status

        lists = ServersModel.get_list(page_num, page_size, **filters)
        _count = ServersModel.get_count(**filters)

        pages = {
            "total_num": _count,
            "total_page": int((_count - 1) / page_size) + 1,
            "page_num": page_num
        }

        self.render("index.html", search_param=search_param, search_query=_search_filter_query, table_colum=table_colum, lists=lists, list_choose=choose_filters, pages=pages)


class AddHandler(tornado.web.RequestHandler):
    def get(self, server_id=0):
        if server_id == 0:
            server_id = self.get_argument('id', False)
        choose_filters = dict()
        default_choose = dict()
        if server_id is not False:
            try:
                server_id = int(server_id)
            except ValueError:
                server_id = False

        if server_id:
            server_info = ServersModel.get_one(server_id)
            if not server_info:
                return self.write('参数错误')
        else:
            server_info = ServersModel.get_object()

        isp_options = {}
        isp_list = IspModel.get_all()
        for isp_k, isp_v in isp_list.iteritems():
            if not server_info.isp_id:
                server_info.isp_id = isp_k
            isp_options[isp_k] = isp_v.name
        choose_filters["isp"] = isp_options

        idc_options = {}
        idc_list = IdcModel.get_all()
        for idc_k, idc_v in idc_list.iteritems():
            if not server_info.idc_id:
                server_info.idc_id = idc_k
            idc_options[idc_k] = idc_v.name
        choose_filters["idc"] = idc_options

        business_options = {}
        business_list = BusinessModel.get_all()
        for b_k, b_v in business_list.iteritems():
            if not server_info.business_id:
                server_info.business_id = b_k
            business_options[b_k] = b_v.name
        choose_filters["business"] = business_options

        application_options = {}
        app_list = ApplicationModel.get_all()
        for a_k, a_v in app_list.iteritems():
            if not server_info.application_id:
                server_info.application_id = a_k
            application_options[a_k] = a_v.name
        choose_filters["application"] = application_options

        if not server_info.environment:
            server_info.environment = 1
        if not server_info.role:
            server_info.role = 1
        if not server_info.status:
            server_info.status = 1

        choose_filters["environment"] = choose_filters["role"] = self.application.config.environment
        choose_filters["status"] = self.application.config.status

        self.render("info.html", list_choose=choose_filters, default_choose=default_choose, server_info=server_info)

    def post(self):
        """python POST提交上的默认是unicode类型, int()类型转化必须是数字的,否则报错. 所以使用try except来处理.

        """

        _name = self.get_argument('name', False)
        _ip_addr = self.get_argument('ip_addr', False)
        _head_name = self.get_argument('head_name', False)
        _cluster = self.get_argument('cluster', False)
        _id = self.get_argument('id', False)

        if not _name or not _ip_addr or not _head_name or not _cluster:
            return self.write('输入框参数不齐, 请重新填写')

        _isp_id = self.get_argument('isp', 0)
        _idc_id = self.get_argument('idc', 0)
        _environment = self.get_argument('environment', 0)
        _role = self.get_argument('role', 0)
        _business_id = self.get_argument('business', 0)
        _application_id = self.get_argument('application', 0)

        if not _isp_id or not _idc_id or not _environment or not _role or not _business_id or not _application_id:
            return self.write('选择框参数不齐, 请重新填写')

        _status = self.get_argument('status', 0)
        if not _status:
            return self.write('单选项参数不齐')

        isp_info = IspModel.get_one(_isp_id)
        if not isp_info:
            return self.write("不存在的ISP服务商")

        idc_info = IdcModel.get_one(_idc_id)
        if not idc_info:
            return self.write("IDC不存在")

        business_info = BusinessModel.get_one(_business_id)
        if not business_info:
            return self.write("业务不存在")

        application_info = ApplicationModel.get_one(_application_id)
        if not application_info:
            return self.write("应用不存在")

        _status = int(_status)
        if _status != 1 and _status != 2:
            return self.write("错误的服务器状态")

        ip_addrs = _ip_addr.split('.')
        if len(ip_addrs) != 4:
            return self.write("错误的IP地址1")
        for _ip in ip_addrs:
            try:
                _ip = int(_ip)
            except ValueError:
                return self.write("错误的IP地址2")
            if _ip >= 255 or _ip < 0:
                return self.write("错误的IP地址2")

        data_param = {
            "name": _name,
            "ip_addr": _ip_addr,
            "head_name": _head_name,
            "cluster": _cluster,
            "isp_id": _isp_id,
            "idc_id": _idc_id,
            "environment": _environment,
            "role": _role,
            "business_id": _business_id,
            "application_id": _application_id,
            "status": _status,
            "user_id": self.application.user_id
        }
        if not _id:
            server = ServersModel.create(**data_param)
            if server.id > 0:
                self.redirect('/')
            else:
                return self.write('数据插入失败, 请重试或联系管理员.5076')
        else:
            try:
                _id = int(_id)
            except ValueError:
                return self.write('错误的ID')
            server = ServersModel.update(_id, **data_param)
            if server:
                self.redirect('/')
            else:
                return self.write('更新失败, 请重试或联系管理员.5076')


class RemoveHandler(tornado.web.RequestHandler):
    def get(self):
        _output = {"status": 1, "message": ""}
        _id = self.get_argument('id', 0)
        try:
            _id = int(_id)
        except ValueError:
            _output["status"] = 101
            _output["message"] = "错误的参数类型"
            return self.write(json.dumps(_output))

        server = ServersModel.remove(_id)
        if server == 1:
            return self.write(json.dumps(_output))





