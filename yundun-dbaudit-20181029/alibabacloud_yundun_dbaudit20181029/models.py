# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ClearInstanceStorageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        storage_space: str = None,
        storage_category: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.storage_space = storage_space
        self.storage_category = storage_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        return self


class ClearInstanceStorageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ClearInstanceStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearInstanceStorageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClearInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        ip_version: str = None,
        white_list: List[str] = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.ip_version = ip_version
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigInstanceWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigInstanceWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigInstanceWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditLogsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        start_time: str = None,
        end_time: str = None,
        current_page: int = None,
        page_size: int = None,
        sort: str = None,
        dir: str = None,
        db_id: str = None,
        query_string: str = None,
        payload: str = None,
        login_user: str = None,
        op_type: str = None,
        sip: str = None,
        dip: str = None,
        result: str = None,
        accessid: str = None,
        sessionid: str = None,
        sqlid: str = None,
        db_type: str = None,
        sport: str = None,
        dport: str = None,
        smac: str = None,
        dmac: str = None,
        db_name: str = None,
        client_prg: str = None,
        host_name: str = None,
        client_user: str = None,
        sql_len: str = None,
        effect_row: str = None,
        cost: str = None,
        result_desc: str = None,
        data_set: str = None,
        alarm_name: str = None,
        alarm_level: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.start_time = start_time
        self.end_time = end_time
        self.current_page = current_page
        self.page_size = page_size
        self.sort = sort
        self.dir = dir
        self.db_id = db_id
        self.query_string = query_string
        self.payload = payload
        self.login_user = login_user
        self.op_type = op_type
        self.sip = sip
        self.dip = dip
        self.result = result
        self.accessid = accessid
        self.sessionid = sessionid
        self.sqlid = sqlid
        self.db_type = db_type
        self.sport = sport
        self.dport = dport
        self.smac = smac
        self.dmac = dmac
        self.db_name = db_name
        self.client_prg = client_prg
        self.host_name = host_name
        self.client_user = client_user
        self.sql_len = sql_len
        self.effect_row = effect_row
        self.cost = cost
        self.result_desc = result_desc
        self.data_set = data_set
        self.alarm_name = alarm_name
        self.alarm_level = alarm_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.query_string is not None:
            result['QueryString'] = self.query_string
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.result is not None:
            result['Result'] = self.result
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        if self.sqlid is not None:
            result['Sqlid'] = self.sqlid
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.sql_len is not None:
            result['SqlLen'] = self.sql_len
        if self.effect_row is not None:
            result['EffectRow'] = self.effect_row
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.result_desc is not None:
            result['ResultDesc'] = self.result_desc
        if self.data_set is not None:
            result['DataSet'] = self.data_set
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('QueryString') is not None:
            self.query_string = m.get('QueryString')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        if m.get('Sqlid') is not None:
            self.sqlid = m.get('Sqlid')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('SqlLen') is not None:
            self.sql_len = m.get('SqlLen')
        if m.get('EffectRow') is not None:
            self.effect_row = m.get('EffectRow')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('ResultDesc') is not None:
            self.result_desc = m.get('ResultDesc')
        if m.get('DataSet') is not None:
            self.data_set = m.get('DataSet')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        return self


