# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeAttackProtectionCountRequest(TeaModel):
    def __init__(
        self,
        agent_type: str = None,
        end_timestamp: int = None,
        start_timestamp: int = None,
    ):
        self.agent_type = agent_type
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # This parameter is required.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        return self


class DescribeAttackProtectionCountResponseBody(TeaModel):
    def __init__(
        self,
        block_high_count: int = None,
        block_low_count: int = None,
        block_medium_count: int = None,
        monitor_high_count: int = None,
        monitor_low_count: int = None,
        monitor_medium_count: int = None,
        request_id: str = None,
        total_request_count: int = None,
    ):
        self.block_high_count = block_high_count
        self.block_low_count = block_low_count
        self.block_medium_count = block_medium_count
        self.monitor_high_count = monitor_high_count
        self.monitor_low_count = monitor_low_count
        self.monitor_medium_count = monitor_medium_count
        self.request_id = request_id
        self.total_request_count = total_request_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_high_count is not None:
            result['BlockHighCount'] = self.block_high_count
        if self.block_low_count is not None:
            result['BlockLowCount'] = self.block_low_count
        if self.block_medium_count is not None:
            result['BlockMediumCount'] = self.block_medium_count
        if self.monitor_high_count is not None:
            result['MonitorHighCount'] = self.monitor_high_count
        if self.monitor_low_count is not None:
            result['MonitorLowCount'] = self.monitor_low_count
        if self.monitor_medium_count is not None:
            result['MonitorMediumCount'] = self.monitor_medium_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_request_count is not None:
            result['TotalRequestCount'] = self.total_request_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockHighCount') is not None:
            self.block_high_count = m.get('BlockHighCount')
        if m.get('BlockLowCount') is not None:
            self.block_low_count = m.get('BlockLowCount')
        if m.get('BlockMediumCount') is not None:
            self.block_medium_count = m.get('BlockMediumCount')
        if m.get('MonitorHighCount') is not None:
            self.monitor_high_count = m.get('MonitorHighCount')
        if m.get('MonitorLowCount') is not None:
            self.monitor_low_count = m.get('MonitorLowCount')
        if m.get('MonitorMediumCount') is not None:
            self.monitor_medium_count = m.get('MonitorMediumCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRequestCount') is not None:
            self.total_request_count = m.get('TotalRequestCount')
        return self


class DescribeAttackProtectionCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAttackProtectionCountResponseBody = None,
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
            temp_model = DescribeAttackProtectionCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAttacksRequest(TeaModel):
    def __init__(
        self,
        agent_type: str = None,
        application_id: str = None,
        attack_host_id: str = None,
        attack_type: str = None,
        attack_url: str = None,
        end_timestamp: int = None,
        handler_type: str = None,
        hostname: str = None,
        ip: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        pid: str = None,
        rasp_type: str = None,
        region: str = None,
        remote: str = None,
        severity: str = None,
        start_timestamp: int = None,
        union_id: str = None,
    ):
        self.agent_type = agent_type
        self.application_id = application_id
        self.attack_host_id = attack_host_id
        self.attack_type = attack_type
        self.attack_url = attack_url
        # This parameter is required.
        self.end_timestamp = end_timestamp
        self.handler_type = handler_type
        self.hostname = hostname
        self.ip = ip
        self.lang = lang
        self.page_number = page_number
        self.page_size = page_size
        self.pid = pid
        self.rasp_type = rasp_type
        self.region = region
        self.remote = remote
        self.severity = severity
        # This parameter is required.
        self.start_timestamp = start_timestamp
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attack_host_id is not None:
            result['AttackHostId'] = self.attack_host_id
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type
        if self.attack_url is not None:
            result['AttackUrl'] = self.attack_url
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.handler_type is not None:
            result['HandlerType'] = self.handler_type
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.rasp_type is not None:
            result['RaspType'] = self.rasp_type
        if self.region is not None:
            result['Region'] = self.region
        if self.remote is not None:
            result['Remote'] = self.remote
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('AttackHostId') is not None:
            self.attack_host_id = m.get('AttackHostId')
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')
        if m.get('AttackUrl') is not None:
            self.attack_url = m.get('AttackUrl')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('HandlerType') is not None:
            self.handler_type = m.get('HandlerType')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RaspType') is not None:
            self.rasp_type = m.get('RaspType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remote') is not None:
            self.remote = m.get('Remote')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class DescribeAttacksResponseBodyAttacksInputParamItemList(TeaModel):
    def __init__(
        self,
        processed_key: str = None,
        raw_key: str = None,
        value: str = None,
    ):
        self.processed_key = processed_key
        self.raw_key = raw_key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.processed_key is not None:
            result['ProcessedKey'] = self.processed_key
        if self.raw_key is not None:
            result['RawKey'] = self.raw_key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessedKey') is not None:
            self.processed_key = m.get('ProcessedKey')
        if m.get('RawKey') is not None:
            self.raw_key = m.get('RawKey')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeAttacksResponseBodyAttacks(TeaModel):
    def __init__(
        self,
        app_dir: str = None,
        app_id: str = None,
        app_name: str = None,
        avd: str = None,
        cmdline: str = None,
        confidence: str = None,
        content: str = None,
        content_length: int = None,
        count: int = None,
        data: str = None,
        headers: str = None,
        host_id: str = None,
        hostname: str = None,
        input_param_item_list: List[DescribeAttacksResponseBodyAttacksInputParamItemList] = None,
        install_type: int = None,
        ip: str = None,
        jdk: str = None,
        language: str = None,
        language_version: str = None,
        max_timestamp: int = None,
        message: str = None,
        method: str = None,
        middleware_instance_id: str = None,
        min_timestamp: int = None,
        os: str = None,
        os_arch: str = None,
        os_version: str = None,
        param: str = None,
        payload: str = None,
        payload_length: int = None,
        pid: str = None,
        rasp_version: str = None,
        region: str = None,
        remote: str = None,
        result: str = None,
        rule_result: str = None,
        severity: str = None,
        stacktrace: List[str] = None,
        time: str = None,
        timestamp: int = None,
        type: str = None,
        union_id: str = None,
        url: str = None,
    ):
        self.app_dir = app_dir
        self.app_id = app_id
        self.app_name = app_name
        self.avd = avd
        self.cmdline = cmdline
        self.confidence = confidence
        self.content = content
        self.content_length = content_length
        self.count = count
        self.data = data
        self.headers = headers
        self.host_id = host_id
        self.hostname = hostname
        self.input_param_item_list = input_param_item_list
        self.install_type = install_type
        self.ip = ip
        self.jdk = jdk
        self.language = language
        self.language_version = language_version
        self.max_timestamp = max_timestamp
        self.message = message
        self.method = method
        self.middleware_instance_id = middleware_instance_id
        self.min_timestamp = min_timestamp
        self.os = os
        self.os_arch = os_arch
        self.os_version = os_version
        self.param = param
        self.payload = payload
        self.payload_length = payload_length
        self.pid = pid
        self.rasp_version = rasp_version
        self.region = region
        self.remote = remote
        self.result = result
        self.rule_result = rule_result
        self.severity = severity
        self.stacktrace = stacktrace
        self.time = time
        self.timestamp = timestamp
        self.type = type
        # unionId。
        self.union_id = union_id
        self.url = url

    def validate(self):
        if self.input_param_item_list:
            for k in self.input_param_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_dir is not None:
            result['AppDir'] = self.app_dir
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.avd is not None:
            result['Avd'] = self.avd
        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.content is not None:
            result['Content'] = self.content
        if self.content_length is not None:
            result['ContentLength'] = self.content_length
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        result['InputParamItemList'] = []
        if self.input_param_item_list is not None:
            for k in self.input_param_item_list:
                result['InputParamItemList'].append(k.to_map() if k else None)
        if self.install_type is not None:
            result['InstallType'] = self.install_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.language is not None:
            result['Language'] = self.language
        if self.language_version is not None:
            result['LanguageVersion'] = self.language_version
        if self.max_timestamp is not None:
            result['MaxTimestamp'] = self.max_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.method is not None:
            result['Method'] = self.method
        if self.middleware_instance_id is not None:
            result['MiddlewareInstanceId'] = self.middleware_instance_id
        if self.min_timestamp is not None:
            result['MinTimestamp'] = self.min_timestamp
        if self.os is not None:
            result['Os'] = self.os
        if self.os_arch is not None:
            result['OsArch'] = self.os_arch
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.param is not None:
            result['Param'] = self.param
        if self.payload is not None:
            result['Payload'] = self.payload
        if self.payload_length is not None:
            result['PayloadLength'] = self.payload_length
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.rasp_version is not None:
            result['RaspVersion'] = self.rasp_version
        if self.region is not None:
            result['Region'] = self.region
        if self.remote is not None:
            result['Remote'] = self.remote
        if self.result is not None:
            result['Result'] = self.result
        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.stacktrace is not None:
            result['Stacktrace'] = self.stacktrace
        if self.time is not None:
            result['Time'] = self.time
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDir') is not None:
            self.app_dir = m.get('AppDir')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Avd') is not None:
            self.avd = m.get('Avd')
        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentLength') is not None:
            self.content_length = m.get('ContentLength')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        self.input_param_item_list = []
        if m.get('InputParamItemList') is not None:
            for k in m.get('InputParamItemList'):
                temp_model = DescribeAttacksResponseBodyAttacksInputParamItemList()
                self.input_param_item_list.append(temp_model.from_map(k))
        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LanguageVersion') is not None:
            self.language_version = m.get('LanguageVersion')
        if m.get('MaxTimestamp') is not None:
            self.max_timestamp = m.get('MaxTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('MiddlewareInstanceId') is not None:
            self.middleware_instance_id = m.get('MiddlewareInstanceId')
        if m.get('MinTimestamp') is not None:
            self.min_timestamp = m.get('MinTimestamp')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsArch') is not None:
            self.os_arch = m.get('OsArch')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        if m.get('PayloadLength') is not None:
            self.payload_length = m.get('PayloadLength')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RaspVersion') is not None:
            self.rasp_version = m.get('RaspVersion')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remote') is not None:
            self.remote = m.get('Remote')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Stacktrace') is not None:
            self.stacktrace = m.get('Stacktrace')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAttacksResponseBody(TeaModel):
    def __init__(
        self,
        attacks: List[DescribeAttacksResponseBodyAttacks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.attacks = attacks
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.attacks:
            for k in self.attacks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attacks'] = []
        if self.attacks is not None:
            for k in self.attacks:
                result['Attacks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attacks = []
        if m.get('Attacks') is not None:
            for k in m.get('Attacks'):
                temp_model = DescribeAttacksResponseBodyAttacks()
                self.attacks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAttacksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAttacksResponseBody = None,
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
            temp_model = DescribeAttacksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


