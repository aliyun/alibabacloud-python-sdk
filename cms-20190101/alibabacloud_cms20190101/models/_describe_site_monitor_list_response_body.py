# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteMonitorListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        site_monitors: main_models.DescribeSiteMonitorListResponseBodySiteMonitors = None,
        success: str = None,
        total_count: int = None,
    ):
        # The status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.site_monitors = site_monitors
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.site_monitors:
            self.site_monitors.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_monitors is not None:
            result['SiteMonitors'] = self.site_monitors.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteMonitors') is not None:
            temp_model = main_models.DescribeSiteMonitorListResponseBodySiteMonitors()
            self.site_monitors = temp_model.from_map(m.get('SiteMonitors'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSiteMonitorListResponseBodySiteMonitors(DaraModel):
    def __init__(
        self,
        site_monitor: List[main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitor] = None,
    ):
        self.site_monitor = site_monitor

    def validate(self):
        if self.site_monitor:
            for v1 in self.site_monitor:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SiteMonitor'] = []
        if self.site_monitor is not None:
            for k1 in self.site_monitor:
                result['SiteMonitor'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.site_monitor = []
        if m.get('SiteMonitor') is not None:
            for k1 in m.get('SiteMonitor'):
                temp_model = main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitor()
                self.site_monitor.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitor(DaraModel):
    def __init__(
        self,
        address: str = None,
        agent_group: str = None,
        create_time: str = None,
        interval: str = None,
        options_json: main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJson = None,
        task_id: str = None,
        task_name: str = None,
        task_state: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        self.address = address
        self.agent_group = agent_group
        self.create_time = create_time
        self.interval = interval
        self.options_json = options_json
        self.task_id = task_id
        self.task_name = task_name
        self.task_state = task_state
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        if self.options_json:
            self.options_json.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.agent_group is not None:
            result['AgentGroup'] = self.agent_group

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.options_json is not None:
            result['OptionsJson'] = self.options_json.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OptionsJson') is not None:
            temp_model = main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJson()
            self.options_json = temp_model.from_map(m.get('OptionsJson'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJson(DaraModel):
    def __init__(
        self,
        acceptable_response_code: str = None,
        assertions: main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertions = None,
        attempts: int = None,
        authentication: int = None,
        cert_verify: bool = None,
        cookie: str = None,
        diagnosis_mtr: bool = None,
        diagnosis_ping: bool = None,
        dns_match_rule: str = None,
        dns_server: str = None,
        dns_type: str = None,
        enable_operator_dns: bool = None,
        failure_rate: float = None,
        header: str = None,
        http_method: str = None,
        is_base_64encode: str = None,
        match_rule: int = None,
        password: str = None,
        ping_num: int = None,
        port: int = None,
        protocol: str = None,
        proxy_protocol: bool = None,
        request_content: str = None,
        request_format: str = None,
        response_content: str = None,
        response_format: str = None,
        retry_delay: int = None,
        time_out: int = None,
        unfollow_redirect: bool = None,
        username: str = None,
    ):
        self.acceptable_response_code = acceptable_response_code
        self.assertions = assertions
        self.attempts = attempts
        self.authentication = authentication
        self.cert_verify = cert_verify
        self.cookie = cookie
        self.diagnosis_mtr = diagnosis_mtr
        self.diagnosis_ping = diagnosis_ping
        self.dns_match_rule = dns_match_rule
        self.dns_server = dns_server
        self.dns_type = dns_type
        self.enable_operator_dns = enable_operator_dns
        self.failure_rate = failure_rate
        self.header = header
        self.http_method = http_method
        self.is_base_64encode = is_base_64encode
        self.match_rule = match_rule
        self.password = password
        self.ping_num = ping_num
        self.port = port
        self.protocol = protocol
        self.proxy_protocol = proxy_protocol
        self.request_content = request_content
        self.request_format = request_format
        self.response_content = response_content
        self.response_format = response_format
        self.retry_delay = retry_delay
        self.time_out = time_out
        self.unfollow_redirect = unfollow_redirect
        self.username = username

    def validate(self):
        if self.assertions:
            self.assertions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceptable_response_code is not None:
            result['acceptable_response_code'] = self.acceptable_response_code

        if self.assertions is not None:
            result['assertions'] = self.assertions.to_map()

        if self.attempts is not None:
            result['attempts'] = self.attempts

        if self.authentication is not None:
            result['authentication'] = self.authentication

        if self.cert_verify is not None:
            result['cert_verify'] = self.cert_verify

        if self.cookie is not None:
            result['cookie'] = self.cookie

        if self.diagnosis_mtr is not None:
            result['diagnosis_mtr'] = self.diagnosis_mtr

        if self.diagnosis_ping is not None:
            result['diagnosis_ping'] = self.diagnosis_ping

        if self.dns_match_rule is not None:
            result['dns_match_rule'] = self.dns_match_rule

        if self.dns_server is not None:
            result['dns_server'] = self.dns_server

        if self.dns_type is not None:
            result['dns_type'] = self.dns_type

        if self.enable_operator_dns is not None:
            result['enable_operator_dns'] = self.enable_operator_dns

        if self.failure_rate is not None:
            result['failure_rate'] = self.failure_rate

        if self.header is not None:
            result['header'] = self.header

        if self.http_method is not None:
            result['http_method'] = self.http_method

        if self.is_base_64encode is not None:
            result['isBase64Encode'] = self.is_base_64encode

        if self.match_rule is not None:
            result['match_rule'] = self.match_rule

        if self.password is not None:
            result['password'] = self.password

        if self.ping_num is not None:
            result['ping_num'] = self.ping_num

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.proxy_protocol is not None:
            result['proxy_protocol'] = self.proxy_protocol

        if self.request_content is not None:
            result['request_content'] = self.request_content

        if self.request_format is not None:
            result['request_format'] = self.request_format

        if self.response_content is not None:
            result['response_content'] = self.response_content

        if self.response_format is not None:
            result['response_format'] = self.response_format

        if self.retry_delay is not None:
            result['retry_delay'] = self.retry_delay

        if self.time_out is not None:
            result['time_out'] = self.time_out

        if self.unfollow_redirect is not None:
            result['unfollow_redirect'] = self.unfollow_redirect

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptable_response_code') is not None:
            self.acceptable_response_code = m.get('acceptable_response_code')

        if m.get('assertions') is not None:
            temp_model = main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertions()
            self.assertions = temp_model.from_map(m.get('assertions'))

        if m.get('attempts') is not None:
            self.attempts = m.get('attempts')

        if m.get('authentication') is not None:
            self.authentication = m.get('authentication')

        if m.get('cert_verify') is not None:
            self.cert_verify = m.get('cert_verify')

        if m.get('cookie') is not None:
            self.cookie = m.get('cookie')

        if m.get('diagnosis_mtr') is not None:
            self.diagnosis_mtr = m.get('diagnosis_mtr')

        if m.get('diagnosis_ping') is not None:
            self.diagnosis_ping = m.get('diagnosis_ping')

        if m.get('dns_match_rule') is not None:
            self.dns_match_rule = m.get('dns_match_rule')

        if m.get('dns_server') is not None:
            self.dns_server = m.get('dns_server')

        if m.get('dns_type') is not None:
            self.dns_type = m.get('dns_type')

        if m.get('enable_operator_dns') is not None:
            self.enable_operator_dns = m.get('enable_operator_dns')

        if m.get('failure_rate') is not None:
            self.failure_rate = m.get('failure_rate')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('http_method') is not None:
            self.http_method = m.get('http_method')

        if m.get('isBase64Encode') is not None:
            self.is_base_64encode = m.get('isBase64Encode')

        if m.get('match_rule') is not None:
            self.match_rule = m.get('match_rule')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('ping_num') is not None:
            self.ping_num = m.get('ping_num')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('proxy_protocol') is not None:
            self.proxy_protocol = m.get('proxy_protocol')

        if m.get('request_content') is not None:
            self.request_content = m.get('request_content')

        if m.get('request_format') is not None:
            self.request_format = m.get('request_format')

        if m.get('response_content') is not None:
            self.response_content = m.get('response_content')

        if m.get('response_format') is not None:
            self.response_format = m.get('response_format')

        if m.get('retry_delay') is not None:
            self.retry_delay = m.get('retry_delay')

        if m.get('time_out') is not None:
            self.time_out = m.get('time_out')

        if m.get('unfollow_redirect') is not None:
            self.unfollow_redirect = m.get('unfollow_redirect')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

class DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertions(DaraModel):
    def __init__(
        self,
        assertions: List[main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertionsAssertions] = None,
    ):
        self.assertions = assertions

    def validate(self):
        if self.assertions:
            for v1 in self.assertions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assertions'] = []
        if self.assertions is not None:
            for k1 in self.assertions:
                result['assertions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assertions = []
        if m.get('assertions') is not None:
            for k1 in m.get('assertions'):
                temp_model = main_models.DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertionsAssertions()
                self.assertions.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorListResponseBodySiteMonitorsSiteMonitorOptionsJsonAssertionsAssertions(DaraModel):
    def __init__(
        self,
        operator: str = None,
        property: str = None,
        target: str = None,
        type: str = None,
    ):
        self.operator = operator
        self.property = property
        self.target = target
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator is not None:
            result['operator'] = self.operator

        if self.property is not None:
            result['property'] = self.property

        if self.target is not None:
            result['target'] = self.target

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('property') is not None:
            self.property = m.get('property')

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

