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


def get_one(idc_id):
    if isinstance(idc_id, int) is False:
        try:
            idc_id = int(idc_id)
        except ValueError:
            return False
    if idc_id == 0:
        return False
    return DB.query(Idc.id).filter(Idc.id == idc_id).scalar()