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
        # The site monitoring tasks that are returned.
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
        # The URL or IP address that is monitored by the site monitoring task.
        self.address = address
        # The detection point type. Valid values:
        # 
        # *   PC
        # *   MOBILE
        self.agent_group = agent_group
        # The time when the site monitoring task was created.
        self.create_time = create_time
        # The interval at which detection requests are sent. Unit: minutes.
        self.interval = interval
        # The extended options of the site monitoring task. The options vary based on the specified protocol. For more information, see [CreateSiteMonitor](https://help.aliyun.com/document_detail/115048.html).
        self.options_json = options_json
        # The ID of the site monitoring task.
        self.task_id = task_id
        # The name of the site monitoring task.
        self.task_name = task_name
        # The task status. Valid values:
        # 
        # *   1: The task is enabled.
        # *   2: The task is disabled.
        self.task_state = task_state
        # The protocol that is used by the site monitoring task. Valid values: HTTP, PING, TCP, UDP, DNS, SMTP, POP3, and FTP.
        self.task_type = task_type
        # The time when the site monitoring task was updated.
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
        # The acceptable status code.
        # 
        # >  We recommend that you configure assertions.
        self.acceptable_response_code = acceptable_response_code
        # The assertions.
        self.assertions = assertions
        # The number of retries after a DNS failure occurred.
        self.attempts = attempts
        # Indicates whether the security authentication feature is enabled. Valid values:
        # 
        # *   0: The feature is enabled.
        # *   1: The feature is disabled.
        self.authentication = authentication
        # Indicates whether the certificate is verified. Valid values:
        # 
        # *   false (default): The certificate is not verified.
        # *   true: The certificate is verified.
        self.cert_verify = cert_verify
        # The cookie of the HTTP request.
        self.cookie = cookie
        # Indicates whether MTR is automatically used to diagnose network issues if a task fails. Valid values:
        # 
        # *   false (default): MTR is not automatically used to diagnose network issues if a task fails.
        # *   true: MTR is automatically used to diagnose network issues if a task fails.
        self.diagnosis_mtr = diagnosis_mtr
        # Indicates whether ping requests are automatically sent to detect network latency if a detection task fails. Valid values:
        # 
        # *   false (default): Ping requests are not automatically sent to detect network latency if a detection task fails.
        # *   true: Ping requests are automatically sent to detect network latency if a detection task fails.
        self.diagnosis_ping = diagnosis_ping
        # The relationship between the list of expected aliases or IP addresses and the list of DNS results. Valid values:
        # 
        # *   IN_DNS: The list of expected values is a subset of the list of DNS results.
        # *   DNS_IN: The list of DNS results is a subset of the list of expected values.
        # *   EQUAL: The list of DNS results is the same as the list of expected values.
        # *   ANY: The list of DNS results intersects with the list of expected values.
        self.dns_match_rule = dns_match_rule
        # The domain name or IP address of the DNS server.
        self.dns_server = dns_server
        # The type of the DNS record. This parameter is returned only if the TaskType parameter is set to DNS. Valid values:
        # 
        # *   A (default): a record that specifies an IP address related to the specified host name or domain name.
        # *   CNAME: a record that maps multiple domain names to a domain name.
        # *   NS: a record that specifies a DNS server used to parse domain names.
        # *   MX: a record that links domain names to the address of a mail server.
        # *   TXT: a record that stores the text information of host name or domain names. The text must be 1 to 512 bytes in length. The TXT record serves as a Sender Policy Framework (SPF) record to fight against spam.
        # *   AAAA: a record that maps a domain name to the relevant IPv6 address.
        self.dns_type = dns_type
        # Indicates whether the DNS server of the carrier is used.
        # 
        # *   true (default): The DNS server of the carrier is used.
        # *   false: The DNS server of the carrier is not used. The default DNS server or the specified DNS server is used.
        self.enable_operator_dns = enable_operator_dns
        # The packet loss rate.
        # 
        # >  This parameter is returned only if the TaskType parameter is set to PING.
        self.failure_rate = failure_rate
        # The header of the HTTP request. An HTTP header is a key-value pair in which the key and the value are separated by a colon (:). The format is `key1:value1`. Each HTTP header occupies a line.
        self.header = header
        # The HTTP request method. Valid values:
        # 
        # *   get
        # *   post
        # *   head
        self.http_method = http_method
        # Indicates whether the password is decoded by using the Base64 algorithm. Valid values:
        # 
        # *   true: The password is decoded by using the Base64 algorithm.
        # *   false (default): The password is not decoded by using the Base64 algorithm.
        self.is_base_64encode = is_base_64encode
        # Indicates whether the alert rule is included. Valid values:
        # 
        # *   0: The alert rule is included.
        # *   1: The alert rule is not included.
        self.match_rule = match_rule
        # The password of the SMTP, POP3, or FTP protocol.
        self.password = password
        # The number of hops for the PING protocol.
        self.ping_num = ping_num
        # The port number of the TCP, UDP, SMTP, or POP3 protocol.
        self.port = port
        # The protocol type of DNS detection. Valid values:
        # 
        # *   udp (default)
        # *   tcp
        # *   tcp-tls
        self.protocol = protocol
        # Indicates whether the PROXY protocol is enabled. Valid values:
        # 
        # *   false (default): The PROXY protocol is disabled.
        # *   true: The PROXY protocol is enabled.
        self.proxy_protocol = proxy_protocol
        # The content of the HTTP request.
        self.request_content = request_content
        # The format of the HTTP request. Valid values:
        # 
        # *   hex: hexadecimal
        # *   txt: text
        self.request_format = request_format
        # The response to the HTTP request.
        # 
        # *   Hexadecimal format: If the request content is a byte string and cannot be represented in printable characters, you can convert the byte string to printable characters in the hexadecimal format. If you convert the byte string to printable characters in the hexadecimal format, one byte is converted to two hexadecimal characters. For example, (byte)1 is converted to `01` and (byte)27 is converted to `1B`. If the request content is a binary array in the Java format, for example, `{(byte)1, (byte)27}`, you can convert the binary array to `011b` or `011B`. Hexadecimal characters are not case-sensitive in site monitoring tasks. You can enter `011B` in the request content and set the request_format parameter to hex.
        # *   Text format: Common text refers to strings that consist of printable characters.
        self.response_content = response_content
        # The format of the HTTP response. Valid values:
        # 
        # *   hex: hexadecimal
        # *   txt: text
        self.response_format = response_format
        # The number of times a failed detection request is retried.
        self.retry_delay = retry_delay
        # The timeout period. Unit: milliseconds.
        self.time_out = time_out
        # Indicates whether redirects are followed if the status code 301 or 302 is returned. Valid values:
        # 
        # *   true: Redirects are not followed.
        # *   false (default): Redirects are followed.
        self.unfollow_redirect = unfollow_redirect
        # The username of the FTP, SMTP, or POP3 protocol.
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
        # The comparison operator of the assertion. Valid values:
        # 
        # *   contains: contains
        # *   doesNotContain: does not contain
        # *   matches: matches regular expressions
        # *   doesNotMatch: does not match regular expressions
        # *   is: equal to a numeric value or matches a character
        # *   isNot: not equal to
        # *   lessThan: less than
        # *   moreThan: greater than
        self.operator = operator
        # The parsing path of the assertion.
        # 
        # *   If the assertion type is `body_json`, the path is `json path`.
        # *   If the assertion type is `body_xml`, the path is `xml path`.
        self.property = property
        # The numeric value or character used for matching.
        self.target = target
        # The assertion type. Valid values:
        # 
        # *   response_time: checks whether the response time meets expectations.
        # *   status_code: checks whether the HTTP status code meets expectations.
        # *   header: checks whether the fields in the response header meet expectations.
        # *   body_text: checks whether the content in the response body meets expectations by using text matching.
        # *   body_json: checks whether the content in the response body meets expectations by using JSON parsing (JSONPath).
        # *   body_xml: checks whether the content in the response body meets expectations by using XML parsing (XPath).
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

