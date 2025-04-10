# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        act: str = None,
        count: int = None,
        domain: str = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        resource_group_id: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.act = act
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.interval = interval
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.name = name
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.ttl = ttl
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class AddLayer7CCRuleResponseBody(TeaModel):
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


class AddLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddLayer7CCRuleResponseBody = None,
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
            temp_model = AddLayer7CCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseDomainSlsConfigRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CloseDomainSlsConfigResponseBody(TeaModel):
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


class CloseDomainSlsConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseDomainSlsConfigResponseBody = None,
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
            temp_model = CloseDomainSlsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigHealthCheckRequest(TeaModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        health_check: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # This parameter is required.
        self.frontend_port = frontend_port
        # This parameter is required.
        self.health_check = health_check
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConfigHealthCheckResponseBody(TeaModel):
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


class ConfigHealthCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigHealthCheckResponseBody = None,
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
            temp_model = ConfigHealthCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RuleRequestUsTimeout(TeaModel):
    def __init__(
        self,
        connect_timeout: int = None,
        rs_timeout: int = None,
    ):
        self.connect_timeout = connect_timeout
        self.rs_timeout = rs_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.rs_timeout is not None:
            result['RsTimeout'] = self.rs_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('RsTimeout') is not None:
            self.rs_timeout = m.get('RsTimeout')
        return self


class ConfigLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout: ConfigLayer4RuleRequestUsTimeout = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout = us_timeout

    def validate(self):
        if self.us_timeout:
            self.us_timeout.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable
        if self.us_timeout is not None:
            result['UsTimeout'] = self.us_timeout.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')
        if m.get('UsTimeout') is not None:
            temp_model = ConfigLayer4RuleRequestUsTimeout()
            self.us_timeout = temp_model.from_map(m['UsTimeout'])
        return self


class ConfigLayer4RuleShrinkRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout_shrink: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout_shrink = us_timeout_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable
        if self.us_timeout_shrink is not None:
            result['UsTimeout'] = self.us_timeout_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')
        if m.get('UsTimeout') is not None:
            self.us_timeout_shrink = m.get('UsTimeout')
        return self


class ConfigLayer4RuleResponseBody(TeaModel):
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


class ConfigLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer4RuleResponseBody = None,
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
            temp_model = ConfigLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer4RuleAttributeRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.config = config
        # This parameter is required.
        self.forward_protocol = forward_protocol
        # This parameter is required.
        self.frontend_port = frontend_port
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConfigLayer4RuleAttributeResponseBody(TeaModel):
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


class ConfigLayer4RuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer4RuleAttributeResponseBody = None,
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
            temp_model = ConfigLayer4RuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer7BlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        black_list: List[str] = None,
        domain: str = None,
        resource_group_id: str = None,
        white_list: List[str] = None,
    ):
        self.black_list = black_list
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigLayer7BlackWhiteListResponseBody(TeaModel):
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


class ConfigLayer7BlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer7BlackWhiteListResponseBody = None,
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
            temp_model = ConfigLayer7BlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        act: str = None,
        count: int = None,
        domain: str = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        resource_group_id: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        # This parameter is required.
        self.act = act
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.interval = interval
        # This parameter is required.
        self.mode = mode
        # This parameter is required.
        self.name = name
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.ttl = ttl
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ConfigLayer7CCRuleResponseBody(TeaModel):
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


class ConfigLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer7CCRuleResponseBody = None,
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
            temp_model = ConfigLayer7CCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer7CCTemplateRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        template: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ConfigLayer7CCTemplateResponseBody(TeaModel):
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


class ConfigLayer7CCTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer7CCTemplateResponseBody = None,
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
            temp_model = ConfigLayer7CCTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer7CertRequest(TeaModel):
    def __init__(
        self,
        cert: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        cert_region: str = None,
        domain: str = None,
        key: str = None,
        resource_group_id: str = None,
    ):
        self.cert = cert
        self.cert_id = cert_id
        self.cert_identifier = cert_identifier
        self.cert_name = cert_name
        self.cert_region = cert_region
        # This parameter is required.
        self.domain = domain
        self.key = key
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert is not None:
            result['Cert'] = self.cert
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ConfigLayer7CertResponseBody(TeaModel):
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


class ConfigLayer7CertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer7CertResponseBody = None,
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
            temp_model = ConfigLayer7CertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        proxy_type_list: str = None,
        proxy_types: List[str] = None,
        real_servers: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.instance_ids = instance_ids
        self.proxy_type_list = proxy_type_list
        self.proxy_types = proxy_types
        # This parameter is required.
        self.real_servers = real_servers
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rs_type = rs_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.proxy_type_list is not None:
            result['ProxyTypeList'] = self.proxy_type_list
        if self.proxy_types is not None:
            result['ProxyTypes'] = self.proxy_types
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ProxyTypeList') is not None:
            self.proxy_type_list = m.get('ProxyTypeList')
        if m.get('ProxyTypes') is not None:
            self.proxy_types = m.get('ProxyTypes')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class ConfigLayer7RuleResponseBody(TeaModel):
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


class ConfigLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigLayer7RuleResponseBody = None,
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
            temp_model = ConfigLayer7RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_params: str = None,
        task_type: int = None,
    ):
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.task_params = task_params
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreateAsyncTaskResponseBody(TeaModel):
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


class CreateAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAsyncTaskResponseBody = None,
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
            temp_model = CreateAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayer4RuleRequestUsTimeout(TeaModel):
    def __init__(
        self,
        connect_timeout: int = None,
        rs_timeout: int = None,
    ):
        self.connect_timeout = connect_timeout
        self.rs_timeout = rs_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.rs_timeout is not None:
            result['RsTimeout'] = self.rs_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('RsTimeout') is not None:
            self.rs_timeout = m.get('RsTimeout')
        return self


class CreateLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout: CreateLayer4RuleRequestUsTimeout = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout = us_timeout

    def validate(self):
        if self.us_timeout:
            self.us_timeout.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable
        if self.us_timeout is not None:
            result['UsTimeout'] = self.us_timeout.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')
        if m.get('UsTimeout') is not None:
            temp_model = CreateLayer4RuleRequestUsTimeout()
            self.us_timeout = temp_model.from_map(m['UsTimeout'])
        return self


class CreateLayer4RuleShrinkRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout_shrink: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout_shrink = us_timeout_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable
        if self.us_timeout_shrink is not None:
            result['UsTimeout'] = self.us_timeout_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')
        if m.get('UsTimeout') is not None:
            self.us_timeout_shrink = m.get('UsTimeout')
        return self


class CreateLayer4RuleResponseBody(TeaModel):
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


class CreateLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayer4RuleResponseBody = None,
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
            temp_model = CreateLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        resource_group_id: str = None,
        rs_type: int = None,
        rules: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.instance_ids = instance_ids
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.rs_type = rs_type
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class CreateLayer7RuleResponseBody(TeaModel):
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


class CreateLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLayer7RuleResponseBody = None,
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
            temp_model = CreateLayer7RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        task_id: int = None,
    ):
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteAsyncTaskResponseBody(TeaModel):
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


class DeleteAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAsyncTaskResponseBody = None,
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
            temp_model = DeleteAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayer4RuleRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        return self


class DeleteLayer4RuleResponseBody(TeaModel):
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


class DeleteLayer4RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLayer4RuleResponseBody = None,
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
            temp_model = DeleteLayer4RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        name: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.name = name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteLayer7CCRuleResponseBody(TeaModel):
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


class DeleteLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLayer7CCRuleResponseBody = None,
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
            temp_model = DeleteLayer7CCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLayer7RuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteLayer7RuleResponseBody(TeaModel):
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


