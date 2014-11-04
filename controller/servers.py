#coding=utf-8

import tornado.web
from model import ServersModel, IspModel, IdcModel, BusinessModel, ApplicationModel
from database import DB, Servers

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
        print filters
        lists = ServersModel.get_list(page_num, page_size, **filters)
        _count = ServersModel.get_count(**filters)

        pages = {
            "total_num": _count,
            "total_page": int((_count - 1) / page_size) + 1,
            "page_num": page_num
        }

        self.render("index.html", search_param=search_param, search_query=_search_filter_query, table_colum=table_colum, lists=lists, list_choose=choose_filters, pages=pages)


class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("info.html")