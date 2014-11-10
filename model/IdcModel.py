#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Idc


def get_all():
    lists = DB.query(Idc).order_by(Idc.id.desc()).all()
    return lists


def get_one(idc_id):
    if isinstance(idc_id, int) is False:
        try:
            idc_id = int(idc_id)
        except ValueError:
            return False
    if idc_id == 0:
        return False
    return DB.query(Idc).filter(Idc.id == idc_id).scalar()


def update(_id, **params):
    update_data = {}
    if params.get("name"):
        update_data["name"] = params["name"]
    if not update_data:
        return False
    _DB = DB.query(Idc).filter(Idc.id == _id).update(update_data)
    DB.commit()
    return _DB


def create(**params):
    insert_data = {}
    if params.get("name"):
        insert_data["name"] = params["name"]
    if not insert_data:
        return False
    _DB = Idc(**insert_data)
    DB.add(_DB)
    DB.commit()
    return _DB


def remove(idc_id):
    _DB = DB.query(Idc).filter(Idc.id == idc_id).delete()
    DB.commit()
    return _DB
