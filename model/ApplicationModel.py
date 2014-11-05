#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Application


def get_all():
    lists = DB.query(Application).all()
    output = {}
    if lists:
        for item in lists:
            output[item.id] = item
    return output


def get_one(application_id):
    if isinstance(application_id, int) is False:
        try:
            application_id = int(application_id)
        except ValueError:
            return False
    if application_id == 0:
        return False
    return DB.query(Application).filter(Application.id == application_id).scalar()