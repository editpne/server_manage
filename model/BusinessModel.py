#coding=utf-8
__author__ = 'zhenguoyu'

from database import DB, Business


def get_all():
    lists = DB.query(Business).order_by(Business.id.desc()).all()
    return lists


def get_one(business_id):
    if isinstance(business_id, int) is False:
        try:
            business_id = int(business_id)
        except ValueError:
            return False
    if business_id == 0:
        return False
    return DB.query(Business).filter(Business.id == business_id).scalar()


def update(_id, **params):
    update_data = {}
    if params.get("name"):
        update_data["name"] = params["name"]
    if not update_data:
        return False
    _DB = DB.query(Business).filter(Business.id == _id).update(update_data)
    DB.commit()
    return _DB


def create(**params):
    insert_data = {}
    if params.get("name"):
        insert_data["name"] = params["name"]
    if not insert_data:
        return False
    _DB = Business(**insert_data)
    DB.add(_DB)
    DB.commit()
    return _DB


def remove(business_id):
    _DB = DB.query(Business).filter(Business.id == business_id).delete()
    DB.commit()
    return _DB
