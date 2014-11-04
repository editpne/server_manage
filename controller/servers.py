#coding=utf-8

import tornado.web
from model import ServersModel, IspModel, IdcModel, BusinessModel
from database import DB, Servers

"""
默认首页
"""


class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        page_num = self.get_argument('page', 1)
        if page_num <= 0:
            page_num = 1
        page_size = self.application.config.page.get('size', 10)
        _name = self.get_argument('name', False)
        _ip_addr = self.get_argument('ip', False)
        _isp_id = self.get_argument('isp', 0)
        _idc_id = self.get_argument('idc', 0)
        _business_id = self.get_argument('business', 0)
        _head_name = self.get_argument('head_name', False)
        _status = self.get_argument('status', 0)
        _cluster = self.get_argument('cluster', False)

        filters = {
            "name": _name,
            "ip_addr": _ip_addr,
            "head_name": _head_name,
            "cluster": _cluster
        }

        search_param = {"name": "名称", "ip": "IP地址", "head_name": "负责人"}
        table_colum = []
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

        choose_filters["environment"] = self.application.config.environment

        business_options = {}
        business_list = BusinessModel.get_all()
        for b_k, b_v in business_list.iteritems():
            business_options[b_k] = b_v.name
        choose_filters["business"] = business_options


        lists = ServersModel.get_list(page_num, page_size, **filters)

        self.render("index.html", search_param=search_param, table_colum=table_colum, lists=lists, list_choose=choose_filters)


