#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Isp


def get_all():
    lists = DB.query(Isp).order_by(Isp.id.desc()).all()
    return lists


def get_one(isp_id):
    if isinstance(isp_id, int) is False:
        try:
            isp_id = int(isp_id)
        except ValueError:
            return False
    if isp_id == 0:
        return False
    return DB.query(Isp).filter(Isp.id == isp_id).scalar()


def update(_id, **params):
    update_data = {}
    if params.get("name"):
        update_data["name"] = params["name"]
    if not update_data:
        return False
    _DB = DB.query(Isp).filter(Isp.id == _id).update(update_data)
    DB.commit()
    return _DB


def create(**params):
    insert_data = {}
    if params.get("name"):
        insert_data["name"] = params["name"]
    if not insert_data:
        return False
    _DB = Isp(**insert_data)
    DB.add(_DB)
    DB.commit()
    return _DB


def remove(isp_id):
    _DB = DB.query(Isp).filter(Isp.id == isp_id).delete()
    DB.commit()
    return _DB
