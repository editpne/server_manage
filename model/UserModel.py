#config=utf-8
__author__ = 'guoguo'

from database import DB, Users


def get_one(user_id):
    """
    get user information by user_id
    :param user_id:
    :return:

    """
    return DB.query(Users).filter(Users.id == user_id).first()


def get_one_by_uname(user_name):
    return DB.query(Users).filter(Users.uname == user_name).first()


def get_all():
    return DB.query(Users).order_by(Users.id.desc()).all()


def update(uid, **params):
    update_data = {}
    if params.get("passwd"):
        update_data["passwd"] = params["passwd"]
    if params.get("real_name"):
        update_data["real_name"] = params["real_name"]
    if params.get("status"):
        update_data["status"] = params["status"]

    if not update_data:
        return False

    _DB = DB.query(Users).filter(Users.id == uid).update(update_data)
    DB.commit()
    return _DB


def create(**params):

    insert_data = {}
    if not params.get("uname") or not params.get("passwd"):
        return False
    insert_data["uname"] = params["uname"]
    insert_data["passwd"] = params["passwd"]

    if params.get("real_name"):
        insert_data["real_name"] = params["real_name"]
    if params.get("status"):
        insert_data["status"] = params["status"]
    _DB = Users(**insert_data)
    DB.add(_DB)
    DB.commit()
    return _DB


def remove(business_id):
    _DB = DB.query(Users).filter(Users.id == business_id).delete()
    DB.commit()
    return _DB