class DeleteLayer7RuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLayer7RuleResponseBody = None,
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
            temp_model = DeleteLayer7RuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(
        self,
        ip_version: str = None,
        line: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.ip_version = ip_version
        self.line = line
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.line is not None:
            result['Line'] = self.line
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeBackSourceCidrResponseBody(TeaModel):
    def __init__(
        self,
        cidr_list: List[str] = None,
        request_id: str = None,
    ):
        self.cidr_list = cidr_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrList') is not None:
            self.cidr_list = m.get('CidrList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBackSourceCidrResponseBody = None,
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
            temp_model = DescribeBackSourceCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBatchSlsDispatchStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.page_no = page_no
        self.page_size = page_size
        self.resource_group_id = resource_group_id
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enable: bool = None,
    ):
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class DescribeBatchSlsDispatchStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_config_status_list: List[DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sls_config_status_list = sls_config_status_list
        self.total_count = total_count

    def validate(self):
        if self.sls_config_status_list:
            for k in self.sls_config_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlsConfigStatusList'] = []
        if self.sls_config_status_list is not None:
            for k in self.sls_config_status_list:
                result['SlsConfigStatusList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sls_config_status_list = []
        if m.get('SlsConfigStatusList') is not None:
            for k in m.get('SlsConfigStatusList'):
                temp_model = DescribeBatchSlsDispatchStatusResponseBodySlsConfigStatusList()
                self.sls_config_status_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBatchSlsDispatchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBatchSlsDispatchStatusResponseBody = None,
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
            temp_model = DescribeBatchSlsDispatchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSEventsRequest(TeaModel):
    def __init__(
        self,
        eip: str = None,
        end_time: int = None,
        offset: int = None,
        page_size: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.eip = eip
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDoSEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        interval: int = None,
        start_time: int = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.interval = interval
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDDoSEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeDDoSEventsResponseBodyEvents] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.events = events
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDDoSEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDDoSEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDDoSEventsResponseBody = None,
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
            temp_model = DescribeDDoSEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDDoSTrafficRequest(TeaModel):
    def __init__(
        self,
        eip: str = None,
        end_time: int = None,
        interval: int = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.eip = eip
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDDoSTrafficResponseBodyDDoSTrafficPoints(TeaModel):
    def __init__(
        self,
        defense_max_in_bps: int = None,
        source_max_in_bps: int = None,
        time: int = None,
    ):
        self.defense_max_in_bps = defense_max_in_bps
        self.source_max_in_bps = source_max_in_bps
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_max_in_bps is not None:
            result['DefenseMaxInBps'] = self.defense_max_in_bps
        if self.source_max_in_bps is not None:
            result['SourceMaxInBps'] = self.source_max_in_bps
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseMaxInBps') is not None:
            self.defense_max_in_bps = m.get('DefenseMaxInBps')
        if m.get('SourceMaxInBps') is not None:
            self.source_max_in_bps = m.get('SourceMaxInBps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeDDoSTrafficResponseBody(TeaModel):
    def __init__(
        self,
        ddo_straffic_points: List[DescribeDDoSTrafficResponseBodyDDoSTrafficPoints] = None,
        defense_in_bytes: int = None,
        request_id: str = None,
        source_in_bytes: int = None,
    ):
        self.ddo_straffic_points = ddo_straffic_points
        self.defense_in_bytes = defense_in_bytes
        self.request_id = request_id
        self.source_in_bytes = source_in_bytes

    def validate(self):
        if self.ddo_straffic_points:
            for k in self.ddo_straffic_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DDoSTrafficPoints'] = []
        if self.ddo_straffic_points is not None:
            for k in self.ddo_straffic_points:
                result['DDoSTrafficPoints'].append(k.to_map() if k else None)
        if self.defense_in_bytes is not None:
            result['DefenseInBytes'] = self.defense_in_bytes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_in_bytes is not None:
            result['SourceInBytes'] = self.source_in_bytes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddo_straffic_points = []
        if m.get('DDoSTrafficPoints') is not None:
            for k in m.get('DDoSTrafficPoints'):
                temp_model = DescribeDDoSTrafficResponseBodyDDoSTrafficPoints()
                self.ddo_straffic_points.append(temp_model.from_map(k))
        if m.get('DefenseInBytes') is not None:
            self.defense_in_bytes = m.get('DefenseInBytes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceInBytes') is not None:
            self.source_in_bytes = m.get('SourceInBytes')
        return self


class DescribeDDoSTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDDoSTrafficResponseBody = None,
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
            temp_model = DescribeDDoSTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDefenseCountStatisticsRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics(TeaModel):
    def __init__(
        self,
        defense_count_total_usage_of_current_month: int = None,
        flow_pack_count_remain: int = None,
        max_usable_defense_count_current_month: int = None,
    ):
        self.defense_count_total_usage_of_current_month = defense_count_total_usage_of_current_month
        self.flow_pack_count_remain = flow_pack_count_remain
        self.max_usable_defense_count_current_month = max_usable_defense_count_current_month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_total_usage_of_current_month is not None:
            result['DefenseCountTotalUsageOfCurrentMonth'] = self.defense_count_total_usage_of_current_month
        if self.flow_pack_count_remain is not None:
            result['FlowPackCountRemain'] = self.flow_pack_count_remain
        if self.max_usable_defense_count_current_month is not None:
            result['MaxUsableDefenseCountCurrentMonth'] = self.max_usable_defense_count_current_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountTotalUsageOfCurrentMonth') is not None:
            self.defense_count_total_usage_of_current_month = m.get('DefenseCountTotalUsageOfCurrentMonth')
        if m.get('FlowPackCountRemain') is not None:
            self.flow_pack_count_remain = m.get('FlowPackCountRemain')
        if m.get('MaxUsableDefenseCountCurrentMonth') is not None:
            self.max_usable_defense_count_current_month = m.get('MaxUsableDefenseCountCurrentMonth')
        return self


class DescribeDefenseCountStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        defense_count_statistics: DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics = None,
        request_id: str = None,
    ):
        self.defense_count_statistics = defense_count_statistics
        self.request_id = request_id

    def validate(self):
        if self.defense_count_statistics:
            self.defense_count_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_statistics is not None:
            result['DefenseCountStatistics'] = self.defense_count_statistics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountStatistics') is not None:
            temp_model = DescribeDefenseCountStatisticsResponseBodyDefenseCountStatistics()
            self.defense_count_statistics = temp_model.from_map(m['DefenseCountStatistics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDefenseCountStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDefenseCountStatisticsResponseBody = None,
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
            temp_model = DescribeDefenseCountStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAccessModeRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain_list = domain_list
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainAccessModeResponseBodyDomainModeList(TeaModel):
    def __init__(
        self,
        access_mode: int = None,
        domain: str = None,
    ):
        self.access_mode = access_mode
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainAccessModeResponseBody(TeaModel):
    def __init__(
        self,
        domain_mode_list: List[DescribeDomainAccessModeResponseBodyDomainModeList] = None,
        request_id: str = None,
    ):
        self.domain_mode_list = domain_mode_list
        self.request_id = request_id

    def validate(self):
        if self.domain_mode_list:
            for k in self.domain_mode_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainModeList'] = []
        if self.domain_mode_list is not None:
            for k in self.domain_mode_list:
                result['DomainModeList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_mode_list = []
        if m.get('DomainModeList') is not None:
            for k in m.get('DomainModeList'):
                temp_model = DescribeDomainAccessModeResponseBodyDomainModeList()
                self.domain_mode_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAccessModeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainAccessModeResponseBody = None,
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
            temp_model = DescribeDomainAccessModeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackEventListRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAttackEventListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        max_qps: int = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        self.max_qps = max_qps
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAttackEventListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeDomainAttackEventListResponseBodyDataList] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.total = total

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeDomainAttackEventListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDomainAttackEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainAttackEventListResponseBody = None,
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
            temp_model = DescribeDomainAttackEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainAttackMaxQpsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        # This parameter is required.
        self.end_time = end_time
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainAttackMaxQpsResponseBody(TeaModel):
    def __init__(
        self,
        qps: str = None,
        request_id: str = None,
    ):
        self.qps = qps
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainAttackMaxQpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainAttackMaxQpsResponseBody = None,
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
            temp_model = DescribeDomainAttackMaxQpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainOverviewRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        self.resource_group_id = resource_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainOverviewResponseBody(TeaModel):
    def __init__(
        self,
        max_http: int = None,
        max_https: int = None,
        request_id: str = None,
    ):
        self.max_http = max_http
        self.max_https = max_https
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_http is not None:
            result['MaxHttp'] = self.max_http
        if self.max_https is not None:
            result['MaxHttps'] = self.max_https
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxHttp') is not None:
            self.max_http = m.get('MaxHttp')
        if m.get('MaxHttps') is not None:
            self.max_https = m.get('MaxHttps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainOverviewResponseBody = None,
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
            temp_model = DescribeDomainOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsListRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        interval: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        self.resource_group_id = resource_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        attack_qps: int = None,
        cache_hits: int = None,
        index: int = None,
        max_attack_qps: int = None,
        max_normal_qps: int = None,
        max_qps: int = None,
        total_count: int = None,
        total_qps: int = None,
    ):
        self.attack_qps = attack_qps
        self.cache_hits = cache_hits
        self.index = index
        self.max_attack_qps = max_attack_qps
        self.max_normal_qps = max_normal_qps
        self.max_qps = max_qps
        self.total_count = total_count
        self.total_qps = total_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attack_qps is not None:
            result['AttackQps'] = self.attack_qps
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.index is not None:
            result['Index'] = self.index
        if self.max_attack_qps is not None:
            result['MaxAttackQps'] = self.max_attack_qps
        if self.max_normal_qps is not None:
            result['MaxNormalQps'] = self.max_normal_qps
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_qps is not None:
            result['TotalQps'] = self.total_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackQps') is not None:
            self.attack_qps = m.get('AttackQps')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('MaxAttackQps') is not None:
            self.max_attack_qps = m.get('MaxAttackQps')
        if m.get('MaxNormalQps') is not None:
            self.max_normal_qps = m.get('MaxNormalQps')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalQps') is not None:
            self.total_qps = m.get('TotalQps')
        return self


class DescribeDomainQpsListResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeDomainQpsListResponseBodyDataList] = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeDomainQpsListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDomainQpsListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainQpsListResponseBody = None,
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
            temp_model = DescribeDomainQpsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainQpsWithCacheRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        # This parameter is required.
        self.end_time = end_time
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainQpsWithCacheResponseBody(TeaModel):
    def __init__(
        self,
        blocks: List[str] = None,
        cache_hits: List[str] = None,
        cc_block_qps: List[str] = None,
        cc_js_qps: List[str] = None,
        interval: int = None,
        ip_block_qps: List[str] = None,
        precise_blocks: List[str] = None,
        precise_js_qps: List[str] = None,
        region_blocks: List[str] = None,
        request_id: str = None,
        start_time: int = None,
        totals: List[str] = None,
    ):
        self.blocks = blocks
        self.cache_hits = cache_hits
        self.cc_block_qps = cc_block_qps
        self.cc_js_qps = cc_js_qps
        self.interval = interval
        self.ip_block_qps = ip_block_qps
        self.precise_blocks = precise_blocks
        self.precise_js_qps = precise_js_qps
        self.region_blocks = region_blocks
        self.request_id = request_id
        self.start_time = start_time
        self.totals = totals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blocks is not None:
            result['Blocks'] = self.blocks
        if self.cache_hits is not None:
            result['CacheHits'] = self.cache_hits
        if self.cc_block_qps is not None:
            result['CcBlockQps'] = self.cc_block_qps
        if self.cc_js_qps is not None:
            result['CcJsQps'] = self.cc_js_qps
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.ip_block_qps is not None:
            result['IpBlockQps'] = self.ip_block_qps
        if self.precise_blocks is not None:
            result['PreciseBlocks'] = self.precise_blocks
        if self.precise_js_qps is not None:
            result['PreciseJsQps'] = self.precise_js_qps
        if self.region_blocks is not None:
            result['RegionBlocks'] = self.region_blocks
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.totals is not None:
            result['Totals'] = self.totals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blocks') is not None:
            self.blocks = m.get('Blocks')
        if m.get('CacheHits') is not None:
            self.cache_hits = m.get('CacheHits')
        if m.get('CcBlockQps') is not None:
            self.cc_block_qps = m.get('CcBlockQps')
        if m.get('CcJsQps') is not None:
            self.cc_js_qps = m.get('CcJsQps')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('IpBlockQps') is not None:
            self.ip_block_qps = m.get('IpBlockQps')
        if m.get('PreciseBlocks') is not None:
            self.precise_blocks = m.get('PreciseBlocks')
        if m.get('PreciseJsQps') is not None:
            self.precise_js_qps = m.get('PreciseJsQps')
        if m.get('RegionBlocks') is not None:
            self.region_blocks = m.get('RegionBlocks')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Totals') is not None:
            self.totals = m.get('Totals')
        return self


class DescribeDomainQpsWithCacheResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainQpsWithCacheResponseBody = None,
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
            temp_model = DescribeDomainQpsWithCacheResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSlsStatusRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainSlsStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_logstore: str = None,
        sls_project: str = None,
        sls_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_logstore = sls_logstore
        self.sls_project = sls_project
        self.sls_status = sls_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_logstore is not None:
            result['SlsLogstore'] = self.sls_logstore
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.sls_status is not None:
            result['SlsStatus'] = self.sls_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsLogstore') is not None:
            self.sls_logstore = m.get('SlsLogstore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('SlsStatus') is not None:
            self.sls_status = m.get('SlsStatus')
        return self


class DescribeDomainSlsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainSlsStatusResponseBody = None,
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
            temp_model = DescribeDomainSlsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainStatusCodeListRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        interval: int = None,
        query_type: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        self.domain = domain
        self.end_time = end_time
        self.interval = interval
        # This parameter is required.
        self.query_type = query_type
        self.resource_group_id = resource_group_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDomainStatusCodeListResponseBodyStatusCodeList(TeaModel):
    def __init__(
        self,
        index: int = None,
        status_200: int = None,
        status_2xx: int = None,
        status_3xx: int = None,
        status_403: int = None,
        status_404: int = None,
        status_405: int = None,
        status_410: int = None,
        status_499: int = None,
        status_4xx: int = None,
        status_501: int = None,
        status_502: int = None,
        status_503: int = None,
        status_504: int = None,
        status_5xx: int = None,
    ):
        self.index = index
        self.status_200 = status_200
        self.status_2xx = status_2xx
        self.status_3xx = status_3xx
        self.status_403 = status_403
        self.status_404 = status_404
        self.status_405 = status_405
        self.status_410 = status_410
        self.status_499 = status_499
        self.status_4xx = status_4xx
        self.status_501 = status_501
        self.status_502 = status_502
        self.status_503 = status_503
        self.status_504 = status_504
        self.status_5xx = status_5xx

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.status_200 is not None:
            result['Status200'] = self.status_200
        if self.status_2xx is not None:
            result['Status2XX'] = self.status_2xx
        if self.status_3xx is not None:
            result['Status3XX'] = self.status_3xx
        if self.status_403 is not None:
            result['Status403'] = self.status_403
        if self.status_404 is not None:
            result['Status404'] = self.status_404
        if self.status_405 is not None:
            result['Status405'] = self.status_405
        if self.status_410 is not None:
            result['Status410'] = self.status_410
        if self.status_499 is not None:
            result['Status499'] = self.status_499
        if self.status_4xx is not None:
            result['Status4XX'] = self.status_4xx
        if self.status_501 is not None:
            result['Status501'] = self.status_501
        if self.status_502 is not None:
            result['Status502'] = self.status_502
        if self.status_503 is not None:
            result['Status503'] = self.status_503
        if self.status_504 is not None:
            result['Status504'] = self.status_504
        if self.status_5xx is not None:
            result['Status5XX'] = self.status_5xx
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Status200') is not None:
            self.status_200 = m.get('Status200')
        if m.get('Status2XX') is not None:
            self.status_2xx = m.get('Status2XX')
        if m.get('Status3XX') is not None:
            self.status_3xx = m.get('Status3XX')
        if m.get('Status403') is not None:
            self.status_403 = m.get('Status403')
        if m.get('Status404') is not None:
            self.status_404 = m.get('Status404')
        if m.get('Status405') is not None:
            self.status_405 = m.get('Status405')
        if m.get('Status410') is not None:
            self.status_410 = m.get('Status410')
        if m.get('Status499') is not None:
            self.status_499 = m.get('Status499')
        if m.get('Status4XX') is not None:
            self.status_4xx = m.get('Status4XX')
        if m.get('Status501') is not None:
            self.status_501 = m.get('Status501')
        if m.get('Status502') is not None:
            self.status_502 = m.get('Status502')
        if m.get('Status503') is not None:
            self.status_503 = m.get('Status503')
        if m.get('Status504') is not None:
            self.status_504 = m.get('Status504')
        if m.get('Status5XX') is not None:
            self.status_5xx = m.get('Status5XX')
        return self


class DescribeDomainStatusCodeListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_code_list: List[DescribeDomainStatusCodeListResponseBodyStatusCodeList] = None,
    ):
        self.request_id = request_id
        self.status_code_list = status_code_list

    def validate(self):
        if self.status_code_list:
            for k in self.status_code_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusCodeList'] = []
        if self.status_code_list is not None:
            for k in self.status_code_list:
                result['StatusCodeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_code_list = []
        if m.get('StatusCodeList') is not None:
            for k in m.get('StatusCodeList'):
                temp_model = DescribeDomainStatusCodeListResponseBodyStatusCodeList()
                self.status_code_list.append(temp_model.from_map(k))
        return self


class DescribeDomainStatusCodeListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainStatusCodeListResponseBody = None,
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
            temp_model = DescribeDomainStatusCodeListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainsRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        offset: int = None,
        page_size: str = None,
        query_domain_pattern: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.domain = domain
        self.instance_ids = instance_ids
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.page_size = page_size
        self.query_domain_pattern = query_domain_pattern
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeDomainsResponseBodyDomainsProxyTypeList(TeaModel):
    def __init__(
        self,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class DescribeDomainsResponseBodyDomainsRealServers(TeaModel):
    def __init__(
        self,
        real_server: str = None,
        rs_type: int = None,
    ):
        self.real_server = real_server
        self.rs_type = rs_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        if self.rs_type is not None:
            result['RsType'] = self.rs_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        if m.get('RsType') is not None:
            self.rs_type = m.get('RsType')
        return self


class DescribeDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        black_list: List[str] = None,
        cc_enabled: bool = None,
        cc_rule_enabled: bool = None,
        cc_template: str = None,
        cert_name: str = None,
        cert_region: str = None,
        cname: str = None,
        domain: str = None,
        http_2enable: bool = None,
        proxy_type_list: List[DescribeDomainsResponseBodyDomainsProxyTypeList] = None,
        real_servers: List[DescribeDomainsResponseBodyDomainsRealServers] = None,
        ssl_ciphers: str = None,
        ssl_protocols: str = None,
        white_list: List[str] = None,
    ):
        self.black_list = black_list
        self.cc_enabled = cc_enabled
        self.cc_rule_enabled = cc_rule_enabled
        self.cc_template = cc_template
        self.cert_name = cert_name
        self.cert_region = cert_region
        self.cname = cname
        self.domain = domain
        self.http_2enable = http_2enable
        self.proxy_type_list = proxy_type_list
        self.real_servers = real_servers
        self.ssl_ciphers = ssl_ciphers
        self.ssl_protocols = ssl_protocols
        self.white_list = white_list

    def validate(self):
        if self.proxy_type_list:
            for k in self.proxy_type_list:
                if k:
                    k.validate()
        if self.real_servers:
            for k in self.real_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.cc_enabled is not None:
            result['CcEnabled'] = self.cc_enabled
        if self.cc_rule_enabled is not None:
            result['CcRuleEnabled'] = self.cc_rule_enabled
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.http_2enable is not None:
            result['Http2Enable'] = self.http_2enable
        result['ProxyTypeList'] = []
        if self.proxy_type_list is not None:
            for k in self.proxy_type_list:
                result['ProxyTypeList'].append(k.to_map() if k else None)
        result['RealServers'] = []
        if self.real_servers is not None:
            for k in self.real_servers:
                result['RealServers'].append(k.to_map() if k else None)
        if self.ssl_ciphers is not None:
            result['SslCiphers'] = self.ssl_ciphers
        if self.ssl_protocols is not None:
            result['SslProtocols'] = self.ssl_protocols
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('CcEnabled') is not None:
            self.cc_enabled = m.get('CcEnabled')
        if m.get('CcRuleEnabled') is not None:
            self.cc_rule_enabled = m.get('CcRuleEnabled')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Http2Enable') is not None:
            self.http_2enable = m.get('Http2Enable')
        self.proxy_type_list = []
        if m.get('ProxyTypeList') is not None:
            for k in m.get('ProxyTypeList'):
                temp_model = DescribeDomainsResponseBodyDomainsProxyTypeList()
                self.proxy_type_list.append(temp_model.from_map(k))
        self.real_servers = []
        if m.get('RealServers') is not None:
            for k in m.get('RealServers'):
                temp_model = DescribeDomainsResponseBodyDomainsRealServers()
                self.real_servers.append(temp_model.from_map(k))
        if m.get('SslCiphers') is not None:
            self.ssl_ciphers = m.get('SslCiphers')
        if m.get('SslProtocols') is not None:
            self.ssl_protocols = m.get('SslProtocols')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domains: List[DescribeDomainsResponseBodyDomains] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.domains = domains
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = DescribeDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDomainsResponseBody = None,
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
            temp_model = DescribeDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticBandwidthSpecRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeElasticBandwidthSpecResponseBody(TeaModel):
    def __init__(
        self,
        elastic_bandwidth_spec: List[str] = None,
        request_id: str = None,
    ):
        self.elastic_bandwidth_spec = elastic_bandwidth_spec
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElasticBandwidthSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeElasticBandwidthSpecResponseBody = None,
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
            temp_model = DescribeElasticBandwidthSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckListRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeHealthCheckListResponseBodyListenersHealthCheck(TeaModel):
    def __init__(
        self,
        domain: str = None,
        down: int = None,
        interval: int = None,
        port: int = None,
        timeout: int = None,
        type: str = None,
        up: int = None,
        uri: str = None,
    ):
        self.domain = domain
        self.down = down
        self.interval = interval
        self.port = port
        self.timeout = timeout
        self.type = type
        self.up = up
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.down is not None:
            result['Down'] = self.down
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.type is not None:
            result['Type'] = self.type
        if self.up is not None:
            result['Up'] = self.up
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeHealthCheckListResponseBodyListeners(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        health_check: DescribeHealthCheckListResponseBodyListenersHealthCheck = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        self.frontend_port = frontend_port
        self.health_check = health_check
        self.instance_id = instance_id
        self.protocol = protocol

    def validate(self):
        if self.health_check:
            self.health_check.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('HealthCheck') is not None:
            temp_model = DescribeHealthCheckListResponseBodyListenersHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeHealthCheckListResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[DescribeHealthCheckListResponseBodyListeners] = None,
        request_id: str = None,
    ):
        self.listeners = listeners
        self.request_id = request_id

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeHealthCheckListResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHealthCheckListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHealthCheckListResponseBody = None,
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
            temp_model = DescribeHealthCheckListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckStatusListRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList(TeaModel):
    def __init__(
        self,
        address: str = None,
        status: str = None,
    ):
        self.address = address
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
        real_server_status_list: List[DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList] = None,
        status: str = None,
    ):
        self.frontend_port = frontend_port
        self.instance_id = instance_id
        self.protocol = protocol
        self.real_server_status_list = real_server_status_list
        self.status = status

    def validate(self):
        if self.real_server_status_list:
            for k in self.real_server_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        result['RealServerStatusList'] = []
        if self.real_server_status_list is not None:
            for k in self.real_server_status_list:
                result['RealServerStatusList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        self.real_server_status_list = []
        if m.get('RealServerStatusList') is not None:
            for k in m.get('RealServerStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseBodyHealthCheckStatusListRealServerStatusList()
                self.real_server_status_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeHealthCheckStatusListResponseBody(TeaModel):
    def __init__(
        self,
        health_check_status_list: List[DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList] = None,
        request_id: str = None,
    ):
        self.health_check_status_list = health_check_status_list
        self.request_id = request_id

    def validate(self):
        if self.health_check_status_list:
            for k in self.health_check_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HealthCheckStatusList'] = []
        if self.health_check_status_list is not None:
            for k in self.health_check_status_list:
                result['HealthCheckStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.health_check_status_list = []
        if m.get('HealthCheckStatusList') is not None:
            for k in m.get('HealthCheckStatusList'):
                temp_model = DescribeHealthCheckStatusListResponseBodyHealthCheckStatusList()
                self.health_check_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHealthCheckStatusListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHealthCheckStatusListResponseBody = None,
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
            temp_model = DescribeHealthCheckStatusListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDetailsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList(TeaModel):
    def __init__(
        self,
        eip: str = None,
        status: str = None,
    ):
        self.eip = eip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstanceDetailsResponseBodyInstanceDetails(TeaModel):
    def __init__(
        self,
        eip_info_list: List[DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList] = None,
        instance_id: str = None,
        line: str = None,
    ):
        self.eip_info_list = eip_info_list
        self.instance_id = instance_id
        self.line = line

    def validate(self):
        if self.eip_info_list:
            for k in self.eip_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EipInfoList'] = []
        if self.eip_info_list is not None:
            for k in self.eip_info_list:
                result['EipInfoList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.line is not None:
            result['Line'] = self.line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_info_list = []
        if m.get('EipInfoList') is not None:
            for k in m.get('EipInfoList'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetailsEipInfoList()
                self.eip_info_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        return self


class DescribeInstanceDetailsResponseBody(TeaModel):
    def __init__(
        self,
        instance_details: List[DescribeInstanceDetailsResponseBodyInstanceDetails] = None,
        request_id: str = None,
    ):
        self.instance_details = instance_details
        self.request_id = request_id

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribeInstanceDetailsResponseBodyInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceDetailsResponseBody = None,
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
            temp_model = DescribeInstanceDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        bandwidth_mbps: int = None,
        base_bandwidth: int = None,
        defense_count: int = None,
        domain_limit: int = None,
        elastic_bandwidth: int = None,
        function_version: str = None,
        instance_id: str = None,
        port_limit: int = None,
        qps_limit: int = None,
        site_limit: int = None,
    ):
        self.bandwidth_mbps = bandwidth_mbps
        self.base_bandwidth = base_bandwidth
        self.defense_count = defense_count
        self.domain_limit = domain_limit
        self.elastic_bandwidth = elastic_bandwidth
        self.function_version = function_version
        self.instance_id = instance_id
        self.port_limit = port_limit
        self.qps_limit = qps_limit
        self.site_limit = site_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_mbps is not None:
            result['BandwidthMbps'] = self.bandwidth_mbps
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.defense_count is not None:
            result['DefenseCount'] = self.defense_count
        if self.domain_limit is not None:
            result['DomainLimit'] = self.domain_limit
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_limit is not None:
            result['PortLimit'] = self.port_limit
        if self.qps_limit is not None:
            result['QpsLimit'] = self.qps_limit
        if self.site_limit is not None:
            result['SiteLimit'] = self.site_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthMbps') is not None:
            self.bandwidth_mbps = m.get('BandwidthMbps')
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('DefenseCount') is not None:
            self.defense_count = m.get('DefenseCount')
        if m.get('DomainLimit') is not None:
            self.domain_limit = m.get('DomainLimit')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortLimit') is not None:
            self.port_limit = m.get('PortLimit')
        if m.get('QpsLimit') is not None:
            self.qps_limit = m.get('QpsLimit')
        if m.get('SiteLimit') is not None:
            self.site_limit = m.get('SiteLimit')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(
        self,
        instance_specs: List[DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
        request_id: str = None,
    ):
        self.instance_specs = instance_specs
        self.request_id = request_id

    def validate(self):
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSpecsResponseBody = None,
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
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceStatisticsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.instance_ids = instance_ids
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeInstanceStatisticsResponseBodyInstanceStatistics(TeaModel):
    def __init__(
        self,
        defense_count_usage: int = None,
        domain_usage: int = None,
        instance_id: str = None,
        port_usage: int = None,
        site_usage: int = None,
    ):
        self.defense_count_usage = defense_count_usage
        self.domain_usage = domain_usage
        self.instance_id = instance_id
        self.port_usage = port_usage
        self.site_usage = site_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.defense_count_usage is not None:
            result['DefenseCountUsage'] = self.defense_count_usage
        if self.domain_usage is not None:
            result['DomainUsage'] = self.domain_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port_usage is not None:
            result['PortUsage'] = self.port_usage
        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseCountUsage') is not None:
            self.defense_count_usage = m.get('DefenseCountUsage')
        if m.get('DomainUsage') is not None:
            self.domain_usage = m.get('DomainUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PortUsage') is not None:
            self.port_usage = m.get('PortUsage')
        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')
        return self


class DescribeInstanceStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        instance_statistics: List[DescribeInstanceStatisticsResponseBodyInstanceStatistics] = None,
        request_id: str = None,
    ):
        self.instance_statistics = instance_statistics
        self.request_id = request_id

    def validate(self):
        if self.instance_statistics:
            for k in self.instance_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceStatistics'] = []
        if self.instance_statistics is not None:
            for k in self.instance_statistics:
                result['InstanceStatistics'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_statistics = []
        if m.get('InstanceStatistics') is not None:
            for k in m.get('InstanceStatistics'):
                temp_model = DescribeInstanceStatisticsResponseBodyInstanceStatistics()
                self.instance_statistics.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceStatisticsResponseBody = None,
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
            temp_model = DescribeInstanceStatisticsResponseBody()
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
        edition: int = None,
        enabled: int = None,
        expire_end_time: int = None,
        expire_start_time: int = None,
        instance_ids: str = None,
        ip: str = None,
        page_no: str = None,
        page_size: str = None,
        remark: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        status: List[int] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.edition = edition
        self.enabled = enabled
        self.expire_end_time = expire_end_time
        self.expire_start_time = expire_start_time
        self.instance_ids = instance_ids
        self.ip = ip
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        self.status = status
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
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_end_time is not None:
            result['ExpireEndTime'] = self.expire_end_time
        if self.expire_start_time is not None:
            result['ExpireStartTime'] = self.expire_start_time
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireEndTime') is not None:
            self.expire_end_time = m.get('ExpireEndTime')
        if m.get('ExpireStartTime') is not None:
            self.expire_start_time = m.get('ExpireStartTime')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        debt_status: int = None,
        edition: int = None,
        enabled: int = None,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        remark: str = None,
        status: int = None,
    ):
        self.debt_status = debt_status
        self.edition = edition
        self.enabled = enabled
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debt_status is not None:
            result['DebtStatus'] = self.debt_status
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebtStatus') is not None:
            self.debt_status = m.get('DebtStatus')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total = total

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
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpTrafficRequest(TeaModel):
    def __init__(
        self,
        eip: str = None,
        end_time: int = None,
        interval: int = None,
        port: int = None,
        query_protocol: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.eip = eip
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        self.port = port
        self.query_protocol = query_protocol
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.port is not None:
            result['Port'] = self.port
        if self.query_protocol is not None:
            result['QueryProtocol'] = self.query_protocol
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('QueryProtocol') is not None:
            self.query_protocol = m.get('QueryProtocol')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeIpTrafficResponseBodyIpTrafficPoints(TeaModel):
    def __init__(
        self,
        act_conns: int = None,
        cps: int = None,
        inact_conns: int = None,
        max_inbps: int = None,
        max_outbps: int = None,
        time: int = None,
    ):
        self.act_conns = act_conns
        self.cps = cps
        self.inact_conns = inact_conns
        self.max_inbps = max_inbps
        self.max_outbps = max_outbps
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.inact_conns is not None:
            result['InactConns'] = self.inact_conns
        if self.max_inbps is not None:
            result['MaxInbps'] = self.max_inbps
        if self.max_outbps is not None:
            result['MaxOutbps'] = self.max_outbps
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('InactConns') is not None:
            self.inact_conns = m.get('InactConns')
        if m.get('MaxInbps') is not None:
            self.max_inbps = m.get('MaxInbps')
        if m.get('MaxOutbps') is not None:
            self.max_outbps = m.get('MaxOutbps')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeIpTrafficResponseBody(TeaModel):
    def __init__(
        self,
        avg_in_bps: int = None,
        avg_out_bps: int = None,
        ip_traffic_points: List[DescribeIpTrafficResponseBodyIpTrafficPoints] = None,
        max_in_bps: int = None,
        max_out_bps: int = None,
        request_id: str = None,
    ):
        self.avg_in_bps = avg_in_bps
        self.avg_out_bps = avg_out_bps
        self.ip_traffic_points = ip_traffic_points
        self.max_in_bps = max_in_bps
        self.max_out_bps = max_out_bps
        self.request_id = request_id

    def validate(self):
        if self.ip_traffic_points:
            for k in self.ip_traffic_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_in_bps is not None:
            result['AvgInBps'] = self.avg_in_bps
        if self.avg_out_bps is not None:
            result['AvgOutBps'] = self.avg_out_bps
        result['IpTrafficPoints'] = []
        if self.ip_traffic_points is not None:
            for k in self.ip_traffic_points:
                result['IpTrafficPoints'].append(k.to_map() if k else None)
        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps
        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgInBps') is not None:
            self.avg_in_bps = m.get('AvgInBps')
        if m.get('AvgOutBps') is not None:
            self.avg_out_bps = m.get('AvgOutBps')
        self.ip_traffic_points = []
        if m.get('IpTrafficPoints') is not None:
            for k in m.get('IpTrafficPoints'):
                temp_model = DescribeIpTrafficResponseBodyIpTrafficPoints()
                self.ip_traffic_points.append(temp_model.from_map(k))
        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')
        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeIpTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeIpTrafficResponseBody = None,
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
            temp_model = DescribeIpTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLayer4RuleAttributesRequest(TeaModel):
    def __init__(
        self,
        listeners: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listeners is not None:
            result['Listeners'] = self.listeners
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack(TeaModel):
    def __init__(
        self,
        cnt: int = None,
        during: int = None,
        expires: int = None,
        type: int = None,
    ):
        self.cnt = cnt
        self.during = during
        self.expires = expires
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cnt is not None:
            result['Cnt'] = self.cnt
        if self.during is not None:
            result['During'] = self.during
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnt') is not None:
            self.cnt = m.get('Cnt')
        if m.get('During') is not None:
            self.during = m.get('During')
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfigCc(TeaModel):
    def __init__(
        self,
        sblack: List[DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack] = None,
    ):
        self.sblack = sblack

    def validate(self):
        if self.sblack:
            for k in self.sblack:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sblack'] = []
        if self.sblack is not None:
            for k in self.sblack:
                result['Sblack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sblack = []
        if m.get('Sblack') is not None:
            for k in m.get('Sblack'):
                temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfigCcSblack()
                self.sblack.append(temp_model.from_map(k))
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen(TeaModel):
    def __init__(
        self,
        max: int = None,
        min: int = None,
    ):
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfigSla(TeaModel):
    def __init__(
        self,
        cps: int = None,
        cps_enable: int = None,
        maxconn: int = None,
        maxconn_enable: int = None,
    ):
        self.cps = cps
        self.cps_enable = cps_enable
        self.maxconn = maxconn
        self.maxconn_enable = maxconn_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit(TeaModel):
    def __init__(
        self,
        bps: int = None,
        cps: int = None,
        cps_enable: int = None,
        cps_mode: int = None,
        maxconn: int = None,
        maxconn_enable: int = None,
        pps: int = None,
    ):
        self.bps = bps
        self.cps = cps
        self.cps_enable = cps_enable
        self.cps_mode = cps_mode
        self.maxconn = maxconn
        self.maxconn_enable = maxconn_enable
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps_mode is not None:
            result['CpsMode'] = self.cps_mode
        if self.maxconn is not None:
            result['Maxconn'] = self.maxconn
        if self.maxconn_enable is not None:
            result['MaxconnEnable'] = self.maxconn_enable
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('CpsMode') is not None:
            self.cps_mode = m.get('CpsMode')
        if m.get('Maxconn') is not None:
            self.maxconn = m.get('Maxconn')
        if m.get('MaxconnEnable') is not None:
            self.maxconn_enable = m.get('MaxconnEnable')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeLayer4RuleAttributesResponseBodyListenersConfig(TeaModel):
    def __init__(
        self,
        cc: DescribeLayer4RuleAttributesResponseBodyListenersConfigCc = None,
        nodata_conn: str = None,
        payload_len: DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen = None,
        persistence_timeout: int = None,
        sla: DescribeLayer4RuleAttributesResponseBodyListenersConfigSla = None,
        slimit: DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit = None,
        synproxy: str = None,
    ):
        self.cc = cc
        self.nodata_conn = nodata_conn
        self.payload_len = payload_len
        self.persistence_timeout = persistence_timeout
        self.sla = sla
        self.slimit = slimit
        self.synproxy = synproxy

    def validate(self):
        if self.cc:
            self.cc.validate()
        if self.payload_len:
            self.payload_len.validate()
        if self.sla:
            self.sla.validate()
        if self.slimit:
            self.slimit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cc is not None:
            result['Cc'] = self.cc.to_map()
        if self.nodata_conn is not None:
            result['NodataConn'] = self.nodata_conn
        if self.payload_len is not None:
            result['PayloadLen'] = self.payload_len.to_map()
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        if self.synproxy is not None:
            result['Synproxy'] = self.synproxy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cc') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfigCc()
            self.cc = temp_model.from_map(m['Cc'])
        if m.get('NodataConn') is not None:
            self.nodata_conn = m.get('NodataConn')
        if m.get('PayloadLen') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfigPayloadLen()
            self.payload_len = temp_model.from_map(m['PayloadLen'])
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('Sla') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfigSla()
            self.sla = temp_model.from_map(m['Sla'])
        if m.get('Slimit') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfigSlimit()
            self.slimit = temp_model.from_map(m['Slimit'])
        if m.get('Synproxy') is not None:
            self.synproxy = m.get('Synproxy')
        return self


class DescribeLayer4RuleAttributesResponseBodyListeners(TeaModel):
    def __init__(
        self,
        config: DescribeLayer4RuleAttributesResponseBodyListenersConfig = None,
        frontend_port: int = None,
        instance_id: str = None,
        protocol: str = None,
    ):
        self.config = config
        self.frontend_port = frontend_port
        self.instance_id = instance_id
        self.protocol = protocol

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = DescribeLayer4RuleAttributesResponseBodyListenersConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeLayer4RuleAttributesResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[DescribeLayer4RuleAttributesResponseBodyListeners] = None,
        request_id: str = None,
    ):
        self.listeners = listeners
        self.request_id = request_id

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeLayer4RuleAttributesResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLayer4RuleAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLayer4RuleAttributesResponseBody = None,
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
            temp_model = DescribeLayer4RuleAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLayer4RulesRequest(TeaModel):
    def __init__(
        self,
        forward_protocol: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        offset: int = None,
        page_size: str = None,
        source_ip: str = None,
    ):
        # The type of forwarding protocol. Values:
        # - **tcp**: Indicates TCP protocol.
        # - **udp**: Indicates UDP protocol.
        self.forward_protocol = forward_protocol
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the DDoS protection instance to be queried.
        # 
        # > You can call [DescribeInstances](https://help.aliyun.com/document_detail/91478.html) to query all DDoS protection instance IDs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # In paginated queries, specifies which page of data to return. The minimum value is **1**, indicating the first page of data.
        # 
        # This parameter is required.
        self.offset = offset
        # In paginated queries, specifies the number of results per page. The maximum value is **50**, indicating that each page can contain up to 50 results.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The source IP address of the request. You do not need to fill this in; it is automatically obtained by the system.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forward_protocol is not None:
            result['ForwardProtocol'] = self.forward_protocol
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardProtocol') is not None:
            self.forward_protocol = m.get('ForwardProtocol')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeLayer4RulesResponseBodyListenersUsTimeout(TeaModel):
    def __init__(
        self,
        connect_timeout: int = None,
        rs_timeout: int = None,
    ):
        self.connect_timeout = connect_timeout
        self.rs_timeout = rs_timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout
        if self.rs_timeout is not None:
            result['RsTimeout'] = self.rs_timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')
        if m.get('RsTimeout') is not None:
            self.rs_timeout = m.get('RsTimeout')
        return self


class DescribeLayer4RulesResponseBodyListeners(TeaModel):
    def __init__(
        self,
        backend_port: int = None,
        bak_mode: int = None,
        current_index: int = None,
        eip: str = None,
        frontend_port: int = None,
        instance_id: str = None,
        is_auto_create: bool = None,
        payload_rule_enable: int = None,
        protocol: str = None,
        proxy_enable: int = None,
        proxy_status: str = None,
        real_servers: List[str] = None,
        remark: str = None,
        us_timeout: DescribeLayer4RulesResponseBodyListenersUsTimeout = None,
    ):
        # The origin server port.
        self.backend_port = backend_port
        # The origin mode. Values:
        # 
        # - **0**: Indicates the default origin mode.
        # - **1**: Indicates the primary/backup origin mode.
        self.bak_mode = bak_mode
        # The currently effective origin server type. Values:
        # 
        # - **1**: Indicates that the primary origin server settings are in effect (DDoS protection forwards business traffic to the primary origin server IP address).
        # - **2**: Indicates that the backup origin server settings are in effect (DDoS protection forwards business traffic to the backup origin server IP address).
        self.current_index = current_index
        # The IP address of the DDoS protection instance.
        self.eip = eip
        # The forwarding port.
        self.frontend_port = frontend_port
        # The ID of the DDoS protection instance.
        self.instance_id = instance_id
        # Indicates whether the rule was automatically created. Values:
        # 
        # - **true**: Indicates that the rule was automatically created by DDoS protection.
        # - **false**: Indicates that the rule was manually created by you.
        self.is_auto_create = is_auto_create
        # Payload rule module switch. Values:
        # 
        # - 1: Enabled
        # - 0: Disabled
        self.payload_rule_enable = payload_rule_enable
        # The type of forwarding protocol.
        self.protocol = protocol
        # Traffic diversion switch. Values:
        # - **0** Off.
        # - **1** On.
        self.proxy_enable = proxy_enable
        # Traffic diversion status. Values:
        # 
        # - on: Diversion is effective
        # - off: Diversion is ineffective
        self.proxy_status = proxy_status
        # The list of origin server IP addresses.
        self.real_servers = real_servers
        # The remarks for the port forwarding rule.
        self.remark = remark
        self.us_timeout = us_timeout

    def validate(self):
        if self.us_timeout:
            self.us_timeout.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backend_port is not None:
            result['BackendPort'] = self.backend_port
        if self.bak_mode is not None:
            result['BakMode'] = self.bak_mode
        if self.current_index is not None:
            result['CurrentIndex'] = self.current_index
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_auto_create is not None:
            result['IsAutoCreate'] = self.is_auto_create
        if self.payload_rule_enable is not None:
            result['PayloadRuleEnable'] = self.payload_rule_enable
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable
        if self.proxy_status is not None:
            result['ProxyStatus'] = self.proxy_status
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.us_timeout is not None:
            result['UsTimeout'] = self.us_timeout.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendPort') is not None:
            self.backend_port = m.get('BackendPort')
        if m.get('BakMode') is not None:
            self.bak_mode = m.get('BakMode')
        if m.get('CurrentIndex') is not None:
            self.current_index = m.get('CurrentIndex')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsAutoCreate') is not None:
            self.is_auto_create = m.get('IsAutoCreate')
        if m.get('PayloadRuleEnable') is not None:
            self.payload_rule_enable = m.get('PayloadRuleEnable')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')
        if m.get('ProxyStatus') is not None:
            self.proxy_status = m.get('ProxyStatus')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UsTimeout') is not None:
            temp_model = DescribeLayer4RulesResponseBodyListenersUsTimeout()
            self.us_timeout = temp_model.from_map(m['UsTimeout'])
        return self


class DescribeLayer4RulesResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[DescribeLayer4RulesResponseBodyListeners] = None,
        request_id: str = None,
        total: int = None,
    ):
        # Detailed configuration of port forwarding rules, including the forwarding port, forwarding protocol, and origin server addresses, etc.
        self.listeners = listeners
        # The ID of the current request.
        self.request_id = request_id
        # The number of returned results.
        self.total = total

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = DescribeLayer4RulesResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeLayer4RulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLayer4RulesResponseBody = None,
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
            temp_model = DescribeLayer4RulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLayer7CCRulesRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        offset: int = None,
        page_size: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.offset = offset
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeLayer7CCRulesResponseBodyLayer7CCRules(TeaModel):
    def __init__(
        self,
        act: str = None,
        count: int = None,
        interval: int = None,
        mode: str = None,
        name: str = None,
        ttl: int = None,
        uri: str = None,
    ):
        self.act = act
        self.count = count
        self.interval = interval
        self.mode = mode
        self.name = name
        self.ttl = ttl
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.act is not None:
            result['Act'] = self.act
        if self.count is not None:
            result['Count'] = self.count
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.name is not None:
            result['Name'] = self.name
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeLayer7CCRulesResponseBody(TeaModel):
    def __init__(
        self,
        layer_7ccrules: List[DescribeLayer7CCRulesResponseBodyLayer7CCRules] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.layer_7ccrules = layer_7ccrules
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.layer_7ccrules:
            for k in self.layer_7ccrules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layer7CCRules'] = []
        if self.layer_7ccrules is not None:
            for k in self.layer_7ccrules:
                result['Layer7CCRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7ccrules = []
        if m.get('Layer7CCRules') is not None:
            for k in m.get('Layer7CCRules'):
                temp_model = DescribeLayer7CCRulesResponseBodyLayer7CCRules()
                self.layer_7ccrules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeLayer7CCRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLayer7CCRulesResponseBody = None,
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
            temp_model = DescribeLayer7CCRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogStoreExistStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeLogStoreExistStatusResponseBody(TeaModel):
    def __init__(
        self,
        exist_status: bool = None,
        request_id: str = None,
    ):
        self.exist_status = exist_status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeLogStoreExistStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogStoreExistStatusResponseBody = None,
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
            temp_model = DescribeLogStoreExistStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        entity_object: str = None,
        entity_type: int = None,
        op_action: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_ip: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        self.entity_object = entity_object
        self.entity_type = entity_type
        self.op_action = op_action
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(
        self,
        entity_object: str = None,
        entity_type: int = None,
        gmt_create: int = None,
        op_account: str = None,
        op_action: int = None,
        op_desc: str = None,
    ):
        self.entity_object = entity_object
        self.entity_type = entity_type
        self.gmt_create = gmt_create
        self.op_account = op_account
        self.op_action = op_action
        self.op_desc = op_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        op_entities: List[DescribeOpEntitiesResponseBodyOpEntities] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.op_entities = op_entities
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpEntitiesResponseBody = None,
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
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSimpleDomainsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.instance_ids = instance_ids
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSimpleDomainsResponseBody(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        request_id: str = None,
    ):
        self.domain_list = domain_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSimpleDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSimpleDomainsResponseBody = None,
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
            temp_model = DescribeSimpleDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsAuthStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSlsAuthStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_auth_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_auth_status = sls_auth_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_auth_status is not None:
            result['SlsAuthStatus'] = self.sls_auth_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsAuthStatus') is not None:
            self.sls_auth_status = m.get('SlsAuthStatus')
        return self


class DescribeSlsAuthStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlsAuthStatusResponseBody = None,
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
            temp_model = DescribeSlsAuthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsEmptyCountRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSlsEmptyCountResponseBody(TeaModel):
    def __init__(
        self,
        available_count: int = None,
        request_id: str = None,
    ):
        self.available_count = available_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_count is not None:
            result['AvailableCount'] = self.available_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCount') is not None:
            self.available_count = m.get('AvailableCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSlsEmptyCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlsEmptyCountResponseBody = None,
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
            temp_model = DescribeSlsEmptyCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsLogstoreInfoRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSlsLogstoreInfoResponseBody(TeaModel):
    def __init__(
        self,
        log_store: str = None,
        project: str = None,
        quota: int = None,
        request_id: str = None,
        ttl: int = None,
        used: int = None,
    ):
        self.log_store = log_store
        self.project = project
        self.quota = quota
        self.request_id = request_id
        self.ttl = ttl
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project is not None:
            result['Project'] = self.project
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class DescribeSlsLogstoreInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlsLogstoreInfoResponseBody = None,
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
            temp_model = DescribeSlsLogstoreInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlsOpenStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSlsOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sls_open_status: bool = None,
    ):
        self.request_id = request_id
        self.sls_open_status = sls_open_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sls_open_status is not None:
            result['SlsOpenStatus'] = self.sls_open_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlsOpenStatus') is not None:
            self.sls_open_status = m.get('SlsOpenStatus')
        return self


class DescribeSlsOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlsOpenStatusResponseBody = None,
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
            temp_model = DescribeSlsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribleCertListRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribleCertListResponseBodyCertList(TeaModel):
    def __init__(
        self,
        cert_identifier: str = None,
        common: str = None,
        domain_related: bool = None,
        end_date: str = None,
        id: int = None,
        issuer: str = None,
        name: str = None,
        start_date: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.common = common
        self.domain_related = domain_related
        self.end_date = end_date
        self.id = id
        self.issuer = issuer
        self.name = name
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier
        if self.common is not None:
            result['Common'] = self.common
        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.id is not None:
            result['Id'] = self.id
        if self.issuer is not None:
            result['Issuer'] = self.issuer
        if self.name is not None:
            result['Name'] = self.name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')
        if m.get('Common') is not None:
            self.common = m.get('Common')
        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribleCertListResponseBody(TeaModel):
    def __init__(
        self,
        cert_list: List[DescribleCertListResponseBodyCertList] = None,
        request_id: str = None,
    ):
        self.cert_list = cert_list
        self.request_id = request_id

    def validate(self):
        if self.cert_list:
            for k in self.cert_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CertList'] = []
        if self.cert_list is not None:
            for k in self.cert_list:
                result['CertList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k in m.get('CertList'):
                temp_model = DescribleCertListResponseBodyCertList()
                self.cert_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribleCertListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribleCertListResponseBody = None,
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
            temp_model = DescribleCertListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribleLayer7InstanceRelationsRequest(TeaModel):
    def __init__(
        self,
        domain_list: List[str] = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain_list = domain_list
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails(TeaModel):
    def __init__(
        self,
        eip_list: List[str] = None,
        function_version: str = None,
        instance_id: str = None,
        ip_mode: str = None,
        ip_version: str = None,
    ):
        self.eip_list = eip_list
        self.function_version = function_version
        self.instance_id = instance_id
        self.ip_mode = ip_mode
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_list is not None:
            result['EipList'] = self.eip_list
        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_mode is not None:
            result['IpMode'] = self.ip_mode
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipList') is not None:
            self.eip_list = m.get('EipList')
        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpMode') is not None:
            self.ip_mode = m.get('IpMode')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations(TeaModel):
    def __init__(
        self,
        domain: str = None,
        instance_details: List[DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails] = None,
    ):
        self.domain = domain
        self.instance_details = instance_details

    def validate(self):
        if self.instance_details:
            for k in self.instance_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        result['InstanceDetails'] = []
        if self.instance_details is not None:
            for k in self.instance_details:
                result['InstanceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.instance_details = []
        if m.get('InstanceDetails') is not None:
            for k in m.get('InstanceDetails'):
                temp_model = DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelationsInstanceDetails()
                self.instance_details.append(temp_model.from_map(k))
        return self


class DescribleLayer7InstanceRelationsResponseBody(TeaModel):
    def __init__(
        self,
        layer_7instance_relations: List[DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations] = None,
        request_id: str = None,
    ):
        self.layer_7instance_relations = layer_7instance_relations
        self.request_id = request_id

    def validate(self):
        if self.layer_7instance_relations:
            for k in self.layer_7instance_relations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layer7InstanceRelations'] = []
        if self.layer_7instance_relations is not None:
            for k in self.layer_7instance_relations:
                result['Layer7InstanceRelations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7instance_relations = []
        if m.get('Layer7InstanceRelations') is not None:
            for k in m.get('Layer7InstanceRelations'):
                temp_model = DescribleLayer7InstanceRelationsResponseBodyLayer7InstanceRelations()
                self.layer_7instance_relations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribleLayer7InstanceRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribleLayer7InstanceRelationsResponseBody = None,
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
            temp_model = DescribleLayer7InstanceRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLayer7CCRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DisableLayer7CCResponseBody(TeaModel):
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


class DisableLayer7CCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableLayer7CCResponseBody = None,
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
            temp_model = DisableLayer7CCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DisableLayer7CCRuleResponseBody(TeaModel):
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


class DisableLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableLayer7CCRuleResponseBody = None,
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
            temp_model = DisableLayer7CCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EmptySlsLogstoreRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class EmptySlsLogstoreResponseBody(TeaModel):
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


class EmptySlsLogstoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EmptySlsLogstoreResponseBody = None,
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
            temp_model = EmptySlsLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLayer7CCRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class EnableLayer7CCResponseBody(TeaModel):
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


class EnableLayer7CCResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableLayer7CCResponseBody = None,
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
            temp_model = EnableLayer7CCResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLayer7CCRuleRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class EnableLayer7CCRuleResponseBody(TeaModel):
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


class EnableLayer7CCRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableLayer7CCRuleResponseBody = None,
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
            temp_model = EnableLayer7CCRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.resource_group_id = resource_group_id
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ListAsyncTaskResponseBodyAsyncTasks(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        task_id: int = None,
        task_params: str = None,
        task_result: str = None,
        task_status: int = None,
        task_type: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.task_id = task_id
        self.task_params = task_params
        self.task_result = task_result
        self.task_status = task_status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        async_tasks: List[ListAsyncTaskResponseBodyAsyncTasks] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.async_tasks = async_tasks
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.async_tasks:
            for k in self.async_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AsyncTasks'] = []
        if self.async_tasks is not None:
            for k in self.async_tasks:
                result['AsyncTasks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.async_tasks = []
        if m.get('AsyncTasks') is not None:
            for k in m.get('AsyncTasks'):
                temp_model = ListAsyncTaskResponseBodyAsyncTasks()
                self.async_tasks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsyncTaskResponseBody = None,
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
            temp_model = ListAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLayer7CustomPortsRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ListLayer7CustomPortsResponseBodyLayer7CustomPorts(TeaModel):
    def __init__(
        self,
        flag: str = None,
        proxy_ports: List[str] = None,
        proxy_type: str = None,
    ):
        self.flag = flag
        self.proxy_ports = proxy_ports
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.proxy_ports is not None:
            result['ProxyPorts'] = self.proxy_ports
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ProxyPorts') is not None:
            self.proxy_ports = m.get('ProxyPorts')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class ListLayer7CustomPortsResponseBody(TeaModel):
    def __init__(
        self,
        layer_7custom_ports: List[ListLayer7CustomPortsResponseBodyLayer7CustomPorts] = None,
        request_id: str = None,
    ):
        self.layer_7custom_ports = layer_7custom_ports
        self.request_id = request_id

    def validate(self):
        if self.layer_7custom_ports:
            for k in self.layer_7custom_ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Layer7CustomPorts'] = []
        if self.layer_7custom_ports is not None:
            for k in self.layer_7custom_ports:
                result['Layer7CustomPorts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.layer_7custom_ports = []
        if m.get('Layer7CustomPorts') is not None:
            for k in m.get('Layer7CustomPorts'):
                temp_model = ListLayer7CustomPortsResponseBodyLayer7CustomPorts()
                self.layer_7custom_ports.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLayer7CustomPortsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLayer7CustomPortsResponseBody = None,
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
            temp_model = ListLayer7CustomPortsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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
        page_size: int = None,
        request_id: str = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.tag_keys = tag_keys
        self.total_count = total_count

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
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
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
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListValueAddedRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ListValueAddedResponseBodyValueAddedList(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        gmt_create: int = None,
        instance_id: str = None,
        log_size: int = None,
        status: int = None,
        store_region: str = None,
    ):
        self.expire_time = expire_time
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.log_size = log_size
        self.status = status
        self.store_region = store_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.log_size is not None:
            result['LogSize'] = self.log_size
        if self.status is not None:
            result['Status'] = self.status
        if self.store_region is not None:
            result['StoreRegion'] = self.store_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LogSize') is not None:
            self.log_size = m.get('LogSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoreRegion') is not None:
            self.store_region = m.get('StoreRegion')
        return self


class ListValueAddedResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        value_added_list: List[ListValueAddedResponseBodyValueAddedList] = None,
    ):
        self.request_id = request_id
        self.value_added_list = value_added_list

    def validate(self):
        if self.value_added_list:
            for k in self.value_added_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ValueAddedList'] = []
        if self.value_added_list is not None:
            for k in self.value_added_list:
                result['ValueAddedList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.value_added_list = []
        if m.get('ValueAddedList') is not None:
            for k in m.get('ValueAddedList'):
                temp_model = ListValueAddedResponseBodyValueAddedList()
                self.value_added_list.append(temp_model.from_map(k))
        return self


class ListValueAddedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListValueAddedResponseBody = None,
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
            temp_model = ListValueAddedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBandWidthRequest(TeaModel):
    def __init__(
        self,
        elastic_bandwidth: int = None,
        instance_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.elastic_bandwidth = elastic_bandwidth
        # This parameter is required.
        self.instance_id = instance_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyElasticBandWidthResponseBody(TeaModel):
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


class ModifyElasticBandWidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyElasticBandWidthResponseBody = None,
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
            temp_model = ModifyElasticBandWidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFullLogTtlRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
        ttl: int = None,
    ):
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip
        # This parameter is required.
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.ttl is not None:
            result['Ttl'] = self.ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')
        return self


class ModifyFullLogTtlResponseBody(TeaModel):
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


class ModifyFullLogTtlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyFullLogTtlResponseBody = None,
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
            temp_model = ModifyFullLogTtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        remark: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.remark = remark
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ModifyInstanceRemarkResponseBody(TeaModel):
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


class ModifyInstanceRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceRemarkResponseBody = None,
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
            temp_model = ModifyInstanceRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDomainSlsConfigRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        lang: str = None,
        resource_group_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.domain = domain
        self.lang = lang
        self.resource_group_id = resource_group_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class OpenDomainSlsConfigResponseBody(TeaModel):
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


class OpenDomainSlsConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenDomainSlsConfigResponseBody = None,
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
            temp_model = OpenDomainSlsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ReleaseInstanceResponseBody(TeaModel):
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


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstanceResponseBody = None,
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseValueAddedRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source_ip: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class ReleaseValueAddedResponseBody(TeaModel):
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


class ReleaseValueAddedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseValueAddedResponseBody = None,
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
            temp_model = ReleaseValueAddedResponseBody()
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
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


