#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Business


def get_all():
    lists = DB.query(Business).all()
    output = {}
    if lists:
        for item in lists:
            output[item.id] = item
    return output


def get_one(business_id):
    if isinstance(business_id, int) is False:
        try:
            business_id = int(business_id)
        except ValueError:
            return False
    if business_id == 0:
        return False
    return DB.query(Business).filter(Business.id == business_id).scalar()