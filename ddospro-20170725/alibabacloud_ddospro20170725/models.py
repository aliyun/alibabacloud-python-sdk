# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ConfigSwitchPriorityRequestConfig(TeaModel):
    def __init__(
        self,
        ip: str = None,
        priority: int = None,
    ):
        self.ip = ip
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.priority is not None:
            result['Priority'] = self.priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        return self


class ConfigSwitchPriorityRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        config: List[ConfigSwitchPriorityRequestConfig] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.config = config

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = ConfigSwitchPriorityRequestConfig()
                self.config.append(temp_model.from_map(k))
        return self


class ConfigSwitchPriorityResponseBody(TeaModel):
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


class ConfigSwitchPriorityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigSwitchPriorityResponseBody = None,
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
            temp_model = ConfigSwitchPriorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCcCustomedRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        matching_rule: str = None,
        domain: str = None,
        visit_count: int = None,
        name: str = None,
        blocking_type: str = None,
        interval: int = None,
        blocking_time: int = None,
        uri: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.matching_rule = matching_rule
        self.domain = domain
        self.visit_count = visit_count
        self.name = name
        self.blocking_type = blocking_type
        self.interval = interval
        self.blocking_time = blocking_time
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.matching_rule is not None:
            result['MatchingRule'] = self.matching_rule
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.visit_count is not None:
            result['VisitCount'] = self.visit_count
        if self.name is not None:
            result['Name'] = self.name
        if self.blocking_type is not None:
            result['BlockingType'] = self.blocking_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.blocking_time is not None:
            result['BlockingTime'] = self.blocking_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchingRule') is not None:
            self.matching_rule = m.get('MatchingRule')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('VisitCount') is not None:
            self.visit_count = m.get('VisitCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BlockingType') is not None:
            self.blocking_type = m.get('BlockingType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('BlockingTime') is not None:
            self.blocking_time = m.get('BlockingTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class CreateCcCustomedRuleResponseBody(TeaModel):
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


class CreateCcCustomedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCcCustomedRuleResponseBody = None,
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
            temp_model = CreateCcCustomedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        ip: str = None,
        type: str = None,
        cc_enable: bool = None,
        real_server: List[str] = None,
        proxy_type: List[str] = None,
        ips: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.ip = ip
        self.type = type
        self.cc_enable = cc_enable
        self.real_server = real_server
        self.proxy_type = proxy_type
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.type is not None:
            result['Type'] = self.type
        if self.cc_enable is not None:
            result['CcEnable'] = self.cc_enable
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CcEnable') is not None:
            self.cc_enable = m.get('CcEnable')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class CreateDomainResponseBody(TeaModel):
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


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDomainResponseBody = None,
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
            temp_model = CreateDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePortRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        front_port: int = None,
        back_port: int = None,
        proxy_type: str = None,
        real_server_list: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.front_port = front_port
        self.back_port = back_port
        self.proxy_type = proxy_type
        self.real_server_list = real_server_list
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        if self.real_server_list is not None:
            result['RealServerList'] = self.real_server_list
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        if m.get('RealServerList') is not None:
            self.real_server_list = m.get('RealServerList')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class CreatePortRuleResponseBody(TeaModel):
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


class CreatePortRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePortRuleResponseBody = None,
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
            temp_model = CreatePortRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransmitLineRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
        domain: str = None,
        ips: List[str] = None,
        real_servers: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type
        self.domain = domain
        self.ips = ips
        self.real_servers = real_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class CreateTransmitLineResponseBody(TeaModel):
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


class CreateTransmitLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTransmitLineResponseBody = None,
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
            temp_model = CreateTransmitLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCcCustomedRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        name: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DeleteCcCustomedRuleResponseBody(TeaModel):
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


class DeleteCcCustomedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCcCustomedRuleResponseBody = None,
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
            temp_model = DeleteCcCustomedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteDomainResponseBody(TeaModel):
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


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDomainResponseBody = None,
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
            temp_model = DeleteDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePortRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        front_port: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.front_port = front_port
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DeletePortRuleResponseBody(TeaModel):
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


class DeletePortRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePortRuleResponseBody = None,
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
            temp_model = DeletePortRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTransmitLineRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        line: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.line = line
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line is not None:
            result['Line'] = self.line
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteTransmitLineResponseBody(TeaModel):
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


class DeleteTransmitLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTransmitLineResponseBody = None,
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
            temp_model = DeleteTransmitLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackSourceCidrRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        line: str = None,
        region: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.line = line
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.line is not None:
            result['Line'] = self.line
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeBackSourceCidrResponseBodyCidrList(TeaModel):
    def __init__(
        self,
        cidr: List[str] = None,
    ):
        self.cidr = cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cidr is not None:
            result['Cidr'] = self.cidr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')
        return self


class DescribeBackSourceCidrResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cidr_list: DescribeBackSourceCidrResponseBodyCidrList = None,
    ):
        self.request_id = request_id
        self.cidr_list = cidr_list

    def validate(self):
        if self.cidr_list:
            self.cidr_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cidr_list is not None:
            result['CidrList'] = self.cidr_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CidrList') is not None:
            temp_model = DescribeBackSourceCidrResponseBodyCidrList()
            self.cidr_list = temp_model.from_map(m['CidrList'])
        return self


class DescribeBackSourceCidrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackSourceCidrResponseBody = None,
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
            temp_model = DescribeBackSourceCidrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeBizFlowResponseBodyDataTimeScope(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        interval: int = None,
    ):
        self.start_time = start_time
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeBizFlowResponseBodyData(TeaModel):
    def __init__(
        self,
        in_kbps: List[str] = None,
        out_kbps: List[str] = None,
        time_scope: DescribeBizFlowResponseBodyDataTimeScope = None,
    ):
        self.in_kbps = in_kbps
        self.out_kbps = out_kbps
        self.time_scope = time_scope

    def validate(self):
        if self.time_scope:
            self.time_scope.validate()

    def to_map(self):
        result = dict()
        if self.in_kbps is not None:
            result['InKbps'] = self.in_kbps
        if self.out_kbps is not None:
            result['OutKbps'] = self.out_kbps
        if self.time_scope is not None:
            result['TimeScope'] = self.time_scope.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InKbps') is not None:
            self.in_kbps = m.get('InKbps')
        if m.get('OutKbps') is not None:
            self.out_kbps = m.get('OutKbps')
        if m.get('TimeScope') is not None:
            temp_model = DescribeBizFlowResponseBodyDataTimeScope()
            self.time_scope = temp_model.from_map(m['TimeScope'])
        return self


class DescribeBizFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeBizFlowResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeBizFlowResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeBizFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBizFlowResponseBody = None,
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
            temp_model = DescribeBizFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCcEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        domain: str = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.domain = domain
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class DescribeCcEventsResponseBodyEventList(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        domain: str = None,
        attack_finished: bool = None,
        max_qps: int = None,
        duration: int = None,
        blocked_count: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.domain = domain
        self.attack_finished = attack_finished
        self.max_qps = max_qps
        self.duration = duration
        self.blocked_count = blocked_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.attack_finished is not None:
            result['AttackFinished'] = self.attack_finished
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.blocked_count is not None:
            result['BlockedCount'] = self.blocked_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('AttackFinished') is not None:
            self.attack_finished = m.get('AttackFinished')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('BlockedCount') is not None:
            self.blocked_count = m.get('BlockedCount')
        return self


class DescribeCcEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        event_list: List[DescribeCcEventsResponseBodyEventList] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.event_list = event_list
        self.total = total

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeCcEventsResponseBodyEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCcEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCcEventsResponseBody = None,
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
            temp_model = DescribeCcEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCnameAutoStatusRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
        domain: str = None,
    ):
        self.resource_owner_id = resource_owner_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeCnameAutoStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: bool = None,
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


class DescribeCnameAutoStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCnameAutoStatusResponseBody = None,
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
            temp_model = DescribeCnameAutoStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosAttackEventsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeDdosAttackEventsResponseBodyDataEventList(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        attack_type: str = None,
        result: int = None,
        duration: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.attack_type = attack_type
        self.result = result
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.result is not None:
            result['Result'] = self.result
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class DescribeDdosAttackEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        event_list: List[DescribeDdosAttackEventsResponseBodyDataEventList] = None,
        total_count: int = None,
    ):
        self.event_list = event_list
        self.total_count = total_count

    def validate(self):
        if self.event_list:
            for k in self.event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EventList'] = []
        if self.event_list is not None:
            for k in self.event_list:
                result['EventList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_list = []
        if m.get('EventList') is not None:
            for k in m.get('EventList'):
                temp_model = DescribeDdosAttackEventsResponseBodyDataEventList()
                self.event_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDdosAttackEventsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDdosAttackEventsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDdosAttackEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDdosAttackEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosAttackEventsResponseBody = None,
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
            temp_model = DescribeDdosAttackEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosAttackEventSourceIpsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeDdosAttackEventSourceIpsResponseBodyDataIpList(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        in_bps: int = None,
        city: str = None,
    ):
        self.source_ip = source_ip
        self.in_bps = in_bps
        self.city = city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.in_bps is not None:
            result['InBps'] = self.in_bps
        if self.city is not None:
            result['City'] = self.city
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')
        if m.get('City') is not None:
            self.city = m.get('City')
        return self


class DescribeDdosAttackEventSourceIpsResponseBodyData(TeaModel):
    def __init__(
        self,
        ip_list: List[DescribeDdosAttackEventSourceIpsResponseBodyDataIpList] = None,
        total_count: int = None,
    ):
        self.ip_list = ip_list
        self.total_count = total_count

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribeDdosAttackEventSourceIpsResponseBodyDataIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDdosAttackEventSourceIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeDdosAttackEventSourceIpsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeDdosAttackEventSourceIpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeDdosAttackEventSourceIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosAttackEventSourceIpsResponseBody = None,
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
            temp_model = DescribeDdosAttackEventSourceIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosAttackTypeChartRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDdosAttackTypeChartResponseBody(TeaModel):
    def __init__(
        self,
        attck_count: int = None,
        request_id: str = None,
        attck_type: str = None,
        drop_count: int = None,
        drop_type: str = None,
    ):
        self.attck_count = attck_count
        self.request_id = request_id
        self.attck_type = attck_type
        self.drop_count = drop_count
        self.drop_type = drop_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.attck_count is not None:
            result['AttckCount'] = self.attck_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.attck_type is not None:
            result['AttckType'] = self.attck_type
        if self.drop_count is not None:
            result['DropCount'] = self.drop_count
        if self.drop_type is not None:
            result['DropType'] = self.drop_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttckCount') is not None:
            self.attck_count = m.get('AttckCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AttckType') is not None:
            self.attck_type = m.get('AttckType')
        if m.get('DropCount') is not None:
            self.drop_count = m.get('DropCount')
        if m.get('DropType') is not None:
            self.drop_type = m.get('DropType')
        return self


class DescribeDdosAttackTypeChartResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosAttackTypeChartResponseBody = None,
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
            temp_model = DescribeDdosAttackTypeChartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosFlowProportionDiagramRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDdosFlowProportionDiagramResponseBody(TeaModel):
    def __init__(
        self,
        total_bps: int = None,
        request_id: str = None,
        drop_pps: int = None,
        drop_bps: int = None,
        total_pps: int = None,
    ):
        self.total_bps = total_bps
        self.request_id = request_id
        self.drop_pps = drop_pps
        self.drop_bps = drop_bps
        self.total_pps = total_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.drop_pps is not None:
            result['DropPps'] = self.drop_pps
        if self.drop_bps is not None:
            result['DropBps'] = self.drop_bps
        if self.total_pps is not None:
            result['TotalPps'] = self.total_pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DropPps') is not None:
            self.drop_pps = m.get('DropPps')
        if m.get('DropBps') is not None:
            self.drop_bps = m.get('DropBps')
        if m.get('TotalPps') is not None:
            self.total_pps = m.get('TotalPps')
        return self


class DescribeDdosFlowProportionDiagramResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosFlowProportionDiagramResponseBody = None,
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
            temp_model = DescribeDdosFlowProportionDiagramResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosIpConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        index: int = None,
        page_size: int = None,
        ips: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.index = index
        self.page_size = page_size
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.index is not None:
            result['Index'] = self.index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class DescribeDdosIpConfigResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        clean_status: int = None,
        bandwidth: int = None,
        config_domain_count: int = None,
        line: str = None,
        elastic_bandwidth: int = None,
        lb_id: str = None,
        config_port_count: int = None,
        ip: str = None,
        total_defense_count: int = None,
    ):
        self.status = status
        self.clean_status = clean_status
        self.bandwidth = bandwidth
        self.config_domain_count = config_domain_count
        self.line = line
        self.elastic_bandwidth = elastic_bandwidth
        self.lb_id = lb_id
        self.config_port_count = config_port_count
        self.ip = ip
        self.total_defense_count = total_defense_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.clean_status is not None:
            result['CleanStatus'] = self.clean_status
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.config_domain_count is not None:
            result['ConfigDomainCount'] = self.config_domain_count
        if self.line is not None:
            result['Line'] = self.line
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.lb_id is not None:
            result['LbId'] = self.lb_id
        if self.config_port_count is not None:
            result['ConfigPortCount'] = self.config_port_count
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.total_defense_count is not None:
            result['TotalDefenseCount'] = self.total_defense_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CleanStatus') is not None:
            self.clean_status = m.get('CleanStatus')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConfigDomainCount') is not None:
            self.config_domain_count = m.get('ConfigDomainCount')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('LbId') is not None:
            self.lb_id = m.get('LbId')
        if m.get('ConfigPortCount') is not None:
            self.config_port_count = m.get('ConfigPortCount')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('TotalDefenseCount') is not None:
            self.total_defense_count = m.get('TotalDefenseCount')
        return self


class DescribeDdosIpConfigResponseBody(TeaModel):
    def __init__(
        self,
        data_list: List[DescribeDdosIpConfigResponseBodyDataList] = None,
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
                temp_model = DescribeDdosIpConfigResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosIpConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosIpConfigResponseBody = None,
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
            temp_model = DescribeDdosIpConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosPeakFlowRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        start_time: int = None,
        end_time: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDdosPeakFlowResponseBody(TeaModel):
    def __init__(
        self,
        peak_flow: str = None,
        request_id: str = None,
    ):
        self.peak_flow = peak_flow
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.peak_flow is not None:
            result['PeakFlow'] = self.peak_flow
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakFlow') is not None:
            self.peak_flow = m.get('PeakFlow')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDdosPeakFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosPeakFlowResponseBody = None,
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
            temp_model = DescribeDdosPeakFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainConfigPageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class DescribeDomainConfigPageResponseBodyConfigListInstancesRules(TeaModel):
    def __init__(
        self,
        proxy_type_list: List[str] = None,
        line: str = None,
        real_servers: List[str] = None,
        ip: str = None,
    ):
        self.proxy_type_list = proxy_type_list
        self.line = line
        self.real_servers = real_servers
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_type_list is not None:
            result['ProxyTypeList'] = self.proxy_type_list
        if self.line is not None:
            result['Line'] = self.line
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyTypeList') is not None:
            self.proxy_type_list = m.get('ProxyTypeList')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDomainConfigPageResponseBodyConfigListInstances(TeaModel):
    def __init__(
        self,
        instance_remark: str = None,
        instance_id: str = None,
        rules: List[DescribeDomainConfigPageResponseBodyConfigListInstancesRules] = None,
    ):
        self.instance_remark = instance_remark
        self.instance_id = instance_id
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_remark is not None:
            result['InstanceRemark'] = self.instance_remark
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRemark') is not None:
            self.instance_remark = m.get('InstanceRemark')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeDomainConfigPageResponseBodyConfigListInstancesRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeDomainConfigPageResponseBodyConfigList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        cname: str = None,
        instances: List[DescribeDomainConfigPageResponseBodyConfigListInstances] = None,
    ):
        self.domain = domain
        self.cname = cname
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeDomainConfigPageResponseBodyConfigListInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeDomainConfigPageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        config_list: List[DescribeDomainConfigPageResponseBodyConfigList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = DescribeDomainConfigPageResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class DescribeDomainConfigPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainConfigPageResponseBody = None,
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
            temp_model = DescribeDomainConfigPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDomainSecurityConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DescribeDomainSecurityConfigResponseBodyCcInfo(TeaModel):
    def __init__(
        self,
        cc_custom_rule_count: int = None,
        cc_switch: bool = None,
        cc_template: str = None,
        cc_custom_rule_enable: bool = None,
    ):
        self.cc_custom_rule_count = cc_custom_rule_count
        self.cc_switch = cc_switch
        self.cc_template = cc_template
        self.cc_custom_rule_enable = cc_custom_rule_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cc_custom_rule_count is not None:
            result['CcCustomRuleCount'] = self.cc_custom_rule_count
        if self.cc_switch is not None:
            result['CcSwitch'] = self.cc_switch
        if self.cc_template is not None:
            result['CcTemplate'] = self.cc_template
        if self.cc_custom_rule_enable is not None:
            result['CcCustomRuleEnable'] = self.cc_custom_rule_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcCustomRuleCount') is not None:
            self.cc_custom_rule_count = m.get('CcCustomRuleCount')
        if m.get('CcSwitch') is not None:
            self.cc_switch = m.get('CcSwitch')
        if m.get('CcTemplate') is not None:
            self.cc_template = m.get('CcTemplate')
        if m.get('CcCustomRuleEnable') is not None:
            self.cc_custom_rule_enable = m.get('CcCustomRuleEnable')
        return self


class DescribeDomainSecurityConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cc_info: DescribeDomainSecurityConfigResponseBodyCcInfo = None,
        cname_enable: bool = None,
        white_list: str = None,
        black_list: str = None,
        cname_mode: int = None,
    ):
        self.request_id = request_id
        self.cc_info = cc_info
        self.cname_enable = cname_enable
        self.white_list = white_list
        self.black_list = black_list
        self.cname_mode = cname_mode

    def validate(self):
        if self.cc_info:
            self.cc_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cc_info is not None:
            result['CcInfo'] = self.cc_info.to_map()
        if self.cname_enable is not None:
            result['CnameEnable'] = self.cname_enable
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.cname_mode is not None:
            result['CnameMode'] = self.cname_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CcInfo') is not None:
            temp_model = DescribeDomainSecurityConfigResponseBodyCcInfo()
            self.cc_info = temp_model.from_map(m['CcInfo'])
        if m.get('CnameEnable') is not None:
            self.cname_enable = m.get('CnameEnable')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('CnameMode') is not None:
            self.cname_mode = m.get('CnameMode')
        return self


class DescribeDomainSecurityConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDomainSecurityConfigResponseBody = None,
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
            temp_model = DescribeDomainSecurityConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHealthCheckConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeHealthCheckConfigResponseBodyListenersCheck(TeaModel):
    def __init__(
        self,
        type: str = None,
        timeout: int = None,
        domain: str = None,
        interval: int = None,
        up: int = None,
        down: int = None,
        port: int = None,
        uri: str = None,
    ):
        self.type = type
        self.timeout = timeout
        self.domain = domain
        self.interval = interval
        self.up = up
        self.down = down
        self.port = port
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.up is not None:
            result['Up'] = self.up
        if self.down is not None:
            result['Down'] = self.down
        if self.port is not None:
            result['Port'] = self.port
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('Up') is not None:
            self.up = m.get('Up')
        if m.get('Down') is not None:
            self.down = m.get('Down')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeHealthCheckConfigResponseBodyListenersConfigSla(TeaModel):
    def __init__(
        self,
        cps_enable: int = None,
        cps: int = None,
        max_conn_enable: int = None,
        max_conn: int = None,
    ):
        self.cps_enable = cps_enable
        self.cps = cps
        self.max_conn_enable = max_conn_enable
        self.max_conn = max_conn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.max_conn_enable is not None:
            result['MaxConnEnable'] = self.max_conn_enable
        if self.max_conn is not None:
            result['MaxConn'] = self.max_conn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('MaxConnEnable') is not None:
            self.max_conn_enable = m.get('MaxConnEnable')
        if m.get('MaxConn') is not None:
            self.max_conn = m.get('MaxConn')
        return self


class DescribeHealthCheckConfigResponseBodyListenersConfigPayloadLength(TeaModel):
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


class DescribeHealthCheckConfigResponseBodyListenersConfigSlimit(TeaModel):
    def __init__(
        self,
        cps_enable: int = None,
        cps: int = None,
        max_conn_enable: int = None,
        max_conn: int = None,
    ):
        self.cps_enable = cps_enable
        self.cps = cps
        self.max_conn_enable = max_conn_enable
        self.max_conn = max_conn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cps_enable is not None:
            result['CpsEnable'] = self.cps_enable
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.max_conn_enable is not None:
            result['MaxConnEnable'] = self.max_conn_enable
        if self.max_conn is not None:
            result['MaxConn'] = self.max_conn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpsEnable') is not None:
            self.cps_enable = m.get('CpsEnable')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('MaxConnEnable') is not None:
            self.max_conn_enable = m.get('MaxConnEnable')
        if m.get('MaxConn') is not None:
            self.max_conn = m.get('MaxConn')
        return self


class DescribeHealthCheckConfigResponseBodyListenersConfig(TeaModel):
    def __init__(
        self,
        syn_proxy: str = None,
        persistence_timeout: int = None,
        no_data_conn: str = None,
        sla: DescribeHealthCheckConfigResponseBodyListenersConfigSla = None,
        payload_length: DescribeHealthCheckConfigResponseBodyListenersConfigPayloadLength = None,
        slimit: DescribeHealthCheckConfigResponseBodyListenersConfigSlimit = None,
    ):
        self.syn_proxy = syn_proxy
        self.persistence_timeout = persistence_timeout
        self.no_data_conn = no_data_conn
        self.sla = sla
        self.payload_length = payload_length
        self.slimit = slimit

    def validate(self):
        if self.sla:
            self.sla.validate()
        if self.payload_length:
            self.payload_length.validate()
        if self.slimit:
            self.slimit.validate()

    def to_map(self):
        result = dict()
        if self.syn_proxy is not None:
            result['SynProxy'] = self.syn_proxy
        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout
        if self.no_data_conn is not None:
            result['NoDataConn'] = self.no_data_conn
        if self.sla is not None:
            result['Sla'] = self.sla.to_map()
        if self.payload_length is not None:
            result['PayloadLength'] = self.payload_length.to_map()
        if self.slimit is not None:
            result['Slimit'] = self.slimit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynProxy') is not None:
            self.syn_proxy = m.get('SynProxy')
        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')
        if m.get('NoDataConn') is not None:
            self.no_data_conn = m.get('NoDataConn')
        if m.get('Sla') is not None:
            temp_model = DescribeHealthCheckConfigResponseBodyListenersConfigSla()
            self.sla = temp_model.from_map(m['Sla'])
        if m.get('PayloadLength') is not None:
            temp_model = DescribeHealthCheckConfigResponseBodyListenersConfigPayloadLength()
            self.payload_length = temp_model.from_map(m['PayloadLength'])
        if m.get('Slimit') is not None:
            temp_model = DescribeHealthCheckConfigResponseBodyListenersConfigSlimit()
            self.slimit = temp_model.from_map(m['Slimit'])
        return self


class DescribeHealthCheckConfigResponseBodyListeners(TeaModel):
    def __init__(
        self,
        frontend_port: int = None,
        check: DescribeHealthCheckConfigResponseBodyListenersCheck = None,
        protocol: str = None,
        back_port: int = None,
        config: DescribeHealthCheckConfigResponseBodyListenersConfig = None,
    ):
        self.frontend_port = frontend_port
        self.check = check
        self.protocol = protocol
        self.back_port = back_port
        self.config = config

    def validate(self):
        if self.check:
            self.check.validate()
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        if self.frontend_port is not None:
            result['FrontendPort'] = self.frontend_port
        if self.check is not None:
            result['Check'] = self.check.to_map()
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontendPort') is not None:
            self.frontend_port = m.get('FrontendPort')
        if m.get('Check') is not None:
            temp_model = DescribeHealthCheckConfigResponseBodyListenersCheck()
            self.check = temp_model.from_map(m['Check'])
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('Config') is not None:
            temp_model = DescribeHealthCheckConfigResponseBodyListenersConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class DescribeHealthCheckConfigResponseBody(TeaModel):
    def __init__(
        self,
        listeners: List[DescribeHealthCheckConfigResponseBodyListeners] = None,
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
                temp_model = DescribeHealthCheckConfigResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHealthCheckConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHealthCheckConfigResponseBody = None,
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
            temp_model = DescribeHealthCheckConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancePageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_size: int = None,
        current_page: int = None,
        instance_id: str = None,
        line: str = None,
        instance_id_list: List[str] = None,
        ip_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_size = page_size
        self.current_page = current_page
        self.instance_id = instance_id
        self.line = line
        self.instance_id_list = instance_id_list
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.line is not None:
            result['Line'] = self.line
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class DescribeInstancePageResponseBodyInstanceListIpList(TeaModel):
    def __init__(
        self,
        status: int = None,
        line: str = None,
        ip: str = None,
        instance_id: str = None,
        band_width: int = None,
        elastic_band_width: int = None,
    ):
        self.status = status
        self.line = line
        self.ip = ip
        self.instance_id = instance_id
        self.band_width = band_width
        self.elastic_band_width = elastic_band_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.line is not None:
            result['Line'] = self.line
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.band_width is not None:
            result['BandWidth'] = self.band_width
        if self.elastic_band_width is not None:
            result['ElasticBandWidth'] = self.elastic_band_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BandWidth') is not None:
            self.band_width = m.get('BandWidth')
        if m.get('ElasticBandWidth') is not None:
            self.elastic_band_width = m.get('ElasticBandWidth')
        return self


class DescribeInstancePageResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        instance_remark: str = None,
        ip_list: List[DescribeInstancePageResponseBodyInstanceListIpList] = None,
        instance_id: str = None,
    ):
        self.instance_remark = instance_remark
        self.ip_list = ip_list
        self.instance_id = instance_id

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_remark is not None:
            result['InstanceRemark'] = self.instance_remark
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRemark') is not None:
            self.instance_remark = m.get('InstanceRemark')
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribeInstancePageResponseBodyInstanceListIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstancePageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        instance_list: List[DescribeInstancePageResponseBodyInstanceList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstancePageResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeInstancePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancePageResponseBody = None,
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
            temp_model = DescribeInstancePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePortRulePageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        page_size: int = None,
        ip: str = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.page_size = page_size
        self.ip = ip
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribePortRulePageResponseBodyRuleList(TeaModel):
    def __init__(
        self,
        back_protocol: str = None,
        back_port: int = None,
        lb_id: str = None,
        ip: str = None,
        lvs_type: str = None,
        real_server: str = None,
        front_port: int = None,
        front_protocol: str = None,
    ):
        self.back_protocol = back_protocol
        self.back_port = back_port
        self.lb_id = lb_id
        self.ip = ip
        self.lvs_type = lvs_type
        self.real_server = real_server
        self.front_port = front_port
        self.front_protocol = front_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.back_protocol is not None:
            result['BackProtocol'] = self.back_protocol
        if self.back_port is not None:
            result['BackPort'] = self.back_port
        if self.lb_id is not None:
            result['LbId'] = self.lb_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lvs_type is not None:
            result['LvsType'] = self.lvs_type
        if self.real_server is not None:
            result['RealServer'] = self.real_server
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.front_protocol is not None:
            result['FrontProtocol'] = self.front_protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackProtocol') is not None:
            self.back_protocol = m.get('BackProtocol')
        if m.get('BackPort') is not None:
            self.back_port = m.get('BackPort')
        if m.get('LbId') is not None:
            self.lb_id = m.get('LbId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('LvsType') is not None:
            self.lvs_type = m.get('LvsType')
        if m.get('RealServer') is not None:
            self.real_server = m.get('RealServer')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('FrontProtocol') is not None:
            self.front_protocol = m.get('FrontProtocol')
        return self


class DescribePortRulePageResponseBody(TeaModel):
    def __init__(
        self,
        rule_list: List[DescribePortRulePageResponseBodyRuleList] = None,
        request_id: str = None,
        count: int = None,
    ):
        self.rule_list = rule_list
        self.request_id = request_id
        self.count = count

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = DescribePortRulePageResponseBodyRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribePortRulePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePortRulePageResponseBody = None,
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
            temp_model = DescribePortRulePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCcCustomedRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class ListCcCustomedRuleResponseBodyRuleListRule(TeaModel):
    def __init__(
        self,
        blocking_time: int = None,
        blocking_type: str = None,
        interval: int = None,
        visit_count: int = None,
        name: str = None,
        uri: str = None,
        matching_rule: str = None,
    ):
        self.blocking_time = blocking_time
        self.blocking_type = blocking_type
        self.interval = interval
        self.visit_count = visit_count
        self.name = name
        self.uri = uri
        self.matching_rule = matching_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.blocking_time is not None:
            result['BlockingTime'] = self.blocking_time
        if self.blocking_type is not None:
            result['BlockingType'] = self.blocking_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.visit_count is not None:
            result['VisitCount'] = self.visit_count
        if self.name is not None:
            result['Name'] = self.name
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.matching_rule is not None:
            result['MatchingRule'] = self.matching_rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockingTime') is not None:
            self.blocking_time = m.get('BlockingTime')
        if m.get('BlockingType') is not None:
            self.blocking_type = m.get('BlockingType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('VisitCount') is not None:
            self.visit_count = m.get('VisitCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('MatchingRule') is not None:
            self.matching_rule = m.get('MatchingRule')
        return self


class ListCcCustomedRuleResponseBodyRuleList(TeaModel):
    def __init__(
        self,
        rule: List[ListCcCustomedRuleResponseBodyRuleListRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for k in self.rule:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rule'] = []
        if self.rule is not None:
            for k in self.rule:
                result['Rule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k in m.get('Rule'):
                temp_model = ListCcCustomedRuleResponseBodyRuleListRule()
                self.rule.append(temp_model.from_map(k))
        return self


class ListCcCustomedRuleResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        rule_list: ListCcCustomedRuleResponseBodyRuleList = None,
        request_id: str = None,
    ):
        self.total_count = total_count
        self.rule_list = rule_list
        self.request_id = request_id

    def validate(self):
        if self.rule_list:
            self.rule_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.rule_list is not None:
            result['RuleList'] = self.rule_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RuleList') is not None:
            temp_model = ListCcCustomedRuleResponseBodyRuleList()
            self.rule_list = temp_model.from_map(m['RuleList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCcCustomedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCcCustomedRuleResponseBody = None,
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
            temp_model = ListCcCustomedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCcCustomStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        enable: bool = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyCcCustomStatusResponseBody(TeaModel):
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


class ModifyCcCustomStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCcCustomStatusResponseBody = None,
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
            temp_model = ModifyCcCustomStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCcStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        enable: bool = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyCcStatusResponseBody(TeaModel):
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


class ModifyCcStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCcStatusResponseBody = None,
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
            temp_model = ModifyCcStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCcTemplateRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        mode: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class ModifyCcTemplateResponseBody(TeaModel):
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


class ModifyCcTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCcTemplateResponseBody = None,
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
            temp_model = ModifyCcTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDDoSProtectConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ip: str = None,
        front_port: int = None,
        config_json: str = None,
        lb_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ip = ip
        self.front_port = front_port
        self.config_json = config_json
        self.lb_id = lb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json
        if self.lb_id is not None:
            result['LbId'] = self.lb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('ConfigJson') is not None:
            self.config_json = m.get('ConfigJson')
        if m.get('LbId') is not None:
            self.lb_id = m.get('LbId')
        return self


class ModifyDDoSProtectConfigResponseBody(TeaModel):
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


class ModifyDDoSProtectConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDDoSProtectConfigResponseBody = None,
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
            temp_model = ModifyDDoSProtectConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainBlackWhiteListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        black: List[str] = None,
        white: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.black = black
        self.white = white

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.black is not None:
            result['Black'] = self.black
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Black') is not None:
            self.black = m.get('Black')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class ModifyDomainBlackWhiteListResponseBody(TeaModel):
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


class ModifyDomainBlackWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDomainBlackWhiteListResponseBody = None,
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
            temp_model = ModifyDomainBlackWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDomainProxyRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        proxy_type: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.proxy_type = proxy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')
        return self


class ModifyDomainProxyResponseBody(TeaModel):
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


class ModifyDomainProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDomainProxyResponseBody = None,
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
            temp_model = ModifyDomainProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticBandwidthRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        elastic_bandwidth: int = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.elastic_bandwidth = elastic_bandwidth
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class ModifyElasticBandwidthResponseBody(TeaModel):
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


class ModifyElasticBandwidthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyElasticBandwidthResponseBody = None,
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
            temp_model = ModifyElasticBandwidthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHealthCheckConfigRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ip: str = None,
        front_port: int = None,
        config_json: str = None,
        lb_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ip = ip
        self.front_port = front_port
        self.config_json = config_json
        self.lb_id = lb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json
        if self.lb_id is not None:
            result['LbId'] = self.lb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('ConfigJson') is not None:
            self.config_json = m.get('ConfigJson')
        if m.get('LbId') is not None:
            self.lb_id = m.get('LbId')
        return self


class ModifyHealthCheckConfigResponseBody(TeaModel):
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


class ModifyHealthCheckConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHealthCheckConfigResponseBody = None,
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
            temp_model = ModifyHealthCheckConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpCnameStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        ip: str = None,
        enable: bool = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.ip = ip
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class ModifyIpCnameStatusResponseBody(TeaModel):
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


class ModifyIpCnameStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIpCnameStatusResponseBody = None,
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
            temp_model = ModifyIpCnameStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPersistenceTimeOutRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        ip: str = None,
        front_port: int = None,
        config_json: str = None,
        lb_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.ip = ip
        self.front_port = front_port
        self.config_json = config_json
        self.lb_id = lb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.config_json is not None:
            result['ConfigJson'] = self.config_json
        if self.lb_id is not None:
            result['LbId'] = self.lb_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('ConfigJson') is not None:
            self.config_json = m.get('ConfigJson')
        if m.get('LbId') is not None:
            self.lb_id = m.get('LbId')
        return self


class ModifyPersistenceTimeOutResponseBody(TeaModel):
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


class ModifyPersistenceTimeOutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPersistenceTimeOutResponseBody = None,
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
            temp_model = ModifyPersistenceTimeOutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRealServersRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        type: str = None,
        domain: str = None,
        line: str = None,
        real_servers: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.type = type
        self.domain = domain
        self.line = line
        self.real_servers = real_servers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.line is not None:
            result['Line'] = self.line
        if self.real_servers is not None:
            result['RealServers'] = self.real_servers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('RealServers') is not None:
            self.real_servers = m.get('RealServers')
        return self


class ModifyRealServersResponseBody(TeaModel):
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


class ModifyRealServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRealServersResponseBody = None,
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
            temp_model = ModifyRealServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTransmitLineRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        domain: str = None,
        ips: List[str] = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.domain = domain
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class ModifyTransmitLineResponseBody(TeaModel):
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


class ModifyTransmitLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTransmitLineResponseBody = None,
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
            temp_model = ModifyTransmitLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCcCustomedRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        matching_rule: str = None,
        domain: str = None,
        visit_count: int = None,
        name: str = None,
        blocking_type: str = None,
        interval: int = None,
        blocking_time: int = None,
        uri: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.matching_rule = matching_rule
        self.domain = domain
        self.visit_count = visit_count
        self.name = name
        self.blocking_type = blocking_type
        self.interval = interval
        self.blocking_time = blocking_time
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.matching_rule is not None:
            result['MatchingRule'] = self.matching_rule
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.visit_count is not None:
            result['VisitCount'] = self.visit_count
        if self.name is not None:
            result['Name'] = self.name
        if self.blocking_type is not None:
            result['BlockingType'] = self.blocking_type
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.blocking_time is not None:
            result['BlockingTime'] = self.blocking_time
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchingRule') is not None:
            self.matching_rule = m.get('MatchingRule')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('VisitCount') is not None:
            self.visit_count = m.get('VisitCount')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('BlockingType') is not None:
            self.blocking_type = m.get('BlockingType')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('BlockingTime') is not None:
            self.blocking_time = m.get('BlockingTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class UpdateCcCustomedRuleResponseBody(TeaModel):
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


class UpdateCcCustomedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCcCustomedRuleResponseBody = None,
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
            temp_model = UpdateCcCustomedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePortRuleRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        front_port: int = None,
        real_server_list: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.front_port = front_port
        self.real_server_list = real_server_list
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.front_port is not None:
            result['FrontPort'] = self.front_port
        if self.real_server_list is not None:
            result['RealServerList'] = self.real_server_list
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('FrontPort') is not None:
            self.front_port = m.get('FrontPort')
        if m.get('RealServerList') is not None:
            self.real_server_list = m.get('RealServerList')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class UpdatePortRuleResponseBody(TeaModel):
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


class UpdatePortRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePortRuleResponseBody = None,
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
            temp_model = UpdatePortRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


