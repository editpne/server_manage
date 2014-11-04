#coding=utf-8

from database import DB, Servers


def get(id):
    pass


def get_count(**filters):
    if filters.get("name"):
        _name = filters["name"]

    pass


def get_list(page_num, page_size, **filters):
    _DB = DB.query(Servers)
    if filters.get("name"):
        _name = filters["name"]
        _DB = _DB.filter(Servers.name.like(_name+'%'))
    limit = page_size * (page_num - 1)
    lists = _DB.limit(page_size).offset(limit)

    return lists
