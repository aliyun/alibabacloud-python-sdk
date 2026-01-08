# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sasrasp20240727 import models as main_models
from darabonba.model import DaraModel

class DescribeAttacksResponseBody(DaraModel):
    def __init__(
        self,
        attacks: List[main_models.DescribeAttacksResponseBodyAttacks] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.attacks = attacks
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.attacks:
            for v1 in self.attacks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attacks'] = []
        if self.attacks is not None:
            for k1 in self.attacks:
                result['Attacks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attacks = []
        if m.get('Attacks') is not None:
            for k1 in m.get('Attacks'):
                temp_model = main_models.DescribeAttacksResponseBodyAttacks()
                self.attacks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAttacksResponseBodyAttacks(DaraModel):
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
        handle_status: int = None,
        handle_timestamp: int = None,
        headers: str = None,
        host_id: str = None,
        hostname: str = None,
        input_param_item_list: List[main_models.DescribeAttacksResponseBodyAttacksInputParamItemList] = None,
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
        self.handle_status = handle_status
        self.handle_timestamp = handle_timestamp
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
            for v1 in self.input_param_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status

        if self.handle_timestamp is not None:
            result['HandleTimestamp'] = self.handle_timestamp

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        result['InputParamItemList'] = []
        if self.input_param_item_list is not None:
            for k1 in self.input_param_item_list:
                result['InputParamItemList'].append(k1.to_map() if k1 else None)

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

        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')

        if m.get('HandleTimestamp') is not None:
            self.handle_timestamp = m.get('HandleTimestamp')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        self.input_param_item_list = []
        if m.get('InputParamItemList') is not None:
            for k1 in m.get('InputParamItemList'):
                temp_model = main_models.DescribeAttacksResponseBodyAttacksInputParamItemList()
                self.input_param_item_list.append(temp_model.from_map(k1))

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



class DescribeAttacksResponseBodyAttacksInputParamItemList(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

