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
