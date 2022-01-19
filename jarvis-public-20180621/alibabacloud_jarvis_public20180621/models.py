# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateConsoleAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        dst_port: int = None,
        instance_id_list: str = None,
        instance_info_list: str = None,
        lang: str = None,
        live_time: int = None,
        note: str = None,
        product_name: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        white_list_type: int = None,
    ):
        self.dst_port = dst_port
        self.instance_id_list = instance_id_list
        self.instance_info_list = instance_info_list
        self.lang = lang
        self.live_time = live_time
        self.note = note
        self.product_name = product_name
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.white_list_type = white_list_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.instance_info_list is not None:
            result['InstanceInfoList'] = self.instance_info_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.live_time is not None:
            result['LiveTime'] = self.live_time
        if self.note is not None:
            result['Note'] = self.note
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('InstanceInfoList') is not None:
            self.instance_info_list = m.get('InstanceInfoList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LiveTime') is not None:
            self.live_time = m.get('LiveTime')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class CreateConsoleAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        module: str = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConsoleAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConsoleAccessWhiteListResponseBody = None,
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
            temp_model = CreateConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsoleAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        disable_whitelist: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.disable_whitelist = disable_whitelist
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disable_whitelist is not None:
            result['DisableWhitelist'] = self.disable_whitelist
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableWhitelist') is not None:
            self.disable_whitelist = m.get('DisableWhitelist')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteConsoleAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        module: str = None,
        request_id: str = None,
    ):
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConsoleAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConsoleAccessWhiteListResponseBody = None,
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
            temp_model = DeleteConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhiteListSlbListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAccessWhiteListSlbListResponseBodySlbList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
        item_sign: str = None,
        region: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.item_sign = item_sign
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.item_sign is not None:
            result['ItemSign'] = self.item_sign
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ItemSign') is not None:
            self.item_sign = m.get('ItemSign')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeAccessWhiteListSlbListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        slb_list: List[DescribeAccessWhiteListSlbListResponseBodySlbList] = None,
        total_count: int = None,
        module: str = None,
    ):
        self.request_id = request_id
        self.slb_list = slb_list
        self.total_count = total_count
        self.module = module

    def validate(self):
        if self.slb_list:
            for k in self.slb_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlbList'] = []
        if self.slb_list is not None:
            for k in self.slb_list:
                result['SlbList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slb_list = []
        if m.get('SlbList') is not None:
            for k in m.get('SlbList'):
                temp_model = DescribeAccessWhiteListSlbListResponseBodySlbList()
                self.slb_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhiteListSlbListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessWhiteListSlbListResponseBody = None,
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
            temp_model = DescribeAccessWhiteListSlbListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhitelistEcsListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAccessWhitelistEcsListResponseBodyEcsList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DescribeAccessWhitelistEcsListResponseBody(TeaModel):
    def __init__(
        self,
        ecs_list: List[DescribeAccessWhitelistEcsListResponseBodyEcsList] = None,
        request_id: str = None,
        total_count: int = None,
        module: str = None,
    ):
        self.ecs_list = ecs_list
        self.request_id = request_id
        self.total_count = total_count
        self.module = module

    def validate(self):
        if self.ecs_list:
            for k in self.ecs_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsList'] = []
        if self.ecs_list is not None:
            for k in self.ecs_list:
                result['EcsList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_list = []
        if m.get('EcsList') is not None:
            for k in m.get('EcsList'):
                temp_model = DescribeAccessWhitelistEcsListResponseBodyEcsList()
                self.ecs_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhitelistEcsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccessWhitelistEcsListResponseBody = None,
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
            temp_model = DescribeAccessWhitelistEcsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackEventRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        product_type: str = None,
        region: str = None,
        server_ip_list: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.product_type = product_type
        self.region = region
        self.server_ip_list = server_ip_list
        self.source_ip = source_ip
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.server_ip_list is not None:
            result['ServerIpList'] = self.server_ip_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServerIpList') is not None:
            self.server_ip_list = m.get('ServerIpList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAttackEventResponseBodyEventList(TeaModel):
    def __init__(
        self,
        attack_type: str = None,
        gmt_create: str = None,
        gmt_create_stamp: int = None,
        gmt_modified: str = None,
        source_ip: str = None,
        url: str = None,
        vm_ip: str = None,
    ):
        self.attack_type = attack_type
        self.gmt_create = gmt_create
        self.gmt_create_stamp = gmt_create_stamp
        self.gmt_modified = gmt_modified
        self.source_ip = source_ip
        self.url = url
        self.vm_ip = vm_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_create_stamp is not None:
            result['GmtCreateStamp'] = self.gmt_create_stamp
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.url is not None:
            result['Url'] = self.url
        if self.vm_ip is not None:
            result['VmIp'] = self.vm_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtCreateStamp') is not None:
            self.gmt_create_stamp = m.get('GmtCreateStamp')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VmIp') is not None:
            self.vm_ip = m.get('VmIp')
        return self


class DescribeAttackEventResponseBody(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeAttackEventResponseBodyEventList] = None,
        module: str = None,
        request_id: str = None,
    ):
        self.event_list = event_list
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeAttackEventResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAttackEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAttackEventResponseBody = None,
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
            temp_model = DescribeAttackEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttackedIpRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        product_type: str = None,
        region: str = None,
        server_ip_list: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.product_type = product_type
        self.region = region
        self.server_ip_list = server_ip_list
        self.source_ip = source_ip
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.server_ip_list is not None:
            result['ServerIpList'] = self.server_ip_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServerIpList') is not None:
            self.server_ip_list = m.get('ServerIpList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeAttackedIpResponseBody(TeaModel):
    def __init__(
        self,
        ip_list: List[str] = None,
        module: str = None,
        request_id: str = None,
    ):
        self.ip_list = ip_list
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAttackedIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAttackedIpResponseBody = None,
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
            temp_model = DescribeAttackedIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConsoleAccessWhiteListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dst_ip: str = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        status: str = None,
        white_list_type: int = None,
        query_product: str = None,
    ):
        self.current_page = current_page
        self.dst_ip = dst_ip
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.status = status
        self.white_list_type = white_list_type
        self.query_product = query_product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.status is not None:
            result['Status'] = self.status
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        if self.query_product is not None:
            result['queryProduct'] = self.query_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        if m.get('queryProduct') is not None:
            self.query_product = m.get('queryProduct')
        return self


class DescribeConsoleAccessWhiteListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        gmt_create: str = None,
        gmt_real_expire: str = None,
        id: int = None,
        ins_product: str = None,
        region_id: str = None,
        src_ip: str = None,
        status: str = None,
    ):
        self.dst_ip = dst_ip
        self.gmt_create = gmt_create
        self.gmt_real_expire = gmt_real_expire
        self.id = id
        self.ins_product = ins_product
        self.region_id = region_id
        self.src_ip = src_ip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_real_expire is not None:
            result['GmtRealExpire'] = self.gmt_real_expire
        if self.id is not None:
            result['Id'] = self.id
        if self.ins_product is not None:
            result['InsProduct'] = self.ins_product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtRealExpire') is not None:
            self.gmt_real_expire = m.get('GmtRealExpire')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsProduct') is not None:
            self.ins_product = m.get('InsProduct')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeConsoleAccessWhiteListResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class DescribeConsoleAccessWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeConsoleAccessWhiteListResponseBodyDataList] = None,
        page_info: DescribeConsoleAccessWhiteListResponseBodyPageInfo = None,
        request_id: str = None,
        module: str = None,
    ):
        self.data_list = data_list
        self.page_info = page_info
        self.request_id = request_id
        self.module = module

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeConsoleAccessWhiteListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeConsoleAccessWhiteListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeConsoleAccessWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConsoleAccessWhiteListResponseBody = None,
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
            temp_model = DescribeConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCountAttackEventRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        product_type: str = None,
        region: str = None,
        server_ip_list: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        self.current_page = current_page
        self.end_time = end_time
        self.lang = lang
        self.page_size = page_size
        self.product_type = product_type
        self.region = region
        self.server_ip_list = server_ip_list
        self.source_ip = source_ip
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.server_ip_list is not None:
            result['ServerIpList'] = self.server_ip_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServerIpList') is not None:
            self.server_ip_list = m.get('ServerIpList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCountAttackEventResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        module: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCountAttackEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCountAttackEventResponseBody = None,
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
            temp_model = DescribeCountAttackEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePhoneInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        phone_num: str = None,
        source_code: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.phone_num = phone_num
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.phone_num is not None:
            result['phoneNum'] = self.phone_num
        if self.source_code is not None:
            result['sourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('phoneNum') is not None:
            self.phone_num = m.get('phoneNum')
        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')
        return self


class DescribePhoneInfoResponseBody(TeaModel):
    def __init__(
        self,
        module: str = None,
        request_id: str = None,
        detect_time: str = None,
        phone_num: int = None,
        risk_level: int = None,
    ):
        self.module = module
        self.request_id = request_id
        self.detect_time = detect_time
        self.phone_num = phone_num
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.detect_time is not None:
            result['detectTime'] = self.detect_time
        if self.phone_num is not None:
            result['phoneNum'] = self.phone_num
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('detectTime') is not None:
            self.detect_time = m.get('detectTime')
        if m.get('phoneNum') is not None:
            self.phone_num = m.get('phoneNum')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        return self


class DescribePhoneInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePhoneInfoResponseBody = None,
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
            temp_model = DescribePhoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