class DescribeAuditLogsResponseBodyAuditLogs(TeaModel):
    def __init__(
        self,
        client_user: str = None,
        effect_row: int = None,
        c_5: str = None,
        client_prg: str = None,
        accessid: str = None,
        result_desc: str = None,
        sql_len: int = None,
        payload: str = None,
        c_4: str = None,
        date_time: str = None,
        db_name: str = None,
        data_set: str = None,
        sqlid: str = None,
        relate_ip: str = None,
        alarm_level: int = None,
        c_2: str = None,
        dip: str = None,
        result: int = None,
        cost: int = None,
        relate_user: str = None,
        sip: str = None,
        c_3: str = None,
        host_name: str = None,
        alarm_name: str = None,
        pick_ip: str = None,
        relate_info: str = None,
        pick_user: str = None,
        op_type: str = None,
        sport: int = None,
        data_set_size: int = None,
        db_type: str = None,
        alarm_flag: int = None,
        smac: int = None,
        dport: int = None,
        c_1: str = None,
        dmac: int = None,
        login_user: str = None,
        sessionid: str = None,
    ):
        self.client_user = client_user
        self.effect_row = effect_row
        self.c_5 = c_5
        self.client_prg = client_prg
        self.accessid = accessid
        self.result_desc = result_desc
        self.sql_len = sql_len
        self.payload = payload
        self.c_4 = c_4
        self.date_time = date_time
        self.db_name = db_name
        self.data_set = data_set
        self.sqlid = sqlid
        self.relate_ip = relate_ip
        self.alarm_level = alarm_level
        self.c_2 = c_2
        self.dip = dip
        self.result = result
        self.cost = cost
        self.relate_user = relate_user
        self.sip = sip
        self.c_3 = c_3
        self.host_name = host_name
        self.alarm_name = alarm_name
        self.pick_ip = pick_ip
        self.relate_info = relate_info
        self.pick_user = pick_user
        self.op_type = op_type
        self.sport = sport
        self.data_set_size = data_set_size
        self.db_type = db_type
        self.alarm_flag = alarm_flag
        self.smac = smac
        self.dport = dport
        self.c_1 = c_1
        self.dmac = dmac
        self.login_user = login_user
        self.sessionid = sessionid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.effect_row is not None:
            result['EffectRow'] = self.effect_row
        if self.c_5 is not None:
            result['C5'] = self.c_5
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.result_desc is not None:
            result['ResultDesc'] = self.result_desc
        if self.sql_len is not None:
            result['SqlLen'] = self.sql_len
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.c_4 is not None:
            result['C4'] = self.c_4
        if self.date_time is not None:
            result['DateTime'] = self.date_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.data_set is not None:
            result['DataSet'] = self.data_set
        if self.sqlid is not None:
            result['Sqlid'] = self.sqlid
        if self.relate_ip is not None:
            result['RelateIp'] = self.relate_ip
        if self.alarm_level is not None:
            result['AlarmLevel'] = self.alarm_level
        if self.c_2 is not None:
            result['C2'] = self.c_2
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.result is not None:
            result['Result'] = self.result
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.relate_user is not None:
            result['RelateUser'] = self.relate_user
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.c_3 is not None:
            result['C3'] = self.c_3
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name
        if self.pick_ip is not None:
            result['PickIp'] = self.pick_ip
        if self.relate_info is not None:
            result['RelateInfo'] = self.relate_info
        if self.pick_user is not None:
            result['PickUser'] = self.pick_user
        if self.op_type is not None:
            result['OpType'] = self.op_type
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.data_set_size is not None:
            result['DataSetSize'] = self.data_set_size
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.alarm_flag is not None:
            result['AlarmFlag'] = self.alarm_flag
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.c_1 is not None:
            result['C1'] = self.c_1
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('EffectRow') is not None:
            self.effect_row = m.get('EffectRow')
        if m.get('C5') is not None:
            self.c_5 = m.get('C5')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('ResultDesc') is not None:
            self.result_desc = m.get('ResultDesc')
        if m.get('SqlLen') is not None:
            self.sql_len = m.get('SqlLen')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('C4') is not None:
            self.c_4 = m.get('C4')
        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DataSet') is not None:
            self.data_set = m.get('DataSet')
        if m.get('Sqlid') is not None:
            self.sqlid = m.get('Sqlid')
        if m.get('RelateIp') is not None:
            self.relate_ip = m.get('RelateIp')
        if m.get('AlarmLevel') is not None:
            self.alarm_level = m.get('AlarmLevel')
        if m.get('C2') is not None:
            self.c_2 = m.get('C2')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('RelateUser') is not None:
            self.relate_user = m.get('RelateUser')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('C3') is not None:
            self.c_3 = m.get('C3')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')
        if m.get('PickIp') is not None:
            self.pick_ip = m.get('PickIp')
        if m.get('RelateInfo') is not None:
            self.relate_info = m.get('RelateInfo')
        if m.get('PickUser') is not None:
            self.pick_user = m.get('PickUser')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('DataSetSize') is not None:
            self.data_set_size = m.get('DataSetSize')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('AlarmFlag') is not None:
            self.alarm_flag = m.get('AlarmFlag')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('C1') is not None:
            self.c_1 = m.get('C1')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        return self


class DescribeAuditLogsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        audit_logs: List[DescribeAuditLogsResponseBodyAuditLogs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.audit_logs = audit_logs

    def validate(self):
        if self.audit_logs:
            for k in self.audit_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AuditLogs'] = []
        if self.audit_logs is not None:
            for k in self.audit_logs:
                result['AuditLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.audit_logs = []
        if m.get('AuditLogs') is not None:
            for k in m.get('AuditLogs'):
                temp_model = DescribeAuditLogsResponseBodyAuditLogs()
                self.audit_logs.append(temp_model.from_map(k))
        return self


class DescribeAuditLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAuditLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttribueRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.lang = lang
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttribueResponseBodyInstanceAttribue(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        expire_time: int = None,
        instance_id: str = None,
        internet_endpoint: str = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        series_code: str = None,
        description: str = None,
        instance_status: int = None,
        license_code: str = None,
        public_network_access: bool = None,
        white_list: List[str] = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.internet_endpoint = internet_endpoint
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.series_code = series_code
        self.description = description
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_network_access = public_network_access
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeInstanceAttribueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_attribue: DescribeInstanceAttribueResponseBodyInstanceAttribue = None,
    ):
        self.request_id = request_id
        self.instance_attribue = instance_attribue

    def validate(self):
        if self.instance_attribue:
            self.instance_attribue.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribue is not None:
            result['InstanceAttribue'] = self.instance_attribue.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribue') is not None:
            temp_model = DescribeInstanceAttribueResponseBodyInstanceAttribue()
            self.instance_attribue = temp_model.from_map(m['InstanceAttribue'])
        return self


class DescribeInstanceAttribueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAttribueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttribueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        expire_time: int = None,
        image_version: str = None,
        instance_id: str = None,
        internet_endpoint: str = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        series_code: str = None,
        description: str = None,
        instance_status: str = None,
        license_code: str = None,
        public_network_access: bool = None,
        white_list: List[str] = None,
        ipv_6white_list: List[str] = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.expire_time = expire_time
        self.image_version = image_version
        self.instance_id = instance_id
        self.internet_endpoint = internet_endpoint
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.series_code = series_code
        self.description = description
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_network_access = public_network_access
        self.white_list = white_list
        self.ipv_6white_list = ipv_6white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        if self.ipv_6white_list is not None:
            result['Ipv6WhiteList'] = self.ipv_6white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        if m.get('Ipv6WhiteList') is not None:
            self.ipv_6white_list = m.get('Ipv6WhiteList')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_attribute: DescribeInstanceAttributeResponseBodyInstanceAttribute = None,
    ):
        self.request_id = request_id
        self.instance_attribute = instance_attribute

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        current_page: int = None,
        region_id: str = None,
        instance_status: str = None,
        resource_group_id: str = None,
        instance_id: List[str] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.page_size = page_size
        self.current_page = current_page
        self.region_id = region_id
        self.instance_status = instance_status
        self.resource_group_id = resource_group_id
        self.instance_id = instance_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        expire_time: int = None,
        image_version: str = None,
        instance_id: str = None,
        internet_endpoint: str = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        series_code: str = None,
        description: str = None,
        instance_status: str = None,
        license_code: str = None,
        public_network_access: bool = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.expire_time = expire_time
        self.image_version = image_version
        self.instance_id = instance_id
        self.internet_endpoint = internet_endpoint
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.series_code = series_code
        self.description = description
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_network_access = public_network_access

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStorageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceStorageResponseBodyInstanceStorages(TeaModel):
    def __init__(
        self,
        storage_time: int = None,
        storage_capacity: int = None,
        storage_category: str = None,
        storage_space: str = None,
        storage_used: int = None,
    ):
        self.storage_time = storage_time
        self.storage_capacity = storage_capacity
        self.storage_category = storage_category
        self.storage_space = storage_space
        self.storage_used = storage_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_time is not None:
            result['StorageTime'] = self.storage_time
        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageTime') is not None:
            self.storage_time = m.get('StorageTime')
        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        return self


class DescribeInstanceStorageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_storages: List[DescribeInstanceStorageResponseBodyInstanceStorages] = None,
    ):
        self.request_id = request_id
        self.instance_storages = instance_storages

    def validate(self):
        if self.instance_storages:
            for k in self.instance_storages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceStorages'] = []
        if self.instance_storages is not None:
            for k in self.instance_storages:
                result['InstanceStorages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_storages = []
        if m.get('InstanceStorages') is not None:
            for k in m.get('InstanceStorages'):
                temp_model = DescribeInstanceStorageResponseBodyInstanceStorages()
                self.instance_storages.append(temp_model.from_map(k))
        return self


class DescribeInstanceStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceStorageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        self.region_endpoint = region_endpoint
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRenewStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRenewStatusResponseBodyInstances(TeaModel):
    def __init__(
        self,
        renew_status: str = None,
        instance_id: str = None,
    ):
        self.renew_status = renew_status
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeRenewStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instances: List[DescribeRenewStatusResponseBodyInstances] = None,
    ):
        self.request_id = request_id
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeRenewStatusResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeRenewStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRenewStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRenewStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSessionLogsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        start_time: str = None,
        end_time: str = None,
        current_page: int = None,
        page_size: int = None,
        sort: str = None,
        dir: str = None,
        db_id: str = None,
        sip: str = None,
        sport: str = None,
        login_user: str = None,
        dip: str = None,
        dport: str = None,
        sessionid: str = None,
        db_type: str = None,
        smac: str = None,
        dmac: str = None,
        client_prg: str = None,
        host_name: str = None,
        client_user: str = None,
        db_name: str = None,
        session_status: str = None,
        sql_count: str = None,
        req_flow: str = None,
        rsp_flow: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.start_time = start_time
        self.end_time = end_time
        self.current_page = current_page
        self.page_size = page_size
        self.sort = sort
        self.dir = dir
        self.db_id = db_id
        self.sip = sip
        self.sport = sport
        self.login_user = login_user
        self.dip = dip
        self.dport = dport
        self.sessionid = sessionid
        self.db_type = db_type
        self.smac = smac
        self.dmac = dmac
        self.client_prg = client_prg
        self.host_name = host_name
        self.client_user = client_user
        self.db_name = db_name
        self.session_status = session_status
        self.sql_count = sql_count
        self.req_flow = req_flow
        self.rsp_flow = rsp_flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.req_flow is not None:
            result['ReqFlow'] = self.req_flow
        if self.rsp_flow is not None:
            result['RspFlow'] = self.rsp_flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('ReqFlow') is not None:
            self.req_flow = m.get('ReqFlow')
        if m.get('RspFlow') is not None:
            self.rsp_flow = m.get('RspFlow')
        return self


