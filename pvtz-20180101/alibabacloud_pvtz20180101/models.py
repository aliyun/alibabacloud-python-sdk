# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddZoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_name: str = None,
        user_client_ip: str = None,
        proxy_pattern: str = None,
        resource_group_id: str = None,
        zone_type: str = None,
        zone_tag: str = None,
    ):
        self.lang = lang
        self.zone_name = zone_name
        self.user_client_ip = user_client_ip
        self.proxy_pattern = proxy_pattern
        self.resource_group_id = resource_group_id
        self.zone_type = zone_type
        self.zone_tag = zone_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        return self


class AddZoneResponseBody(TeaModel):
    def __init__(
        self,
        zone_name: str = None,
        zone_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.zone_name = zone_name
        self.zone_id = zone_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddZoneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AddZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddZoneRecordRequest(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        lang: str = None,
        rr: str = None,
        type: str = None,
        ttl: int = None,
        priority: int = None,
        value: str = None,
        user_client_ip: str = None,
    ):
        self.zone_id = zone_id
        self.lang = lang
        self.rr = rr
        self.type = type
        self.ttl = ttl
        self.priority = priority
        self.value = value
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.type is not None:
            result['Type'] = self.type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.value is not None:
            result['Value'] = self.value
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class AddZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.record_id = record_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = AddZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindZoneVpcRequestVpcs(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        region_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BindZoneVpcRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
        user_client_ip: str = None,
        vpcs: List[BindZoneVpcRequestVpcs] = None,
    ):
        self.lang = lang
        self.zone_id = zone_id
        self.user_client_ip = user_client_ip
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = BindZoneVpcRequestVpcs()
                self.vpcs.append(temp_model.from_map(k))
        return self


class BindZoneVpcResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindZoneVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindZoneVpcResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = BindZoneVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckZoneNameRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_name: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.zone_name = zone_name
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class CheckZoneNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        check: bool = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.check = check
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.check is not None:
            result['Check'] = self.check
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Check') is not None:
            self.check = m.get('Check')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckZoneNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckZoneNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = CheckZoneNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.zone_id = zone_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteZoneResponseBody(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        request_id: str = None,
    ):
        self.zone_id = zone_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteZoneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteZoneRecordRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DeleteZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: int = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class DeleteZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DeleteZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeLogsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        zone_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
        entity_type: str = None,
        user_client_ip: str = None,
    ):
        self.keyword = keyword
        self.lang = lang
        self.zone_id = zone_id
        self.page_number = page_number
        self.page_size = page_size
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.entity_type = entity_type
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeChangeLogsResponseBodyChangeLogsChangeLog(TeaModel):
    def __init__(
        self,
        oper_timestamp: int = None,
        entity_id: str = None,
        oper_object: str = None,
        oper_time: str = None,
        oper_ip: str = None,
        oper_action: str = None,
        content: str = None,
        entity_name: str = None,
        id: int = None,
    ):
        self.oper_timestamp = oper_timestamp
        self.entity_id = entity_id
        self.oper_object = oper_object
        self.oper_time = oper_time
        self.oper_ip = oper_ip
        self.oper_action = oper_action
        self.content = content
        self.entity_name = entity_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.oper_timestamp is not None:
            result['OperTimestamp'] = self.oper_timestamp
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.oper_object is not None:
            result['OperObject'] = self.oper_object
        if self.oper_time is not None:
            result['OperTime'] = self.oper_time
        if self.oper_ip is not None:
            result['OperIp'] = self.oper_ip
        if self.oper_action is not None:
            result['OperAction'] = self.oper_action
        if self.content is not None:
            result['Content'] = self.content
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperTimestamp') is not None:
            self.oper_timestamp = m.get('OperTimestamp')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('OperObject') is not None:
            self.oper_object = m.get('OperObject')
        if m.get('OperTime') is not None:
            self.oper_time = m.get('OperTime')
        if m.get('OperIp') is not None:
            self.oper_ip = m.get('OperIp')
        if m.get('OperAction') is not None:
            self.oper_action = m.get('OperAction')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeChangeLogsResponseBodyChangeLogs(TeaModel):
    def __init__(
        self,
        change_log: List[DescribeChangeLogsResponseBodyChangeLogsChangeLog] = None,
    ):
        self.change_log = change_log

    def validate(self):
        if self.change_log:
            for k in self.change_log:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k in self.change_log:
                result['ChangeLog'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k in m.get('ChangeLog'):
                temp_model = DescribeChangeLogsResponseBodyChangeLogsChangeLog()
                self.change_log.append(temp_model.from_map(k))
        return self


class DescribeChangeLogsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        change_logs: DescribeChangeLogsResponseBodyChangeLogs = None,
        page_number: int = None,
        total_pages: int = None,
        total_items: int = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.change_logs = change_logs
        self.page_number = page_number
        self.total_pages = total_pages
        self.total_items = total_items

    def validate(self):
        if self.change_logs:
            self.change_logs.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.change_logs is not None:
            result['ChangeLogs'] = self.change_logs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChangeLogs') is not None:
            temp_model = DescribeChangeLogsResponseBodyChangeLogs()
            self.change_logs = temp_model.from_map(m['ChangeLogs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        return self


class DescribeChangeLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeChangeLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeChangeLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        accept_language: str = None,
        authorized_user_id: int = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.accept_language = accept_language
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_name = region_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
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


class DescribeRequestGraphRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
        vpc_id: str = None,
        start_timestamp: int = None,
        end_timestamp: int = None,
        biz_type: str = None,
        biz_id: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip
        self.zone_id = zone_id
        self.vpc_id = vpc_id
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.biz_type = biz_type
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop(TeaModel):
    def __init__(
        self,
        time: str = None,
        request_count: int = None,
        timestamp: int = None,
    ):
        self.time = time
        self.request_count = request_count
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeRequestGraphResponseBodyRequestDetails(TeaModel):
    def __init__(
        self,
        zone_request_top: List[DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for k in self.zone_request_top:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k in self.zone_request_top:
                result['ZoneRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k in m.get('ZoneRequestTop'):
                temp_model = DescribeRequestGraphResponseBodyRequestDetailsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k))
        return self


class DescribeRequestGraphResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        request_details: DescribeRequestGraphResponseBodyRequestDetails = None,
    ):
        self.request_id = request_id
        self.request_details = request_details

    def validate(self):
        if self.request_details:
            self.request_details.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_details is not None:
            result['RequestDetails'] = self.request_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestDetails') is not None:
            temp_model = DescribeRequestGraphResponseBodyRequestDetails()
            self.request_details = temp_model.from_map(m['RequestDetails'])
        return self


class DescribeRequestGraphResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRequestGraphResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeRequestGraphResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStatisticSummaryRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop(TeaModel):
    def __init__(
        self,
        request_count: int = None,
        zone_name: str = None,
        biz_type: str = None,
    ):
        self.request_count = request_count
        self.zone_name = zone_name
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class DescribeStatisticSummaryResponseBodyZoneRequestTops(TeaModel):
    def __init__(
        self,
        zone_request_top: List[DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop] = None,
    ):
        self.zone_request_top = zone_request_top

    def validate(self):
        if self.zone_request_top:
            for k in self.zone_request_top:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ZoneRequestTop'] = []
        if self.zone_request_top is not None:
            for k in self.zone_request_top:
                result['ZoneRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_request_top = []
        if m.get('ZoneRequestTop') is not None:
            for k in m.get('ZoneRequestTop'):
                temp_model = DescribeStatisticSummaryResponseBodyZoneRequestTopsZoneRequestTop()
                self.zone_request_top.append(temp_model.from_map(k))
        return self


class DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        region_name: str = None,
        tunnel_id: str = None,
        request_count: int = None,
        region_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.region_name = region_name
        self.tunnel_id = tunnel_id
        self.request_count = request_count
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeStatisticSummaryResponseBodyVpcRequestTops(TeaModel):
    def __init__(
        self,
        vpc_request_top: List[DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop] = None,
    ):
        self.vpc_request_top = vpc_request_top

    def validate(self):
        if self.vpc_request_top:
            for k in self.vpc_request_top:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['VpcRequestTop'] = []
        if self.vpc_request_top is not None:
            for k in self.vpc_request_top:
                result['VpcRequestTop'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc_request_top = []
        if m.get('VpcRequestTop') is not None:
            for k in m.get('VpcRequestTop'):
                temp_model = DescribeStatisticSummaryResponseBodyVpcRequestTopsVpcRequestTop()
                self.vpc_request_top.append(temp_model.from_map(k))
        return self


class DescribeStatisticSummaryResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        zone_request_tops: DescribeStatisticSummaryResponseBodyZoneRequestTops = None,
        vpc_request_tops: DescribeStatisticSummaryResponseBodyVpcRequestTops = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.zone_request_tops = zone_request_tops
        self.vpc_request_tops = vpc_request_tops

    def validate(self):
        if self.zone_request_tops:
            self.zone_request_tops.validate()
        if self.vpc_request_tops:
            self.vpc_request_tops.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_request_tops is not None:
            result['ZoneRequestTops'] = self.zone_request_tops.to_map()
        if self.vpc_request_tops is not None:
            result['VpcRequestTops'] = self.vpc_request_tops.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneRequestTops') is not None:
            temp_model = DescribeStatisticSummaryResponseBodyZoneRequestTops()
            self.zone_request_tops = temp_model.from_map(m['ZoneRequestTops'])
        if m.get('VpcRequestTops') is not None:
            temp_model = DescribeStatisticSummaryResponseBodyVpcRequestTops()
            self.vpc_request_tops = temp_model.from_map(m['VpcRequestTops'])
        return self


class DescribeStatisticSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStatisticSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeStatisticSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserServiceStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeUserServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeUserServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.zone_id = zone_id
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeZoneInfoResponseBodyBindVpcsVpc(TeaModel):
    def __init__(
        self,
        vpc_name: str = None,
        vpc_id: str = None,
        region_name: str = None,
        vpc_user_id: int = None,
        region_id: str = None,
    ):
        self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        self.region_name = region_name
        self.vpc_user_id = vpc_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.vpc_user_id is not None:
            result['VpcUserId'] = self.vpc_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('VpcUserId') is not None:
            self.vpc_user_id = m.get('VpcUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZoneInfoResponseBodyBindVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeZoneInfoResponseBodyBindVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeZoneInfoResponseBodyBindVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeZoneInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        slave_dns: bool = None,
        resource_group_id: str = None,
        zone_id: str = None,
        proxy_pattern: str = None,
        create_time: str = None,
        zone_type: str = None,
        remark: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        update_time: str = None,
        update_timestamp: int = None,
        record_count: int = None,
        create_timestamp: int = None,
        bind_vpcs: DescribeZoneInfoResponseBodyBindVpcs = None,
        is_ptr: bool = None,
    ):
        self.request_id = request_id
        self.slave_dns = slave_dns
        self.resource_group_id = resource_group_id
        self.zone_id = zone_id
        self.proxy_pattern = proxy_pattern
        self.create_time = create_time
        self.zone_type = zone_type
        self.remark = remark
        self.zone_name = zone_name
        self.zone_tag = zone_tag
        self.update_time = update_time
        self.update_timestamp = update_timestamp
        self.record_count = record_count
        self.create_timestamp = create_timestamp
        self.bind_vpcs = bind_vpcs
        self.is_ptr = is_ptr

    def validate(self):
        if self.bind_vpcs:
            self.bind_vpcs.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slave_dns is not None:
            result['SlaveDns'] = self.slave_dns
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.bind_vpcs is not None:
            result['BindVpcs'] = self.bind_vpcs.to_map()
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlaveDns') is not None:
            self.slave_dns = m.get('SlaveDns')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('BindVpcs') is not None:
            temp_model = DescribeZoneInfoResponseBodyBindVpcs()
            self.bind_vpcs = temp_model.from_map(m['BindVpcs'])
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        return self


class DescribeZoneInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZoneInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeZoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneRecordsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        keyword: str = None,
        zone_id: str = None,
        page_number: int = None,
        page_size: int = None,
        user_client_ip: str = None,
        tag: str = None,
        search_mode: str = None,
        order_by: str = None,
        direction: str = None,
    ):
        self.lang = lang
        self.keyword = keyword
        self.zone_id = zone_id
        self.page_number = page_number
        self.page_size = page_size
        self.user_client_ip = user_client_ip
        self.tag = tag
        self.search_mode = search_mode
        self.order_by = order_by
        self.direction = direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.direction is not None:
            result['Direction'] = self.direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        return self


class DescribeZoneRecordsResponseBodyRecordsRecord(TeaModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
        value: str = None,
        ttl: int = None,
        remark: str = None,
        record_id: int = None,
        rr: str = None,
        priority: int = None,
    ):
        self.status = status
        self.type = type
        self.value = value
        self.ttl = ttl
        self.remark = remark
        self.record_id = record_id
        self.rr = rr
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class DescribeZoneRecordsResponseBodyRecords(TeaModel):
    def __init__(
        self,
        record: List[DescribeZoneRecordsResponseBodyRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeZoneRecordsResponseBodyRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeZoneRecordsResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_pages: int = None,
        total_items: int = None,
        records: DescribeZoneRecordsResponseBodyRecords = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_pages = total_pages
        self.total_items = total_items
        self.records = records

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.records is not None:
            result['Records'] = self.records.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('Records') is not None:
            temp_model = DescribeZoneRecordsResponseBodyRecords()
            self.records = temp_model.from_map(m['Records'])
        return self


class DescribeZoneRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZoneRecordsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeZoneRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        keyword: str = None,
        user_client_ip: str = None,
        search_mode: str = None,
        query_region_id: str = None,
        query_vpc_id: str = None,
        resource_group_id: str = None,
        order_by: str = None,
        direction: str = None,
        zone_type: str = None,
        zone_tag: List[str] = None,
    ):
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.keyword = keyword
        self.user_client_ip = user_client_ip
        self.search_mode = search_mode
        self.query_region_id = query_region_id
        self.query_vpc_id = query_vpc_id
        self.resource_group_id = resource_group_id
        self.order_by = order_by
        self.direction = direction
        self.zone_type = zone_type
        self.zone_tag = zone_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode
        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id
        if self.query_vpc_id is not None:
            result['QueryVpcId'] = self.query_vpc_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')
        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')
        if m.get('QueryVpcId') is not None:
            self.query_vpc_id = m.get('QueryVpcId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        zone_type: str = None,
        remark: str = None,
        create_time: str = None,
        record_count: int = None,
        zone_name: str = None,
        proxy_pattern: str = None,
        update_timestamp: int = None,
        resource_group_id: str = None,
        zone_id: str = None,
        zone_tag: str = None,
        is_ptr: bool = None,
        create_timestamp: int = None,
    ):
        self.update_time = update_time
        self.zone_type = zone_type
        self.remark = remark
        self.create_time = create_time
        self.record_count = record_count
        self.zone_name = zone_name
        self.proxy_pattern = proxy_pattern
        self.update_timestamp = update_timestamp
        self.resource_group_id = resource_group_id
        self.zone_id = zone_id
        self.zone_tag = zone_tag
        self.is_ptr = is_ptr
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZonesResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total_pages: int = None,
        total_items: int = None,
        zones: DescribeZonesResponseBodyZones = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total_pages = total_pages
        self.total_items = total_items
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        if self.total_items is not None:
            result['TotalItems'] = self.total_items
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZoneVpcTreeRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc(TeaModel):
    def __init__(
        self,
        vpc_name: str = None,
        vpc_id: str = None,
        region_name: str = None,
        region_id: str = None,
    ):
        self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        self.region_name = region_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZoneVpcTreeResponseBodyZonesZoneVpcs(TeaModel):
    def __init__(
        self,
        vpc: List[DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for k in self.vpc:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Vpc'] = []
        if self.vpc is not None:
            for k in self.vpc:
                result['Vpc'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k in m.get('Vpc'):
                temp_model = DescribeZoneVpcTreeResponseBodyZonesZoneVpcsVpc()
                self.vpc.append(temp_model.from_map(k))
        return self


class DescribeZoneVpcTreeResponseBodyZonesZone(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        zone_type: str = None,
        remark: str = None,
        create_time: str = None,
        vpcs: DescribeZoneVpcTreeResponseBodyZonesZoneVpcs = None,
        record_count: int = None,
        zone_name: str = None,
        update_timestamp: int = None,
        zone_id: str = None,
        zone_tag: str = None,
        is_ptr: bool = None,
        create_timestamp: int = None,
    ):
        self.update_time = update_time
        self.zone_type = zone_type
        self.remark = remark
        self.create_time = create_time
        self.vpcs = vpcs
        self.record_count = record_count
        self.zone_name = zone_name
        self.update_timestamp = update_timestamp
        self.zone_id = zone_id
        self.zone_tag = zone_tag
        self.is_ptr = is_ptr
        self.create_timestamp = create_timestamp

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()
        if self.record_count is not None:
            result['RecordCount'] = self.record_count
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag
        if self.is_ptr is not None:
            result['IsPtr'] = self.is_ptr
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Vpcs') is not None:
            temp_model = DescribeZoneVpcTreeResponseBodyZonesZoneVpcs()
            self.vpcs = temp_model.from_map(m['Vpcs'])
        if m.get('RecordCount') is not None:
            self.record_count = m.get('RecordCount')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')
        if m.get('IsPtr') is not None:
            self.is_ptr = m.get('IsPtr')
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        return self


class DescribeZoneVpcTreeResponseBodyZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeZoneVpcTreeResponseBodyZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZoneVpcTreeResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZoneVpcTreeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeZoneVpcTreeResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZoneVpcTreeResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZoneVpcTreeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeZoneVpcTreeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = DescribeZoneVpcTreeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_id: str = None,
        user_client_ip: str = None,
        new_resource_group_id: str = None,
    ):
        self.lang = lang
        self.resource_id = resource_id
        self.user_client_ip = user_client_ip
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
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


class SetProxyPatternRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
        proxy_pattern: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.zone_id = zone_id
        self.proxy_pattern = proxy_pattern
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SetProxyPatternResponseBody(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        request_id: str = None,
    ):
        self.zone_id = zone_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetProxyPatternResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetProxyPatternResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetProxyPatternResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetZoneRecordStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        status: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.status = status
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class SetZoneRecordStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        record_id: int = None,
    ):
        self.status = status
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class SetZoneRecordStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetZoneRecordStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = SetZoneRecordStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        record_id: int = None,
        remark: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.record_id = record_id
        self.remark = remark
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class UpdateRecordRemarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: int = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class UpdateRecordRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRecordRemarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateRecordRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZoneRecordRequest(TeaModel):
    def __init__(
        self,
        rr: str = None,
        lang: str = None,
        record_id: int = None,
        type: str = None,
        ttl: int = None,
        priority: int = None,
        value: str = None,
        user_client_ip: str = None,
    ):
        self.rr = rr
        self.lang = lang
        self.record_id = record_id
        self.type = type
        self.ttl = ttl
        self.priority = priority
        self.value = value
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rr is not None:
            result['Rr'] = self.rr
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.type is not None:
            result['Type'] = self.type
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.value is not None:
            result['Value'] = self.value
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rr') is not None:
            self.rr = m.get('Rr')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class UpdateZoneRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        record_id: int = None,
    ):
        self.request_id = request_id
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class UpdateZoneRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateZoneRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateZoneRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateZoneRemarkRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        zone_id: str = None,
        remark: str = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        self.zone_id = zone_id
        self.remark = remark
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')
        return self


class UpdateZoneRemarkResponseBody(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        request_id: str = None,
    ):
        self.zone_id = zone_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateZoneRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateZoneRemarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateZoneRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


