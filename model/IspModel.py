#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Isp


def get_all():
    lists = DB.query(Isp).all()
    output = {}
    if lists:
        for item in lists:
            output[item.id] = item
    return output