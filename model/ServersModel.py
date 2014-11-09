#coding=utf-8

from database import DB, Servers


def get_one(server_id):
    return DB.query(Servers).filter(Servers.id == server_id).first()


def get_object():
    return Servers()


def get_count(**filters):
    _DB = DB.query(Servers)
    if filters.get("name"):
        _name = filters["name"]
        _DB = _DB.filter(Servers.name.like(_name+'%'))

    if filters.get("idc") and filters["idc"] > 0:
        _idc_id = filters["idc"]
        _DB = _DB.filter(Servers.idc_id == _idc_id)

    if filters.get("isp") and filters["isp"] > 0:
        _isp_id = filters["isp"]
        _DB = _DB.filter(Servers.isp_id == _isp_id)

    if filters.get("ip_addr"):
        _ip_addr = filters["ip_addr"]
        _DB = _DB.filter(Servers.ip_addr.like(_ip_addr+'%'))

    if filters.get("head_name"):
        _head_name = filters["head_name"]
        _DB = _DB.filter(Servers.head_name.like(_head_name+'%'))

    if filters.get("environment") and filters["environment"] > 0:
        _environment = filters["environment"]
        _DB = _DB.filter(Servers.environment == _environment)

    if filters.get("business") and filters["business"] > 0:
        _business_id = filters["business"]
        _DB = _DB.filter(Servers.business_id == _business_id)

    if filters.get("status") and filters["status"] > 0:
        _status = filters["status"]
        _DB = _DB.filter(Servers.status == _status)

    if filters.get("role") and filters["role"] > 0:
        _role = filters["role"]
        _DB = _DB.filter(Servers.role == _role)

    if filters.get("application") and filters["application"] > 0:
        _application_id = filters["application"]
        _DB = _DB.filter(Servers.application_id == _application_id)

    if filters.get("cluster"):
        _cluster = filters["cluster"]
        _DB = _DB.filter(Servers.cluster.like(_cluster+'%'))
    return _DB.count()


def get_list(page_num, page_size, **filters):
    _DB = DB.query(Servers)
    if filters.get("name"):
        _name = filters["name"]
        _DB = _DB.filter(Servers.name.like(_name+'%'))

    if filters.get("idc") and filters["idc"] > 0:
        _idc_id = filters["idc"]
        _DB = _DB.filter(Servers.idc_id == _idc_id)

    if filters.get("isp") and filters["isp"] > 0:
        _isp_id = filters["isp"]
        _DB = _DB.filter(Servers.isp_id == _isp_id)

    if filters.get("ip_addr"):
        _ip_addr = filters["ip_addr"]
        _DB = _DB.filter(Servers.ip_addr.like(_ip_addr+'%'))

    if filters.get("head_name"):
        _head_name = filters["head_name"]
        _DB = _DB.filter(Servers.head_name.like(_head_name+'%'))

    if filters.get("environment") and filters["environment"] > 0:
        _environment = filters["environment"]
        _DB = _DB.filter(Servers.environment == _environment)

    if filters.get("business") and filters["business"] > 0:
        _business_id = filters["business"]
        _DB = _DB.filter(Servers.business_id == _business_id)

    if filters.get("status") and filters["status"] > 0:
        _status = filters["status"]
        _DB = _DB.filter(Servers.status == _status)

    if filters.get("role") and filters["role"] > 0:
        _role = filters["role"]
        _DB = _DB.filter(Servers.role == _role)

    if filters.get("application") and filters["application"] > 0:
        _application_id = filters["application"]
        _DB = _DB.filter(Servers.application_id == _application_id)

    if filters.get("cluster"):
        _cluster = filters["cluster"]
        _DB = _DB.filter(Servers.cluster.like(_cluster+'%'))

    limit = page_size * (page_num - 1)
    lists = _DB.limit(page_size).offset(limit)

    return lists


def create(**data_param):
    _DB = Servers(**data_param)
    DB.add(_DB)
    DB.commit()
    return _DB


def remove(server_id):
    _DB = DB.query(Servers).filter(Servers.id == server_id).delete()
    DB.commit()
    return _DB


def update(server_id, **data_param):
    #_DB = Servers(**data_param)
    update_data = {}
    if data_param.get("name"):
        update_data['name'] = data_param['name']
    if data_param.get("ip_addr"):
        update_data['ip_addr'] = data_param['ip_addr']
    if data_param.get("isp_id"):
        update_data['isp_id'] = data_param['isp_id']
    if data_param.get("idc_id"):
        update_data['idc_id'] = data_param['idc_id']
    if data_param.get("environment"):
        update_data['environment'] = data_param['environment']
    if data_param.get("business_id"):
        update_data['business_id'] = data_param['business_id']
    if data_param.get("application_id"):
        update_data['application_id'] = data_param['application_id']
    if data_param.get("cluster"):
        update_data['cluster'] = data_param['cluster']
    if data_param.get("role"):
        update_data['role'] = data_param['role']
    if data_param.get("head_name"):
        update_data['head_name'] = data_param['head_name']
    if data_param.get("status"):
        update_data['status'] = data_param['status']
    if not update_data:
        return False
    _DB = DB.query(Servers).filter(Servers.id == server_id).update(update_data)
    DB.commit()
    return _DB


def get_by_business(business_id):
    return DB.query(Servers).filter(Servers.business_id == business_id).all()


