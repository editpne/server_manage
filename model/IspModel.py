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


def get_one(isp_id):
    if isinstance(isp_id, int) is False:
        try:
            isp_id = int(isp_id)
        except ValueError:
            return False
    if isp_id == 0:
        return False
    return DB.query(Isp).filter(Isp.id == isp_id).scalar()