class DescribeSessionLogsResponseBodySessionLogs(TeaModel):
    def __init__(
        self,
        client_user: str = None,
        session_status: int = None,
        c_5: str = None,
        client_prg: str = None,
        accessid: str = None,
        c_4: str = None,
        db_name: str = None,
        request_flow: int = None,
        pro_con: int = None,
        c_2: str = None,
        dip: str = None,
        sip: str = None,
        c_3: str = None,
        host_name: str = None,
        response_flow: int = None,
        encode: str = None,
        normal_end: int = None,
        end_time: int = None,
        sport: int = None,
        start_time: int = None,
        db_type: str = None,
        str_info: str = None,
        sql_count: int = None,
        smac: int = None,
        dport: int = None,
        dmac: int = None,
        c_1: str = None,
        login_user: str = None,
        sessionid: str = None,
    ):
        self.client_user = client_user
        self.session_status = session_status
        self.c_5 = c_5
        self.client_prg = client_prg
        self.accessid = accessid
        self.c_4 = c_4
        self.db_name = db_name
        self.request_flow = request_flow
        self.pro_con = pro_con
        self.c_2 = c_2
        self.dip = dip
        self.sip = sip
        self.c_3 = c_3
        self.host_name = host_name
        self.response_flow = response_flow
        self.encode = encode
        self.normal_end = normal_end
        self.end_time = end_time
        self.sport = sport
        self.start_time = start_time
        self.db_type = db_type
        self.str_info = str_info
        self.sql_count = sql_count
        self.smac = smac
        self.dport = dport
        self.dmac = dmac
        self.c_1 = c_1
        self.login_user = login_user
        self.sessionid = sessionid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.c_5 is not None:
            result['C5'] = self.c_5
        if self.client_prg is not None:
            result['ClientPrg'] = self.client_prg
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.c_4 is not None:
            result['C4'] = self.c_4
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.request_flow is not None:
            result['RequestFlow'] = self.request_flow
        if self.pro_con is not None:
            result['ProCon'] = self.pro_con
        if self.c_2 is not None:
            result['C2'] = self.c_2
        if self.dip is not None:
            result['Dip'] = self.dip
        if self.sip is not None:
            result['Sip'] = self.sip
        if self.c_3 is not None:
            result['C3'] = self.c_3
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.response_flow is not None:
            result['ResponseFlow'] = self.response_flow
        if self.encode is not None:
            result['Encode'] = self.encode
        if self.normal_end is not None:
            result['NormalEnd'] = self.normal_end
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.sport is not None:
            result['Sport'] = self.sport
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.str_info is not None:
            result['StrInfo'] = self.str_info
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.smac is not None:
            result['Smac'] = self.smac
        if self.dport is not None:
            result['Dport'] = self.dport
        if self.dmac is not None:
            result['Dmac'] = self.dmac
        if self.c_1 is not None:
            result['C1'] = self.c_1
        if self.login_user is not None:
            result['LoginUser'] = self.login_user
        if self.sessionid is not None:
            result['Sessionid'] = self.sessionid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('C5') is not None:
            self.c_5 = m.get('C5')
        if m.get('ClientPrg') is not None:
            self.client_prg = m.get('ClientPrg')
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('C4') is not None:
            self.c_4 = m.get('C4')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RequestFlow') is not None:
            self.request_flow = m.get('RequestFlow')
        if m.get('ProCon') is not None:
            self.pro_con = m.get('ProCon')
        if m.get('C2') is not None:
            self.c_2 = m.get('C2')
        if m.get('Dip') is not None:
            self.dip = m.get('Dip')
        if m.get('Sip') is not None:
            self.sip = m.get('Sip')
        if m.get('C3') is not None:
            self.c_3 = m.get('C3')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ResponseFlow') is not None:
            self.response_flow = m.get('ResponseFlow')
        if m.get('Encode') is not None:
            self.encode = m.get('Encode')
        if m.get('NormalEnd') is not None:
            self.normal_end = m.get('NormalEnd')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Sport') is not None:
            self.sport = m.get('Sport')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('StrInfo') is not None:
            self.str_info = m.get('StrInfo')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('Smac') is not None:
            self.smac = m.get('Smac')
        if m.get('Dport') is not None:
            self.dport = m.get('Dport')
        if m.get('Dmac') is not None:
            self.dmac = m.get('Dmac')
        if m.get('C1') is not None:
            self.c_1 = m.get('C1')
        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')
        if m.get('Sessionid') is not None:
            self.sessionid = m.get('Sessionid')
        return self


class DescribeSessionLogsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        session_logs: List[DescribeSessionLogsResponseBodySessionLogs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.session_logs = session_logs

    def validate(self):
        if self.session_logs:
            for k in self.session_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SessionLogs'] = []
        if self.session_logs is not None:
            for k in self.session_logs:
                result['SessionLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.session_logs = []
        if m.get('SessionLogs') is not None:
            for k in m.get('SessionLogs'):
                temp_model = DescribeSessionLogsResponseBodySessionLogs()
                self.session_logs.append(temp_model.from_map(k))
        return self


class DescribeSessionLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSessionLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSessionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableInstancePublicAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableInstancePublicAccessResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableInstancePublicAccessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableInstancePublicAccessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadAuthRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GenerateUploadAuthResponseBodyUploadConfig(TeaModel):
    def __init__(
        self,
        signature: str = None,
        file_path: str = None,
        policy: str = None,
        expire_time: int = None,
        upload_host: str = None,
        access_id: str = None,
    ):
        self.signature = signature
        self.file_path = file_path
        self.policy = policy
        self.expire_time = expire_time
        self.upload_host = upload_host
        self.access_id = access_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upload_host is not None:
            result['UploadHost'] = self.upload_host
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('UploadHost') is not None:
            self.upload_host = m.get('UploadHost')
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        return self


class GenerateUploadAuthResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upload_config: GenerateUploadAuthResponseBodyUploadConfig = None,
    ):
        self.request_id = request_id
        self.upload_config = upload_config

    def validate(self):
        if self.upload_config:
            self.upload_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upload_config is not None:
            result['UploadConfig'] = self.upload_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UploadConfig') is not None:
            temp_model = GenerateUploadAuthResponseBodyUploadConfig()
            self.upload_config = temp_model.from_map(m['UploadConfig'])
        return self


class GenerateUploadAuthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateUploadAuthResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateUploadAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantServiceRoleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GrantServiceRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GrantServiceRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantServiceRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GrantServiceRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        self.tag_count = tag_count
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        description: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.description = description
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceStorageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        storage_space: str = None,
        storage_category: str = None,
        storage_time: int = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.storage_space = storage_space
        self.storage_category = storage_category
        self.storage_time = storage_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_space is not None:
            result['StorageSpace'] = self.storage_space
        if self.storage_category is not None:
            result['StorageCategory'] = self.storage_category
        if self.storage_time is not None:
            result['StorageTime'] = self.storage_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSpace') is not None:
            self.storage_space = m.get('StorageSpace')
        if m.get('StorageCategory') is not None:
            self.storage_category = m.get('StorageCategory')
        if m.get('StorageTime') is not None:
            self.storage_time = m.get('StorageTime')
        return self


class ModifyInstanceStorageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceStorageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        region_id: str = None,
    ):
        self.resource_id = resource_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
        service_code: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RefundInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefundInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        vswitch_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.vswitch_id = vswitch_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


