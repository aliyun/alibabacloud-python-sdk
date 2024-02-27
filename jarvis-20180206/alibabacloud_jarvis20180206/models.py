# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAccessWhiteListGroupRequest(TeaModel):
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


class CreateAccessWhiteListGroupResponseBody(TeaModel):
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


class CreateAccessWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccessWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAllEcsWhiteListRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
    ):
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        return self


class CreateAllEcsWhiteListResponseBody(TeaModel):
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


class CreateAllEcsWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAllEcsWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAllEcsWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnIpRequest(TeaModel):
    def __init__(
        self,
        cdn_ip_list: str = None,
        lang: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.cdn_ip_list = cdn_ip_list
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_ip_list is not None:
            result['CdnIpList'] = self.cdn_ip_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnIpList') is not None:
            self.cdn_ip_list = m.get('CdnIpList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateCdnIpResponseBody(TeaModel):
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


class CreateCdnIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdnIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCdnIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdnSubscriptionRequest(TeaModel):
    def __init__(
        self,
        cdn_uid_list: str = None,
        lang: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.cdn_uid_list = cdn_uid_list
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_uid_list is not None:
            result['CdnUidList'] = self.cdn_uid_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnUidList') is not None:
            self.cdn_uid_list = m.get('CdnUidList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateCdnSubscriptionResponseBody(TeaModel):
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


class CreateCdnSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdnSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCdnSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
        status_code: int = None,
        body: CreateConsoleAccessWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCpmcPunishFeedBackRequest(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: int = None,
        feed_back: int = None,
        gmt_create: str = None,
        lang: str = None,
        protocol_name: str = None,
        punish_type: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        src_port: int = None,
    ):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.feed_back = feed_back
        self.gmt_create = gmt_create
        self.lang = lang
        self.protocol_name = protocol_name
        self.punish_type = punish_type
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.src_port = src_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.feed_back is not None:
            result['FeedBack'] = self.feed_back
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('FeedBack') is not None:
            self.feed_back = m.get('FeedBack')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        return self


class CreateCpmcPunishFeedBackResponseBody(TeaModel):
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


class CreateCpmcPunishFeedBackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCpmcPunishFeedBackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCpmcPunishFeedBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIpWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
    ):
        self.lang = lang
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        return self


class CreateIpWhiteBaselineResponseBody(TeaModel):
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


class CreateIpWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateIpWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateIpWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMiningApplyRequest(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.file_url = file_url
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class CreateMiningApplyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ip: str = None,
        id: int = None,
        module: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.ip = ip
        self.id = id
        self.module = module
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMiningApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMiningApplyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMiningApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMiningReportRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.content = content
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class CreateMiningReportResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ip: str = None,
        id: int = None,
        module: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.ip = ip
        self.id = id
        self.module = module
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMiningReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMiningReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMiningReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMiningRevokeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class CreateMiningRevokeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        ip: str = None,
        id: int = None,
        module: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.ip = ip
        self.id = id
        self.module = module
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.ip is not None:
            result['IP'] = self.ip
        if self.id is not None:
            result['Id'] = self.id
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMiningRevokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMiningRevokeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMiningRevokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUidWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: int = None,
    ):
        self.lang = lang
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        return self


class CreateUidWhiteBaselineResponseBody(TeaModel):
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


class CreateUidWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUidWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUidWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUidWhiteListGroupRequest(TeaModel):
    def __init__(
        self,
        dst_port: int = None,
        instance_id_list: str = None,
        lang: str = None,
        live_time: int = None,
        note: str = None,
        product_name: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: str = None,
        white_list_type: int = None,
    ):
        self.dst_port = dst_port
        self.instance_id_list = instance_id_list
        self.lang = lang
        self.live_time = live_time
        self.note = note
        self.product_name = product_name
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid
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
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
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
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class CreateUidWhiteListGroupResponseBody(TeaModel):
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


class CreateUidWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUidWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUidWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessWhiteListGroupRequest(TeaModel):
    def __init__(
        self,
        group_id_list: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.group_id_list = group_id_list
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
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteAccessWhiteListGroupResponseBody(TeaModel):
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


class DeleteAccessWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnIpRequest(TeaModel):
    def __init__(
        self,
        cdn_ip: str = None,
        item_id: int = None,
        lang: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.cdn_ip = cdn_ip
        self.item_id = item_id
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteCdnIpResponseBody(TeaModel):
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


class DeleteCdnIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCdnIpResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCdnIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCdnSubscriptionRequest(TeaModel):
    def __init__(
        self,
        cdn_uid_list: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.cdn_uid_list = cdn_uid_list
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
        if self.cdn_uid_list is not None:
            result['CdnUidList'] = self.cdn_uid_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnUidList') is not None:
            self.cdn_uid_list = m.get('CdnUidList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteCdnSubscriptionResponseBody(TeaModel):
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


class DeleteCdnSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCdnSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCdnSubscriptionResponseBody()
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
        status_code: int = None,
        body: DeleteConsoleAccessWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCpmcPunishRequest(TeaModel):
    def __init__(
        self,
        ban_path: str = None,
        detect_id: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        end_time: int = None,
        evidence: str = None,
        instance_id: str = None,
        ip_protocol: str = None,
        lang: str = None,
        owner_ali_uid: str = None,
        punish_type: str = None,
        reason: str = None,
        reg_name: str = None,
        region: str = None,
        remark: str = None,
        rule: str = None,
        source_code: str = None,
        source_ip: str = None,
        source_uid: str = None,
        src_ip: str = None,
        src_port: int = None,
        trigger_type: str = None,
        tunnel_id: int = None,
        url: str = None,
    ):
        self.ban_path = ban_path
        self.detect_id = detect_id
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.end_time = end_time
        self.evidence = evidence
        self.instance_id = instance_id
        self.ip_protocol = ip_protocol
        self.lang = lang
        self.owner_ali_uid = owner_ali_uid
        self.punish_type = punish_type
        self.reason = reason
        self.reg_name = reg_name
        self.region = region
        self.remark = remark
        self.rule = rule
        self.source_code = source_code
        self.source_ip = source_ip
        self.source_uid = source_uid
        self.src_ip = src_ip
        self.src_port = src_port
        self.trigger_type = trigger_type
        self.tunnel_id = tunnel_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ban_path is not None:
            result['BanPath'] = self.ban_path
        if self.detect_id is not None:
            result['DetectId'] = self.detect_id
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.evidence is not None:
            result['Evidence'] = self.evidence
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reg_name is not None:
            result['RegName'] = self.reg_name
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.source_uid is not None:
            result['SourceUid'] = self.source_uid
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BanPath') is not None:
            self.ban_path = m.get('BanPath')
        if m.get('DetectId') is not None:
            self.detect_id = m.get('DetectId')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Evidence') is not None:
            self.evidence = m.get('Evidence')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegName') is not None:
            self.reg_name = m.get('RegName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SourceUid') is not None:
            self.source_uid = m.get('SourceUid')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DeleteCpmcPunishResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        module: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCpmcPunishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCpmcPunishResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCpmcPunishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        wbl_ip_list: str = None,
    ):
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.wbl_ip_list = wbl_ip_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.wbl_ip_list is not None:
            result['WblIpList'] = self.wbl_ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WblIpList') is not None:
            self.wbl_ip_list = m.get('WblIpList')
        return self


class DeleteIpWhiteBaselineResponseBody(TeaModel):
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


class DeleteIpWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteIpWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteIpWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUidWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        wbl_uid_list: str = None,
    ):
        self.lang = lang
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.wbl_uid_list = wbl_uid_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.wbl_uid_list is not None:
            result['WblUidList'] = self.wbl_uid_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WblUidList') is not None:
            self.wbl_uid_list = m.get('WblUidList')
        return self


class DeleteUidWhiteBaselineResponseBody(TeaModel):
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


class DeleteUidWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUidWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUidWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUidWhiteListGroupRequest(TeaModel):
    def __init__(
        self,
        group_id_list: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.group_id_list = group_id_list
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
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteUidWhiteListGroupResponseBody(TeaModel):
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


class DeleteUidWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUidWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUidWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhiteListConditionalRequest(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        query_product: str = None,
    ):
        self.dst_ip = dst_ip
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.query_product = query_product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.query_product is not None:
            result['queryProduct'] = self.query_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('queryProduct') is not None:
            self.query_product = m.get('queryProduct')
        return self


class DeleteWhiteListConditionalResponseBody(TeaModel):
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


class DeleteWhiteListConditionalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWhiteListConditionalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWhiteListConditionalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWhiteListDbItemConditionalRequest(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        query_product: str = None,
    ):
        self.dst_ip = dst_ip
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.query_product = query_product

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.query_product is not None:
            result['queryProduct'] = self.query_product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('queryProduct') is not None:
            self.query_product = m.get('queryProduct')
        return self


class DeleteWhiteListDbItemConditionalResponseBody(TeaModel):
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


class DeleteWhiteListDbItemConditionalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWhiteListDbItemConditionalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWhiteListDbItemConditionalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhiteListEipListRequest(TeaModel):
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


class DescribeAccessWhiteListEipListResponseBodyEipList(TeaModel):
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


class DescribeAccessWhiteListEipListResponseBody(TeaModel):
    def __init__(
        self,
        eip_list: List[DescribeAccessWhiteListEipListResponseBodyEipList] = None,
        request_id: str = None,
        total_count: int = None,
        module: str = None,
    ):
        self.eip_list = eip_list
        self.request_id = request_id
        self.total_count = total_count
        self.module = module

    def validate(self):
        if self.eip_list:
            for k in self.eip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipList'] = []
        if self.eip_list is not None:
            for k in self.eip_list:
                result['EipList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_list = []
        if m.get('EipList') is not None:
            for k in m.get('EipList'):
                temp_model = DescribeAccessWhiteListEipListResponseBodyEipList()
                self.eip_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhiteListEipListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessWhiteListEipListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhiteListEipListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhiteListGroupRequest(TeaModel):
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


class DescribeAccessWhiteListGroupResponseBodyDataListItems(TeaModel):
    def __init__(
        self,
        ip: str = None,
        region_id: str = None,
    ):
        self.ip = ip
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAccessWhiteListGroupResponseBodyDataList(TeaModel):
    def __init__(
        self,
        auto_config: int = None,
        gmt_create: str = None,
        gmt_real_expire: str = None,
        group_id: int = None,
        ins_product: str = None,
        items: List[DescribeAccessWhiteListGroupResponseBodyDataListItems] = None,
        src_ip: str = None,
        status: str = None,
    ):
        self.auto_config = auto_config
        self.gmt_create = gmt_create
        self.gmt_real_expire = gmt_real_expire
        self.group_id = group_id
        self.ins_product = ins_product
        self.items = items
        self.src_ip = src_ip
        self.status = status

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_real_expire is not None:
            result['GmtRealExpire'] = self.gmt_real_expire
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ins_product is not None:
            result['InsProduct'] = self.ins_product
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtRealExpire') is not None:
            self.gmt_real_expire = m.get('GmtRealExpire')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InsProduct') is not None:
            self.ins_product = m.get('InsProduct')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeAccessWhiteListGroupResponseBodyDataListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeAccessWhiteListGroupResponseBodyPageInfo(TeaModel):
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


class DescribeAccessWhiteListGroupResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeAccessWhiteListGroupResponseBodyDataList] = None,
        page_info: DescribeAccessWhiteListGroupResponseBodyPageInfo = None,
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
                temp_model = DescribeAccessWhiteListGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeAccessWhiteListGroupResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhiteListRdsListRequest(TeaModel):
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


class DescribeAccessWhiteListRdsListResponseBodyRdsList(TeaModel):
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


class DescribeAccessWhiteListRdsListResponseBody(TeaModel):
    def __init__(
        self,
        rds_list: List[DescribeAccessWhiteListRdsListResponseBodyRdsList] = None,
        request_id: str = None,
        total_count: int = None,
        module: str = None,
    ):
        self.rds_list = rds_list
        self.request_id = request_id
        self.total_count = total_count
        self.module = module

    def validate(self):
        if self.rds_list:
            for k in self.rds_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RdsList'] = []
        if self.rds_list is not None:
            for k in self.rds_list:
                result['RdsList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rds_list = []
        if m.get('RdsList') is not None:
            for k in m.get('RdsList'):
                temp_model = DescribeAccessWhiteListRdsListResponseBodyRdsList()
                self.rds_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhiteListRdsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessWhiteListRdsListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhiteListRdsListResponseBody()
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
        status_code: int = None,
        body: DescribeAccessWhiteListSlbListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhiteListSlbListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccessWhiteListSwasListRequest(TeaModel):
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


class DescribeAccessWhiteListSwasListResponseBodySwasList(TeaModel):
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


class DescribeAccessWhiteListSwasListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        swas_list: List[DescribeAccessWhiteListSwasListResponseBodySwasList] = None,
        total_count: int = None,
        module: str = None,
    ):
        self.request_id = request_id
        self.swas_list = swas_list
        self.total_count = total_count
        self.module = module

    def validate(self):
        if self.swas_list:
            for k in self.swas_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SwasList'] = []
        if self.swas_list is not None:
            for k in self.swas_list:
                result['SwasList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.swas_list = []
        if m.get('SwasList') is not None:
            for k in m.get('SwasList'):
                temp_model = DescribeAccessWhiteListSwasListResponseBodySwasList()
                self.swas_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeAccessWhiteListSwasListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAccessWhiteListSwasListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhiteListSwasListResponseBody()
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
        status_code: int = None,
        body: DescribeAccessWhitelistEcsListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAccessWhitelistEcsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnCertifyRequest(TeaModel):
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


class DescribeCdnCertifyResponseBody(TeaModel):
    def __init__(
        self,
        is_cdn_vendor: bool = None,
        module: str = None,
        request_id: str = None,
    ):
        self.is_cdn_vendor = is_cdn_vendor
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_cdn_vendor is not None:
            result['IsCdnVendor'] = self.is_cdn_vendor
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsCdnVendor') is not None:
            self.is_cdn_vendor = m.get('IsCdnVendor')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnCertifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnCertifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnCertifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnIpListRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        wl_state: int = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.wl_state = wl_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        if self.wl_state is not None:
            result['WlState'] = self.wl_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
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
        if m.get('WlState') is not None:
            self.wl_state = m.get('WlState')
        return self


class DescribeCdnIpListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: int = None,
        ip_seg: str = None,
        state: int = None,
        update_time: str = None,
        vendor_aliuid: int = None,
    ):
        self.create_time = create_time
        self.id = id
        self.ip_seg = ip_seg
        self.state = state
        self.update_time = update_time
        self.vendor_aliuid = vendor_aliuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ip_seg is not None:
            result['IpSeg'] = self.ip_seg
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_aliuid is not None:
            result['VendorAliuid'] = self.vendor_aliuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IpSeg') is not None:
            self.ip_seg = m.get('IpSeg')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorAliuid') is not None:
            self.vendor_aliuid = m.get('VendorAliuid')
        return self


class DescribeCdnIpListResponseBodyPageInfo(TeaModel):
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


class DescribeCdnIpListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeCdnIpListResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeCdnIpListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeCdnIpListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeCdnIpListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnIpListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnSubscriptionRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
        subscription_state: int = None,
        vendor_name: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip
        self.subscription_state = subscription_state
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.subscription_state is not None:
            result['SubscriptionState'] = self.subscription_state
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SubscriptionState') is not None:
            self.subscription_state = m.get('SubscriptionState')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class DescribeCdnSubscriptionResponseBodyDataList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        safety_factor: str = None,
        subscription_state: int = None,
        update_time: str = None,
        vendor_aliuid: int = None,
        vendor_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.safety_factor = safety_factor
        self.subscription_state = subscription_state
        self.update_time = update_time
        self.vendor_aliuid = vendor_aliuid
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.safety_factor is not None:
            result['SafetyFactor'] = self.safety_factor
        if self.subscription_state is not None:
            result['SubscriptionState'] = self.subscription_state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_aliuid is not None:
            result['VendorAliuid'] = self.vendor_aliuid
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SafetyFactor') is not None:
            self.safety_factor = m.get('SafetyFactor')
        if m.get('SubscriptionState') is not None:
            self.subscription_state = m.get('SubscriptionState')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorAliuid') is not None:
            self.vendor_aliuid = m.get('VendorAliuid')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class DescribeCdnSubscriptionResponseBodyPageInfo(TeaModel):
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


class DescribeCdnSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeCdnSubscriptionResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeCdnSubscriptionResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeCdnSubscriptionResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeCdnSubscriptionResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCdnVendorRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeCdnVendorResponseBodyDataList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        safety_factor: str = None,
        update_time: str = None,
        vendor_aliuid: int = None,
        vendor_name: str = None,
    ):
        self.gmt_create = gmt_create
        self.safety_factor = safety_factor
        self.update_time = update_time
        self.vendor_aliuid = vendor_aliuid
        self.vendor_name = vendor_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.safety_factor is not None:
            result['SafetyFactor'] = self.safety_factor
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor_aliuid is not None:
            result['VendorAliuid'] = self.vendor_aliuid
        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SafetyFactor') is not None:
            self.safety_factor = m.get('SafetyFactor')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VendorAliuid') is not None:
            self.vendor_aliuid = m.get('VendorAliuid')
        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')
        return self


class DescribeCdnVendorResponseBodyPageInfo(TeaModel):
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


class DescribeCdnVendorResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeCdnVendorResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeCdnVendorResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeCdnVendorResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeCdnVendorResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCdnVendorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCdnVendorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCdnVendorResponseBody()
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
        status_code: int = None,
        body: DescribeConsoleAccessWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeConsoleAccessWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCpmcPunishListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        punish_status: str = None,
        punish_type: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.punish_status = punish_status
        self.punish_type = punish_type
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class DescribeCpmcPunishListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        description: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        feed_back: int = None,
        gmt_create: str = None,
        gmt_expire: str = None,
        instance_id: str = None,
        protocol: str = None,
        punish_result: str = None,
        punish_type: str = None,
        reason: str = None,
        region_id: str = None,
        src_ip: str = None,
        src_port: int = None,
    ):
        self.description = description
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.feed_back = feed_back
        self.gmt_create = gmt_create
        self.gmt_expire = gmt_expire
        self.instance_id = instance_id
        self.protocol = protocol
        self.punish_result = punish_result
        self.punish_type = punish_type
        self.reason = reason
        self.region_id = region_id
        self.src_ip = src_ip
        self.src_port = src_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.feed_back is not None:
            result['FeedBack'] = self.feed_back
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('FeedBack') is not None:
            self.feed_back = m.get('FeedBack')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        return self


class DescribeCpmcPunishListResponseBodyPageInfo(TeaModel):
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


class DescribeCpmcPunishListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeCpmcPunishListResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeCpmcPunishListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeCpmcPunishListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeCpmcPunishListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCpmcPunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCpmcPunishListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeCpmcPunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosDefenseInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        source_code: str = None,
        src_uid: int = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.source_code = source_code
        self.src_uid = src_uid

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
        if self.source_code is not None:
            result['sourceCode'] = self.source_code
        if self.src_uid is not None:
            result['srcUid'] = self.src_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')
        if m.get('srcUid') is not None:
            self.src_uid = m.get('srcUid')
        return self


class DescribeDdosDefenseInfoResponseBodyDdosDefenseThreshold(TeaModel):
    def __init__(
        self,
        curr_threshold: int = None,
        recommend_threshold: int = None,
        region_id: str = None,
    ):
        self.curr_threshold = curr_threshold
        self.recommend_threshold = recommend_threshold
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_threshold is not None:
            result['CurrThreshold'] = self.curr_threshold
        if self.recommend_threshold is not None:
            result['RecommendThreshold'] = self.recommend_threshold
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrThreshold') is not None:
            self.curr_threshold = m.get('CurrThreshold')
        if m.get('RecommendThreshold') is not None:
            self.recommend_threshold = m.get('RecommendThreshold')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDdosDefenseInfoResponseBody(TeaModel):
    def __init__(
        self,
        bgp_pkg_state: str = None,
        black_times: int = None,
        ddos_defense_threshold: List[DescribeDdosDefenseInfoResponseBodyDdosDefenseThreshold] = None,
        duration: int = None,
        module: str = None,
        request_id: str = None,
    ):
        self.bgp_pkg_state = bgp_pkg_state
        self.black_times = black_times
        self.ddos_defense_threshold = ddos_defense_threshold
        self.duration = duration
        self.module = module
        self.request_id = request_id

    def validate(self):
        if self.ddos_defense_threshold:
            for k in self.ddos_defense_threshold:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bgp_pkg_state is not None:
            result['BgpPkgState'] = self.bgp_pkg_state
        if self.black_times is not None:
            result['BlackTimes'] = self.black_times
        result['DdosDefenseThreshold'] = []
        if self.ddos_defense_threshold is not None:
            for k in self.ddos_defense_threshold:
                result['DdosDefenseThreshold'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgpPkgState') is not None:
            self.bgp_pkg_state = m.get('BgpPkgState')
        if m.get('BlackTimes') is not None:
            self.black_times = m.get('BlackTimes')
        self.ddos_defense_threshold = []
        if m.get('DdosDefenseThreshold') is not None:
            for k in m.get('DdosDefenseThreshold'):
                temp_model = DescribeDdosDefenseInfoResponseBodyDdosDefenseThreshold()
                self.ddos_defense_threshold.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDdosDefenseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDdosDefenseInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDdosDefenseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEcsListPageRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeEcsListPageResponseBodyDataList(TeaModel):
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


class DescribeEcsListPageResponseBodyPageInfo(TeaModel):
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


class DescribeEcsListPageResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeEcsListPageResponseBodyDataList] = None,
        page_info: DescribeEcsListPageResponseBodyPageInfo = None,
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
                temp_model = DescribeEcsListPageResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeEcsListPageResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeEcsListPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEcsListPageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEcsListPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        status: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.remark = remark
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeIpWhiteBaselineResponseBodyDataList(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        id: int = None,
        owner_ali_uid: int = None,
        real_end_time: int = None,
        remark: str = None,
        src_ip: int = None,
        status: str = None,
    ):
        self.begin_time = begin_time
        self.id = id
        self.owner_ali_uid = owner_ali_uid
        self.real_end_time = real_end_time
        self.remark = remark
        self.src_ip = src_ip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        if self.real_end_time is not None:
            result['RealEndTime'] = self.real_end_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        if m.get('RealEndTime') is not None:
            self.real_end_time = m.get('RealEndTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeIpWhiteBaselineResponseBodyPageInfo(TeaModel):
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


class DescribeIpWhiteBaselineResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeIpWhiteBaselineResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeIpWhiteBaselineResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeIpWhiteBaselineResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeIpWhiteBaselineResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeIpWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMiningPreApplyRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: str = None,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.file_name = file_name
        self.file_type = file_type
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class DescribeMiningPreApplyResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        code: int = None,
        host: str = None,
        key: str = None,
        module: str = None,
        msg: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        sts_token: str = None,
    ):
        self.access_id = access_id
        self.code = code
        self.host = host
        self.key = key
        self.module = module
        self.msg = msg
        self.policy = policy
        self.request_id = request_id
        self.signature = signature
        self.sts_token = sts_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.code is not None:
            result['Code'] = self.code
        if self.host is not None:
            result['Host'] = self.host
        if self.key is not None:
            result['Key'] = self.key
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.sts_token is not None:
            result['StsToken'] = self.sts_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StsToken') is not None:
            self.sts_token = m.get('StsToken')
        return self


class DescribeMiningPreApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMiningPreApplyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMiningPreApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMiningRecordsRequest(TeaModel):
    def __init__(
        self,
        ip: str = None,
        page_number: int = None,
        page_size: int = None,
        source_code: str = None,
        status: str = None,
    ):
        self.ip = ip
        self.page_number = page_number
        self.page_size = page_size
        self.source_code = source_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMiningRecordsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_type: str = None,
        aliuid: str = None,
        aliuid_consistent: str = None,
        authority: str = None,
        binding_time: str = None,
        contact: str = None,
        feedback_data: str = None,
        feedback_deadline: str = None,
        gclevel: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        ip: str = None,
        location: str = None,
        mining_time: str = None,
        ops_oss_url: str = None,
        ops_remark: str = None,
        ops_status: str = None,
        ops_time: str = None,
        owner: str = None,
        product: str = None,
        unbinding_time: str = None,
    ):
        self.account_type = account_type
        self.aliuid = aliuid
        self.aliuid_consistent = aliuid_consistent
        self.authority = authority
        self.binding_time = binding_time
        self.contact = contact
        self.feedback_data = feedback_data
        self.feedback_deadline = feedback_deadline
        self.gclevel = gclevel
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.ip = ip
        self.location = location
        self.mining_time = mining_time
        self.ops_oss_url = ops_oss_url
        self.ops_remark = ops_remark
        self.ops_status = ops_status
        self.ops_time = ops_time
        self.owner = owner
        self.product = product
        self.unbinding_time = unbinding_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.aliuid_consistent is not None:
            result['AliuidConsistent'] = self.aliuid_consistent
        if self.authority is not None:
            result['Authority'] = self.authority
        if self.binding_time is not None:
            result['BindingTime'] = self.binding_time
        if self.contact is not None:
            result['Contact'] = self.contact
        if self.feedback_data is not None:
            result['FeedbackData'] = self.feedback_data
        if self.feedback_deadline is not None:
            result['FeedbackDeadline'] = self.feedback_deadline
        if self.gclevel is not None:
            result['GCLevel'] = self.gclevel
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.location is not None:
            result['Location'] = self.location
        if self.mining_time is not None:
            result['MiningTime'] = self.mining_time
        if self.ops_oss_url is not None:
            result['OpsOssUrl'] = self.ops_oss_url
        if self.ops_remark is not None:
            result['OpsRemark'] = self.ops_remark
        if self.ops_status is not None:
            result['OpsStatus'] = self.ops_status
        if self.ops_time is not None:
            result['OpsTime'] = self.ops_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.product is not None:
            result['Product'] = self.product
        if self.unbinding_time is not None:
            result['UnbindingTime'] = self.unbinding_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('AliuidConsistent') is not None:
            self.aliuid_consistent = m.get('AliuidConsistent')
        if m.get('Authority') is not None:
            self.authority = m.get('Authority')
        if m.get('BindingTime') is not None:
            self.binding_time = m.get('BindingTime')
        if m.get('Contact') is not None:
            self.contact = m.get('Contact')
        if m.get('FeedbackData') is not None:
            self.feedback_data = m.get('FeedbackData')
        if m.get('FeedbackDeadline') is not None:
            self.feedback_deadline = m.get('FeedbackDeadline')
        if m.get('GCLevel') is not None:
            self.gclevel = m.get('GCLevel')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('MiningTime') is not None:
            self.mining_time = m.get('MiningTime')
        if m.get('OpsOssUrl') is not None:
            self.ops_oss_url = m.get('OpsOssUrl')
        if m.get('OpsRemark') is not None:
            self.ops_remark = m.get('OpsRemark')
        if m.get('OpsStatus') is not None:
            self.ops_status = m.get('OpsStatus')
        if m.get('OpsTime') is not None:
            self.ops_time = m.get('OpsTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('UnbindingTime') is not None:
            self.unbinding_time = m.get('UnbindingTime')
        return self


class DescribeMiningRecordsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data_list: List[DescribeMiningRecordsResponseBodyDataList] = None,
        module: str = None,
        msg: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.module = module
        self.msg = msg
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeMiningRecordsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMiningRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMiningRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMiningRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMiningRejectedReasonRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class DescribeMiningRejectedReasonResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        module: str = None,
        msg: str = None,
        reason: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.module = module
        self.msg = msg
        self.reason = reason
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMiningRejectedReasonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMiningRejectedReasonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMiningRejectedReasonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMiningReportContentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class DescribeMiningReportContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        module: str = None,
        msg: str = None,
        oss_url: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.module = module
        self.msg = msg
        self.oss_url = oss_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMiningReportContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMiningReportContentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMiningReportContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMiningReportFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        source_code: str = None,
    ):
        self.id = id
        self.ip = ip
        self.source_code = source_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        return self


class DescribeMiningReportFileResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        module: str = None,
        msg: str = None,
        oss_url: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.module = module
        self.msg = msg
        self.oss_url = oss_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.module is not None:
            result['Module'] = self.module
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMiningReportFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMiningReportFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMiningReportFileResponseBody()
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
        status_code: int = None,
        body: DescribePhoneInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePhoneInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePunishListRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        punish_status: str = None,
        source_ip: str = None,
        src_ip: str = None,
        current_page: int = None,
        page_size: int = None,
        source_code: str = None,
        src_uid: int = None,
    ):
        self.lang = lang
        self.punish_status = punish_status
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.current_page = current_page
        self.page_size = page_size
        self.source_code = source_code
        self.src_uid = src_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.source_code is not None:
            result['sourceCode'] = self.source_code
        if self.src_uid is not None:
            result['srcUid'] = self.src_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')
        if m.get('srcUid') is not None:
            self.src_uid = m.get('srcUid')
        return self


class DescribePunishListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: int = None,
        feed_back: int = None,
        gmt_create: str = None,
        gmt_expire: str = None,
        protocol: str = None,
        punish_result: str = None,
        punish_type: str = None,
        reason: str = None,
        region_id: str = None,
        src_ip: str = None,
        src_port: int = None,
    ):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.feed_back = feed_back
        self.gmt_create = gmt_create
        self.gmt_expire = gmt_expire
        self.protocol = protocol
        self.punish_result = punish_result
        self.punish_type = punish_type
        self.reason = reason
        self.region_id = region_id
        self.src_ip = src_ip
        self.src_port = src_port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.feed_back is not None:
            result['FeedBack'] = self.feed_back
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.src_port is not None:
            result['SrcPort'] = self.src_port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('FeedBack') is not None:
            self.feed_back = m.get('FeedBack')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')
        return self


class DescribePunishListResponseBodyPageInfo(TeaModel):
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


class DescribePunishListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribePunishListResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribePunishListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribePunishListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribePunishListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribePunishListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePunishListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePunishListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResetRecordListRequest(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        lang: str = None,
        period: str = None,
        region: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.dst_ip = dst_ip
        self.lang = lang
        self.period = period
        self.region = region
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class DescribeResetRecordListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_port: int = None,
        punish_count: int = None,
        punish_result: str = None,
        punish_type: str = None,
        src_ip: str = None,
    ):
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.punish_count = punish_count
        self.punish_result = punish_result
        self.punish_type = punish_type
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.punish_count is not None:
            result['PunishCount'] = self.punish_count
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        if self.punish_type is not None:
            result['PunishType'] = self.punish_type
        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('PunishCount') is not None:
            self.punish_count = m.get('PunishCount')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        if m.get('PunishType') is not None:
            self.punish_type = m.get('PunishType')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        return self


class DescribeResetRecordListResponseBodyPageInfo(TeaModel):
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


class DescribeResetRecordListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeResetRecordListResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeResetRecordListResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeResetRecordListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeResetRecordListResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResetRecordListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResetRecordListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResetRecordListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResetRecordQueryCountRequest(TeaModel):
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


class DescribeResetRecordQueryCountResponseBody(TeaModel):
    def __init__(
        self,
        module: str = None,
        query_count: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.module = module
        self.query_count = query_count
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['Module'] = self.module
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeResetRecordQueryCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResetRecordQueryCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResetRecordQueryCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskListDetailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        current_page: int = None,
        page_size: int = None,
        query_product: str = None,
        query_region_id: str = None,
        risk_describe: str = None,
        risk_type: str = None,
        source_code: str = None,
        src_uid: int = None,
        status: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.current_page = current_page
        self.page_size = page_size
        self.query_product = query_product
        self.query_region_id = query_region_id
        self.risk_describe = risk_describe
        self.risk_type = risk_type
        self.source_code = source_code
        self.src_uid = src_uid
        self.status = status

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
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query_product is not None:
            result['queryProduct'] = self.query_product
        if self.query_region_id is not None:
            result['queryRegionId'] = self.query_region_id
        if self.risk_describe is not None:
            result['riskDescribe'] = self.risk_describe
        if self.risk_type is not None:
            result['riskType'] = self.risk_type
        if self.source_code is not None:
            result['sourceCode'] = self.source_code
        if self.src_uid is not None:
            result['srcUid'] = self.src_uid
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('queryProduct') is not None:
            self.query_product = m.get('queryProduct')
        if m.get('queryRegionId') is not None:
            self.query_region_id = m.get('queryRegionId')
        if m.get('riskDescribe') is not None:
            self.risk_describe = m.get('riskDescribe')
        if m.get('riskType') is not None:
            self.risk_type = m.get('riskType')
        if m.get('sourceCode') is not None:
            self.source_code = m.get('sourceCode')
        if m.get('srcUid') is not None:
            self.src_uid = m.get('srcUid')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeRiskListDetailResponseBodyDataListEcsSecGroupRisk(TeaModel):
    def __init__(
        self,
        direction: str = None,
        dst_port_range: str = None,
        net_type: str = None,
        src_ip_range: str = None,
    ):
        self.direction = direction
        self.dst_port_range = dst_port_range
        self.net_type = net_type
        self.src_ip_range = src_ip_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.src_ip_range is not None:
            result['SrcIpRange'] = self.src_ip_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('SrcIpRange') is not None:
            self.src_ip_range = m.get('SrcIpRange')
        return self


class DescribeRiskListDetailResponseBodyDataListRdsWhitelistRisk(TeaModel):
    def __init__(
        self,
        rds_whitelist_group: str = None,
        risk_detail: str = None,
    ):
        self.rds_whitelist_group = rds_whitelist_group
        self.risk_detail = risk_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rds_whitelist_group is not None:
            result['RdsWhitelistGroup'] = self.rds_whitelist_group
        if self.risk_detail is not None:
            result['RiskDetail'] = self.risk_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RdsWhitelistGroup') is not None:
            self.rds_whitelist_group = m.get('RdsWhitelistGroup')
        if m.get('RiskDetail') is not None:
            self.risk_detail = m.get('RiskDetail')
        return self


class DescribeRiskListDetailResponseBodyDataList(TeaModel):
    def __init__(
        self,
        ecs_sec_group_risk: List[DescribeRiskListDetailResponseBodyDataListEcsSecGroupRisk] = None,
        ignore_time: str = None,
        instance_list: List[str] = None,
        product: str = None,
        rds_whitelist_risk: List[DescribeRiskListDetailResponseBodyDataListRdsWhitelistRisk] = None,
        region_id: str = None,
        risk_describe: str = None,
        risk_id: int = None,
        risk_instance: str = None,
        risk_type: str = None,
        status: str = None,
        tactics_name: str = None,
        update_time: str = None,
    ):
        self.ecs_sec_group_risk = ecs_sec_group_risk
        self.ignore_time = ignore_time
        self.instance_list = instance_list
        self.product = product
        self.rds_whitelist_risk = rds_whitelist_risk
        self.region_id = region_id
        self.risk_describe = risk_describe
        self.risk_id = risk_id
        self.risk_instance = risk_instance
        self.risk_type = risk_type
        self.status = status
        self.tactics_name = tactics_name
        self.update_time = update_time

    def validate(self):
        if self.ecs_sec_group_risk:
            for k in self.ecs_sec_group_risk:
                if k:
                    k.validate()
        if self.rds_whitelist_risk:
            for k in self.rds_whitelist_risk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsSecGroupRisk'] = []
        if self.ecs_sec_group_risk is not None:
            for k in self.ecs_sec_group_risk:
                result['EcsSecGroupRisk'].append(k.to_map() if k else None)
        if self.ignore_time is not None:
            result['IgnoreTime'] = self.ignore_time
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.product is not None:
            result['Product'] = self.product
        result['RdsWhitelistRisk'] = []
        if self.rds_whitelist_risk is not None:
            for k in self.rds_whitelist_risk:
                result['RdsWhitelistRisk'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.risk_describe is not None:
            result['RiskDescribe'] = self.risk_describe
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id
        if self.risk_instance is not None:
            result['RiskInstance'] = self.risk_instance
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        if self.status is not None:
            result['Status'] = self.status
        if self.tactics_name is not None:
            result['TacticsName'] = self.tactics_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_sec_group_risk = []
        if m.get('EcsSecGroupRisk') is not None:
            for k in m.get('EcsSecGroupRisk'):
                temp_model = DescribeRiskListDetailResponseBodyDataListEcsSecGroupRisk()
                self.ecs_sec_group_risk.append(temp_model.from_map(k))
        if m.get('IgnoreTime') is not None:
            self.ignore_time = m.get('IgnoreTime')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        self.rds_whitelist_risk = []
        if m.get('RdsWhitelistRisk') is not None:
            for k in m.get('RdsWhitelistRisk'):
                temp_model = DescribeRiskListDetailResponseBodyDataListRdsWhitelistRisk()
                self.rds_whitelist_risk.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RiskDescribe') is not None:
            self.risk_describe = m.get('RiskDescribe')
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')
        if m.get('RiskInstance') is not None:
            self.risk_instance = m.get('RiskInstance')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TacticsName') is not None:
            self.tactics_name = m.get('TacticsName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeRiskListDetailResponseBodyPageInfo(TeaModel):
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


class DescribeRiskListDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeRiskListDetailResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeRiskListDetailResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeRiskListDetailResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeRiskListDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRiskListDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRiskListDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRiskListDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRiskTrendRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        peroid: str = None,
        query_product: str = None,
        query_region_id: str = None,
        source_code: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.peroid = peroid
        self.query_product = query_product
        self.query_region_id = query_region_id
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
        if self.peroid is not None:
            result['Peroid'] = self.peroid
        if self.query_product is not None:
            result['QueryProduct'] = self.query_product
        if self.query_region_id is not None:
            result['QueryRegionId'] = self.query_region_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Peroid') is not None:
            self.peroid = m.get('Peroid')
        if m.get('QueryProduct') is not None:
            self.query_product = m.get('QueryProduct')
        if m.get('QueryRegionId') is not None:
            self.query_region_id = m.get('QueryRegionId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeRiskTrendResponseBodyDataList(TeaModel):
    def __init__(
        self,
        new_risk_count: int = None,
        total_risk_count: int = None,
        update_time: str = None,
    ):
        self.new_risk_count = new_risk_count
        self.total_risk_count = total_risk_count
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_risk_count is not None:
            result['NewRiskCount'] = self.new_risk_count
        if self.total_risk_count is not None:
            result['TotalRiskCount'] = self.total_risk_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewRiskCount') is not None:
            self.new_risk_count = m.get('NewRiskCount')
        if m.get('TotalRiskCount') is not None:
            self.total_risk_count = m.get('TotalRiskCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeRiskTrendResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeRiskTrendResponseBodyDataList] = None,
        module: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeRiskTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRiskTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRiskTrendResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRiskTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpecialEcsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_code: str = None,
        source_ip: str = None,
        target_ip: str = None,
    ):
        self.lang = lang
        self.source_code = source_code
        self.source_ip = source_ip
        self.target_ip = target_ip

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
        if self.target_ip is not None:
            result['TargetIp'] = self.target_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TargetIp') is not None:
            self.target_ip = m.get('TargetIp')
        return self


class DescribeSpecialEcsResponseBodyEcsInfo(TeaModel):
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


class DescribeSpecialEcsResponseBody(TeaModel):
    def __init__(
        self,
        ecs_found: bool = None,
        ecs_info: DescribeSpecialEcsResponseBodyEcsInfo = None,
        request_id: str = None,
        module: str = None,
    ):
        self.ecs_found = ecs_found
        self.ecs_info = ecs_info
        self.request_id = request_id
        self.module = module

    def validate(self):
        if self.ecs_info:
            self.ecs_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ecs_found is not None:
            result['EcsFound'] = self.ecs_found
        if self.ecs_info is not None:
            result['EcsInfo'] = self.ecs_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module is not None:
            result['module'] = self.module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsFound') is not None:
            self.ecs_found = m.get('EcsFound')
        if m.get('EcsInfo') is not None:
            temp_model = DescribeSpecialEcsResponseBodyEcsInfo()
            self.ecs_info = temp_model.from_map(m['EcsInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeSpecialEcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpecialEcsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSpecialEcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUidGcLevelRequest(TeaModel):
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


class DescribeUidGcLevelResponseBody(TeaModel):
    def __init__(
        self,
        gclevel: str = None,
        module: str = None,
        request_id: str = None,
    ):
        self.gclevel = gclevel
        self.module = module
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gclevel is not None:
            result['Gclevel'] = self.gclevel
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gclevel') is not None:
            self.gclevel = m.get('Gclevel')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUidGcLevelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUidGcLevelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUidGcLevelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUidWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: int = None,
        status: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.remark = remark
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUidWhiteBaselineResponseBodyDataList(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        id: int = None,
        owner_ali_uid: int = None,
        real_end_time: int = None,
        remark: str = None,
        src_uid: int = None,
        status: str = None,
    ):
        self.begin_time = begin_time
        self.id = id
        self.owner_ali_uid = owner_ali_uid
        self.real_end_time = real_end_time
        self.remark = remark
        self.src_uid = src_uid
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        if self.real_end_time is not None:
            result['RealEndTime'] = self.real_end_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        if m.get('RealEndTime') is not None:
            self.real_end_time = m.get('RealEndTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUidWhiteBaselineResponseBodyPageInfo(TeaModel):
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


class DescribeUidWhiteBaselineResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeUidWhiteBaselineResponseBodyDataList] = None,
        module: str = None,
        page_info: DescribeUidWhiteBaselineResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.module = module
        self.page_info = page_info
        self.request_id = request_id

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
        if self.module is not None:
            result['Module'] = self.module
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeUidWhiteBaselineResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('PageInfo') is not None:
            temp_model = DescribeUidWhiteBaselineResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUidWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUidWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUidWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUidWhiteListGroupRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        dst_ip: str = None,
        lang: str = None,
        page_size: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: str = None,
        status: str = None,
        white_list_type: int = None,
    ):
        self.current_page = current_page
        self.dst_ip = dst_ip
        self.lang = lang
        self.page_size = page_size
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid
        self.status = status
        self.white_list_type = white_list_type

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
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.status is not None:
            result['Status'] = self.status
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
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
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class DescribeUidWhiteListGroupResponseBodyDataListItems(TeaModel):
    def __init__(
        self,
        ip: str = None,
        region_id: str = None,
    ):
        self.ip = ip
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeUidWhiteListGroupResponseBodyDataList(TeaModel):
    def __init__(
        self,
        auto_config: int = None,
        gmt_create: str = None,
        gmt_real_expire: str = None,
        group_id: int = None,
        items: List[DescribeUidWhiteListGroupResponseBodyDataListItems] = None,
        src_uid: str = None,
        status: str = None,
    ):
        self.auto_config = auto_config
        self.gmt_create = gmt_create
        self.gmt_real_expire = gmt_real_expire
        self.group_id = group_id
        self.items = items
        self.src_uid = src_uid
        self.status = status

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_real_expire is not None:
            result['GmtRealExpire'] = self.gmt_real_expire
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtRealExpire') is not None:
            self.gmt_real_expire = m.get('GmtRealExpire')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeUidWhiteListGroupResponseBodyDataListItems()
                self.items.append(temp_model.from_map(k))
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeUidWhiteListGroupResponseBodyPageInfo(TeaModel):
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


class DescribeUidWhiteListGroupResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeUidWhiteListGroupResponseBodyDataList] = None,
        page_info: DescribeUidWhiteListGroupResponseBodyPageInfo = None,
        product_list: List[str] = None,
        request_id: str = None,
        module: str = None,
    ):
        self.data_list = data_list
        self.page_info = page_info
        self.product_list = product_list
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
        if self.product_list is not None:
            result['ProductList'] = self.product_list
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
                temp_model = DescribeUidWhiteListGroupResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = DescribeUidWhiteListGroupResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('ProductList') is not None:
            self.product_list = m.get('ProductList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('module') is not None:
            self.module = m.get('module')
        return self


class DescribeUidWhiteListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUidWhiteListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUidWhiteListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessWhiteListAutoShareRequest(TeaModel):
    def __init__(
        self,
        auto_config: int = None,
        lang: str = None,
        product_name: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        white_list_type: int = None,
    ):
        self.auto_config = auto_config
        self.lang = lang
        self.product_name = product_name
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
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_name is not None:
            result['ProductName'] = self.product_name
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
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class ModifyAccessWhiteListAutoShareResponseBody(TeaModel):
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


class ModifyAccessWhiteListAutoShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAccessWhiteListAutoShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessWhiteListAutoShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
    ):
        self.id = id
        self.lang = lang
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')
        return self


class ModifyIpWhiteBaselineResponseBody(TeaModel):
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


class ModifyIpWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyIpWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyIpWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUidWhiteBaselineRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: int = None,
    ):
        self.id = id
        self.lang = lang
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        return self


class ModifyUidWhiteBaselineResponseBody(TeaModel):
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


class ModifyUidWhiteBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUidWhiteBaselineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUidWhiteBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUidWhiteListAutoShareRequest(TeaModel):
    def __init__(
        self,
        auto_config: int = None,
        lang: str = None,
        product_name: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_uid: str = None,
        white_list_type: int = None,
    ):
        self.auto_config = auto_config
        self.lang = lang
        self.product_name = product_name
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_uid = src_uid
        self.white_list_type = white_list_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.src_uid is not None:
            result['SrcUid'] = self.src_uid
        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SrcUid') is not None:
            self.src_uid = m.get('SrcUid')
        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')
        return self


class ModifyUidWhiteListAutoShareResponseBody(TeaModel):
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


class ModifyUidWhiteListAutoShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyUidWhiteListAutoShareResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyUidWhiteListAutoShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


