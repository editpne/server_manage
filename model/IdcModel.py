#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Idc


def get_all():
    lists = DB.query(Idc).all()
    output = {}
    if lists:
        for item in lists:
            output[item.id] = item
    return output