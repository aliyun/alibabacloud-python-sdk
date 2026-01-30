# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteMonitorAttributeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        metric_rules: main_models.DescribeSiteMonitorAttributeResponseBodyMetricRules = None,
        request_id: str = None,
        site_monitors: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitors = None,
        success: bool = None,
    ):
        # The response code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The alert rules that are configured for the site monitoring task.
        self.metric_rules = metric_rules
        # The request ID.
        self.request_id = request_id
        # The details of the site monitoring task.
        self.site_monitors = site_monitors
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.metric_rules:
            self.metric_rules.validate()
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

        if self.metric_rules is not None:
            result['MetricRules'] = self.metric_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_monitors is not None:
            result['SiteMonitors'] = self.site_monitors.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MetricRules') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodyMetricRules()
            self.metric_rules = temp_model.from_map(m.get('MetricRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteMonitors') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitors()
            self.site_monitors = temp_model.from_map(m.get('SiteMonitors'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitors(DaraModel):
    def __init__(
        self,
        address: str = None,
        agent_group: str = None,
        custom_schedule: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomSchedule = None,
        interval: str = None,
        isp_cities: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCities = None,
        option_json: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJson = None,
        task_id: str = None,
        task_name: str = None,
        task_state: str = None,
        task_type: str = None,
        vpc_config: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsVpcConfig = None,
    ):
        # The URL that is monitored by the site monitoring task.
        self.address = address
        # The type of the detection point. Default value: PC. Valid values:
        # - PC
        # - MOBILE
        self.agent_group = agent_group
        # The custom detection cycle. You can specify only a time range within a week (from Monday to Sunday).
        self.custom_schedule = custom_schedule
        # The interval at which the site monitoring task is executed. Unit: minutes. Valid values: 1, 5, 15, 30, and 60.
        self.interval = interval
        # The information of detection points. The information includes the carriers that provide the detection points and the cities where the detection points reside.
        self.isp_cities = isp_cities
        # The extended options of the site monitoring task. The options vary based on the specified protocol. For more information, see [CreateSiteMonitor](https://help.aliyun.com/document_detail/115048.html).
        self.option_json = option_json
        # The ID of the site monitoring task.
        self.task_id = task_id
        # The name of the site monitoring task.
        self.task_name = task_name
        # The status of the site monitoring task. Valid values:
        # 
        # *   1: The task is enabled.
        # *   2: The task is disabled.
        self.task_state = task_state
        # The protocol that is used by the site monitoring task. Valid values: HTTP, HTTPS, PING, TCP, UDP, DNS, SMTP, POP3, and FTP.
        self.task_type = task_type
        # The VPC configurations of the synthetic test task.
        self.vpc_config = vpc_config

    def validate(self):
        if self.custom_schedule:
            self.custom_schedule.validate()
        if self.isp_cities:
            self.isp_cities.validate()
        if self.option_json:
            self.option_json.validate()
        if self.vpc_config:
            self.vpc_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.agent_group is not None:
            result['AgentGroup'] = self.agent_group

        if self.custom_schedule is not None:
            result['CustomSchedule'] = self.custom_schedule.to_map()

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.isp_cities is not None:
            result['IspCities'] = self.isp_cities.to_map()

        if self.option_json is not None:
            result['OptionJson'] = self.option_json.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_state is not None:
            result['TaskState'] = self.task_state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.vpc_config is not None:
            result['VpcConfig'] = self.vpc_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AgentGroup') is not None:
            self.agent_group = m.get('AgentGroup')

        if m.get('CustomSchedule') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomSchedule()
            self.custom_schedule = temp_model.from_map(m.get('CustomSchedule'))

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IspCities') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCities()
            self.isp_cities = temp_model.from_map(m.get('IspCities'))

        if m.get('OptionJson') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJson()
            self.option_json = temp_model.from_map(m.get('OptionJson'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('VpcConfig') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsVpcConfig()
            self.vpc_config = temp_model.from_map(m.get('VpcConfig'))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsVpcConfig(DaraModel):
    def __init__(
        self,
        region: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The region of the website for synthetic monitoring.
        self.region = region
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The ID of the VPC used by the synthetic test task.
        self.vpc_id = vpc_id
        # The ID of the vSwitch used by the synthetic test task.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['Region'] = self.region

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJson(DaraModel):
    def __init__(
        self,
        assertions: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertions = None,
        attempts: int = None,
        auth_info: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfo = None,
        blocked_url_list: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBlockedUrlList = None,
        browser_headers: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHeaders = None,
        browser_hosts: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHosts = None,
        browser_info: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfo = None,
        browser_insecure: bool = None,
        browser_task_version: str = None,
        config_variables: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariables = None,
        cookie: str = None,
        diagnosis_mtr: bool = None,
        diagnosis_ping: bool = None,
        dns_hijack_whitelist: str = None,
        dns_match_rule: str = None,
        dns_server: str = None,
        dns_type: str = None,
        empty_message: bool = None,
        enable_packet_capture: bool = None,
        expect_exist_string: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectExistString = None,
        expect_non_exist_string: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectNonExistString = None,
        expect_value: str = None,
        failure_rate: float = None,
        header: str = None,
        hops: int = None,
        host_binding: str = None,
        host_binding_type: int = None,
        http_method: str = None,
        icmp_timeout_millis: int = None,
        ip_network: str = None,
        is_base_64encode: str = None,
        match_rule: int = None,
        max_tls_version: str = None,
        min_tls_version: str = None,
        password: str = None,
        ping_num: int = None,
        ping_port: int = None,
        ping_type: str = None,
        port: int = None,
        private_crt_file_name: str = None,
        protocol: str = None,
        quic_enabled: bool = None,
        quic_target: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonQuicTarget = None,
        request_content: str = None,
        request_format: str = None,
        response_content: str = None,
        response_format: str = None,
        retry_delay: int = None,
        safe_link: int = None,
        screen_shot: bool = None,
        scroll_end: bool = None,
        server_name: str = None,
        steps: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonSteps = None,
        strict_mode: bool = None,
        supported_cipher_suits: str = None,
        time_out: int = None,
        trace_region: str = None,
        trace_type: str = None,
        traffic_hijack_element_blacklist: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementBlacklist = None,
        traffic_hijack_element_count: int = None,
        traffic_hijack_element_whitelist: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementWhitelist = None,
        use_private_crt: bool = None,
        use_ssl: bool = None,
        username: str = None,
        wait_time_after_completion: int = None,
    ):
        # The assertions.
        self.assertions = assertions
        # The number of retries after a DNS failure occurred.
        self.attempts = attempts
        self.auth_info = auth_info
        # The blocked URLs. Wildcards are supported in paths.
        self.blocked_url_list = blocked_url_list
        # The custom headers. Format: {"key": "somekey", "value":"somevalue"}.
        self.browser_headers = browser_headers
        # The custom hosts. Format: {"key": "somekey", "value":"somevalue"}.
        self.browser_hosts = browser_hosts
        # The browser information.
        self.browser_info = browser_info
        # Indicates whether certificate errors are ignored. Valid values:
        # - false: Certificate errors are not ignored.
        # - true: Certificate errors are ignored.
        self.browser_insecure = browser_insecure
        # The version of the browser test task. Valid values:
        # - 1: browser test for a single page
        # - 2: browser test for multiple pages
        self.browser_task_version = browser_task_version
        self.config_variables = config_variables
        # The cookie of the HTTP request.
        self.cookie = cookie
        # Indicates whether the automatic MTR diagnostics feature is enabled for a failed task. Valid values:
        # - false: The automatic MTR diagnostics feature is disabled for a failed task.
        # - true: The automatic MTR diagnostics feature is enabled for a failed task.
        self.diagnosis_mtr = diagnosis_mtr
        # Indicates whether the automatic ping latency detection feature is enabled for a failed task. Valid values:
        # - false: The automatic ping latency detection feature is disabled for a failed task.
        # - true: The automatic ping latency detection feature is enabled for a failed task.
        self.diagnosis_ping = diagnosis_ping
        # The DNS hijack whitelist.
        self.dns_hijack_whitelist = dns_hijack_whitelist
        # The relationship between the list of expected aliases or IP addresses and the list of DNS results. Valid values:
        # 
        # *   IN_DNS: The list of expected values is a subset of the list of DNS results.
        # *   DNS_IN: The list of DNS results is a subset of the list of expected values.
        # *   EQUAL: The list of DNS results is the same as the list of expected values.
        # *   ANY: The list of DNS results intersects with the list of expected values.
        self.dns_match_rule = dns_match_rule
        # The IP address of the DNS server.
        # 
        # >  This parameter is returned only if the TaskType parameter is set to DNS.
        self.dns_server = dns_server
        # The type of the DNS record. This parameter is returned only if the TaskType parameter is set to DNS. Valid values:
        # 
        # *   A (default): a record that specifies an IP address related to the specified host name or domain name.
        # *   CNAME: a record that maps multiple domain names to a domain name.
        # *   NS: a record that specifies a DNS server used to parse domain names.
        # *   MX: a record that links domain names to the address of a mail server.
        # *   TXT: a record that stores the text information of host name or domain names. The text must be 1 to 512 bytes in length. The TXT record serves as a Sender Policy Framework (SPF) record to fight against spam.
        self.dns_type = dns_type
        # Indicates whether the WebSocket task is allowed to return no response or return an empty response. Default value: false. Valid values: false and true.
        self.empty_message = empty_message
        self.enable_packet_capture = enable_packet_capture
        # The string that is expected to exist on the page.
        self.expect_exist_string = expect_exist_string
        # The string that is not expected to exist on the page.
        self.expect_non_exist_string = expect_non_exist_string
        # The domain name or alias to be parsed.
        # 
        # >  This parameter is returned only if the TaskType parameter is set to DNS.
        self.expect_value = expect_value
        # The packet loss rate.
        # 
        # >  This parameter is returned only if the TaskType parameter is set to PING.
        self.failure_rate = failure_rate
        # The header of the HTTP request.
        self.header = header
        # The number of hops to perform traceroute diagnostics if the PING task fails.
        self.hops = hops
        # The custom hosts for the HTTP test task. Format: ip1,ip2:address. You can specify values in multiple lines. Specify the A record or CNAME record that can be resolved by the domain name at the left of the colon. Separate multiple records with commas (,). Specify the domain name at the right of the colon.
        self.host_binding = host_binding
        # The host binding type. Valid values: 0 and 1. 0 indicates random. 1 indicates polling.
        self.host_binding_type = host_binding_type
        # The HTTP request method. Valid values:
        # 
        # *   get
        # *   post
        # *   head
        self.http_method = http_method
        # The timeout period of a PING task that uses ICMP. Unit: milliseconds.
        self.icmp_timeout_millis = icmp_timeout_millis
        # ip_network indicates the network type of the task. Valid values: v4, v6, and auto. Default value: v4.
        self.ip_network = ip_network
        # Indicates whether to perform Base64 decoding and then store the password. Valid values: true and false.
        self.is_base_64encode = is_base_64encode
        # Indicates whether the alert rule is included. Valid values:
        # 
        # *   0: The alert rule is included.
        # *   1: The alert rule is excluded.
        self.match_rule = match_rule
        self.max_tls_version = max_tls_version
        # The minimum TLS version. By default, TLS 1.2 and later versions are supported. TLS 1.0 and 1.1 are disabled. If you still require TLS 1.0 or 1.1, you can change the configuration.
        self.min_tls_version = min_tls_version
        # The password of the SMTP, POP3, or FTP protocol.
        self.password = password
        # The heartbeat of the PING protocol.
        self.ping_num = ping_num
        # The port number for TCP pings.
        self.ping_port = ping_port
        # The PING protocol type. Valid values:
        # 
        # *   icmp
        # *   tcp
        # *   udp
        self.ping_type = ping_type
        # The port number of the TCP, UDP, SMTP, or POP3 protocol.
        self.port = port
        self.private_crt_file_name = private_crt_file_name
        # The protocol that is used to send the request.
        self.protocol = protocol
        # Indicates whether the Quick UDP Internet Connections (QUIC) protocol is used for browser detection. Valid values: true false Default value: false.
        self.quic_enabled = quic_enabled
        # The sites for which the QUIC protocol is forcibly used.
        self.quic_target = quic_target
        # The content of the HTTP request.
        self.request_content = request_content
        # The format of the HTTP request. Valid values:
        # 
        # *   hex: hexadecimal
        # *   txt: text
        self.request_format = request_format
        # The response to the HTTP request.
        self.response_content = response_content
        # The format of the HTTP response. Valid values:
        # 
        # *   hex: hexadecimal
        # *   txt: text
        self.response_format = response_format
        # The number of retries for failed detections.
        self.retry_delay = retry_delay
        self.safe_link = safe_link
        # Indicates whether page screenshot is enabled.
        self.screen_shot = screen_shot
        # Indicates whether to scroll to the bottom of the page after opening the page. This parameter is valid for a browser test task.
        self.scroll_end = scroll_end
        self.server_name = server_name
        self.steps = steps
        # Indicates whether to allow the loading failures of some page elements. Valid values: false and true.
        self.strict_mode = strict_mode
        self.supported_cipher_suits = supported_cipher_suits
        # The timeout period. Unit: milliseconds.
        self.time_out = time_out
        self.trace_region = trace_region
        self.trace_type = trace_type
        # The traffic hijacking blacklist. When redirection occurs, if the URL of the resource loaded by the browser matches the expression in the blacklist, traffic hijacking is considered to have occurred.
        self.traffic_hijack_element_blacklist = traffic_hijack_element_blacklist
        # When redirection occurs, if the browser loads more than the specified number of resources, traffic hijacking is considered to have occurred. If you set the value to 0, no validation is performed. Default value: 0.
        self.traffic_hijack_element_count = traffic_hijack_element_count
        # The traffic hijacking whitelist. When redirection occurs, if the URL of the resource loaded by the browser does not match any expression in the whitelist, traffic hijacking is considered to have occurred.
        self.traffic_hijack_element_whitelist = traffic_hijack_element_whitelist
        self.use_private_crt = use_private_crt
        self.use_ssl = use_ssl
        # The username of the FTP, SMTP, or POP3 protocol.
        self.username = username
        # The additional waiting time after a page is opened in a browser test task.
        self.wait_time_after_completion = wait_time_after_completion

    def validate(self):
        if self.assertions:
            self.assertions.validate()
        if self.auth_info:
            self.auth_info.validate()
        if self.blocked_url_list:
            self.blocked_url_list.validate()
        if self.browser_headers:
            self.browser_headers.validate()
        if self.browser_hosts:
            self.browser_hosts.validate()
        if self.browser_info:
            self.browser_info.validate()
        if self.config_variables:
            self.config_variables.validate()
        if self.expect_exist_string:
            self.expect_exist_string.validate()
        if self.expect_non_exist_string:
            self.expect_non_exist_string.validate()
        if self.quic_target:
            self.quic_target.validate()
        if self.steps:
            self.steps.validate()
        if self.traffic_hijack_element_blacklist:
            self.traffic_hijack_element_blacklist.validate()
        if self.traffic_hijack_element_whitelist:
            self.traffic_hijack_element_whitelist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assertions is not None:
            result['assertions'] = self.assertions.to_map()

        if self.attempts is not None:
            result['attempts'] = self.attempts

        if self.auth_info is not None:
            result['auth_info'] = self.auth_info.to_map()

        if self.blocked_url_list is not None:
            result['blocked_url_list'] = self.blocked_url_list.to_map()

        if self.browser_headers is not None:
            result['browser_headers'] = self.browser_headers.to_map()

        if self.browser_hosts is not None:
            result['browser_hosts'] = self.browser_hosts.to_map()

        if self.browser_info is not None:
            result['browser_info'] = self.browser_info.to_map()

        if self.browser_insecure is not None:
            result['browser_insecure'] = self.browser_insecure

        if self.browser_task_version is not None:
            result['browser_task_version'] = self.browser_task_version

        if self.config_variables is not None:
            result['config_variables'] = self.config_variables.to_map()

        if self.cookie is not None:
            result['cookie'] = self.cookie

        if self.diagnosis_mtr is not None:
            result['diagnosis_mtr'] = self.diagnosis_mtr

        if self.diagnosis_ping is not None:
            result['diagnosis_ping'] = self.diagnosis_ping

        if self.dns_hijack_whitelist is not None:
            result['dns_hijack_whitelist'] = self.dns_hijack_whitelist

        if self.dns_match_rule is not None:
            result['dns_match_rule'] = self.dns_match_rule

        if self.dns_server is not None:
            result['dns_server'] = self.dns_server

        if self.dns_type is not None:
            result['dns_type'] = self.dns_type

        if self.empty_message is not None:
            result['empty_message'] = self.empty_message

        if self.enable_packet_capture is not None:
            result['enable_packet_capture'] = self.enable_packet_capture

        if self.expect_exist_string is not None:
            result['expect_exist_string'] = self.expect_exist_string.to_map()

        if self.expect_non_exist_string is not None:
            result['expect_non_exist_string'] = self.expect_non_exist_string.to_map()

        if self.expect_value is not None:
            result['expect_value'] = self.expect_value

        if self.failure_rate is not None:
            result['failure_rate'] = self.failure_rate

        if self.header is not None:
            result['header'] = self.header

        if self.hops is not None:
            result['hops'] = self.hops

        if self.host_binding is not None:
            result['host_binding'] = self.host_binding

        if self.host_binding_type is not None:
            result['host_binding_type'] = self.host_binding_type

        if self.http_method is not None:
            result['http_method'] = self.http_method

        if self.icmp_timeout_millis is not None:
            result['icmp_timeout_millis'] = self.icmp_timeout_millis

        if self.ip_network is not None:
            result['ip_network'] = self.ip_network

        if self.is_base_64encode is not None:
            result['isBase64Encode'] = self.is_base_64encode

        if self.match_rule is not None:
            result['match_rule'] = self.match_rule

        if self.max_tls_version is not None:
            result['max_tls_version'] = self.max_tls_version

        if self.min_tls_version is not None:
            result['min_tls_version'] = self.min_tls_version

        if self.password is not None:
            result['password'] = self.password

        if self.ping_num is not None:
            result['ping_num'] = self.ping_num

        if self.ping_port is not None:
            result['ping_port'] = self.ping_port

        if self.ping_type is not None:
            result['ping_type'] = self.ping_type

        if self.port is not None:
            result['port'] = self.port

        if self.private_crt_file_name is not None:
            result['private_crt_file_name'] = self.private_crt_file_name

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.quic_enabled is not None:
            result['quic_enabled'] = self.quic_enabled

        if self.quic_target is not None:
            result['quic_target'] = self.quic_target.to_map()

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

        if self.safe_link is not None:
            result['safe_link'] = self.safe_link

        if self.screen_shot is not None:
            result['screen_shot'] = self.screen_shot

        if self.scroll_end is not None:
            result['scroll_end'] = self.scroll_end

        if self.server_name is not None:
            result['server_name'] = self.server_name

        if self.steps is not None:
            result['steps'] = self.steps.to_map()

        if self.strict_mode is not None:
            result['strict_mode'] = self.strict_mode

        if self.supported_cipher_suits is not None:
            result['supported_cipher_suits'] = self.supported_cipher_suits

        if self.time_out is not None:
            result['time_out'] = self.time_out

        if self.trace_region is not None:
            result['trace_region'] = self.trace_region

        if self.trace_type is not None:
            result['trace_type'] = self.trace_type

        if self.traffic_hijack_element_blacklist is not None:
            result['traffic_hijack_element_blacklist'] = self.traffic_hijack_element_blacklist.to_map()

        if self.traffic_hijack_element_count is not None:
            result['traffic_hijack_element_count'] = self.traffic_hijack_element_count

        if self.traffic_hijack_element_whitelist is not None:
            result['traffic_hijack_element_whitelist'] = self.traffic_hijack_element_whitelist.to_map()

        if self.use_private_crt is not None:
            result['use_private_crt'] = self.use_private_crt

        if self.use_ssl is not None:
            result['use_ssl'] = self.use_ssl

        if self.username is not None:
            result['username'] = self.username

        if self.wait_time_after_completion is not None:
            result['waitTime_after_completion'] = self.wait_time_after_completion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assertions') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertions()
            self.assertions = temp_model.from_map(m.get('assertions'))

        if m.get('attempts') is not None:
            self.attempts = m.get('attempts')

        if m.get('auth_info') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfo()
            self.auth_info = temp_model.from_map(m.get('auth_info'))

        if m.get('blocked_url_list') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBlockedUrlList()
            self.blocked_url_list = temp_model.from_map(m.get('blocked_url_list'))

        if m.get('browser_headers') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHeaders()
            self.browser_headers = temp_model.from_map(m.get('browser_headers'))

        if m.get('browser_hosts') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHosts()
            self.browser_hosts = temp_model.from_map(m.get('browser_hosts'))

        if m.get('browser_info') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfo()
            self.browser_info = temp_model.from_map(m.get('browser_info'))

        if m.get('browser_insecure') is not None:
            self.browser_insecure = m.get('browser_insecure')

        if m.get('browser_task_version') is not None:
            self.browser_task_version = m.get('browser_task_version')

        if m.get('config_variables') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariables()
            self.config_variables = temp_model.from_map(m.get('config_variables'))

        if m.get('cookie') is not None:
            self.cookie = m.get('cookie')

        if m.get('diagnosis_mtr') is not None:
            self.diagnosis_mtr = m.get('diagnosis_mtr')

        if m.get('diagnosis_ping') is not None:
            self.diagnosis_ping = m.get('diagnosis_ping')

        if m.get('dns_hijack_whitelist') is not None:
            self.dns_hijack_whitelist = m.get('dns_hijack_whitelist')

        if m.get('dns_match_rule') is not None:
            self.dns_match_rule = m.get('dns_match_rule')

        if m.get('dns_server') is not None:
            self.dns_server = m.get('dns_server')

        if m.get('dns_type') is not None:
            self.dns_type = m.get('dns_type')

        if m.get('empty_message') is not None:
            self.empty_message = m.get('empty_message')

        if m.get('enable_packet_capture') is not None:
            self.enable_packet_capture = m.get('enable_packet_capture')

        if m.get('expect_exist_string') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectExistString()
            self.expect_exist_string = temp_model.from_map(m.get('expect_exist_string'))

        if m.get('expect_non_exist_string') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectNonExistString()
            self.expect_non_exist_string = temp_model.from_map(m.get('expect_non_exist_string'))

        if m.get('expect_value') is not None:
            self.expect_value = m.get('expect_value')

        if m.get('failure_rate') is not None:
            self.failure_rate = m.get('failure_rate')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('hops') is not None:
            self.hops = m.get('hops')

        if m.get('host_binding') is not None:
            self.host_binding = m.get('host_binding')

        if m.get('host_binding_type') is not None:
            self.host_binding_type = m.get('host_binding_type')

        if m.get('http_method') is not None:
            self.http_method = m.get('http_method')

        if m.get('icmp_timeout_millis') is not None:
            self.icmp_timeout_millis = m.get('icmp_timeout_millis')

        if m.get('ip_network') is not None:
            self.ip_network = m.get('ip_network')

        if m.get('isBase64Encode') is not None:
            self.is_base_64encode = m.get('isBase64Encode')

        if m.get('match_rule') is not None:
            self.match_rule = m.get('match_rule')

        if m.get('max_tls_version') is not None:
            self.max_tls_version = m.get('max_tls_version')

        if m.get('min_tls_version') is not None:
            self.min_tls_version = m.get('min_tls_version')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('ping_num') is not None:
            self.ping_num = m.get('ping_num')

        if m.get('ping_port') is not None:
            self.ping_port = m.get('ping_port')

        if m.get('ping_type') is not None:
            self.ping_type = m.get('ping_type')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('private_crt_file_name') is not None:
            self.private_crt_file_name = m.get('private_crt_file_name')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('quic_enabled') is not None:
            self.quic_enabled = m.get('quic_enabled')

        if m.get('quic_target') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonQuicTarget()
            self.quic_target = temp_model.from_map(m.get('quic_target'))

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

        if m.get('safe_link') is not None:
            self.safe_link = m.get('safe_link')

        if m.get('screen_shot') is not None:
            self.screen_shot = m.get('screen_shot')

        if m.get('scroll_end') is not None:
            self.scroll_end = m.get('scroll_end')

        if m.get('server_name') is not None:
            self.server_name = m.get('server_name')

        if m.get('steps') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonSteps()
            self.steps = temp_model.from_map(m.get('steps'))

        if m.get('strict_mode') is not None:
            self.strict_mode = m.get('strict_mode')

        if m.get('supported_cipher_suits') is not None:
            self.supported_cipher_suits = m.get('supported_cipher_suits')

        if m.get('time_out') is not None:
            self.time_out = m.get('time_out')

        if m.get('trace_region') is not None:
            self.trace_region = m.get('trace_region')

        if m.get('trace_type') is not None:
            self.trace_type = m.get('trace_type')

        if m.get('traffic_hijack_element_blacklist') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementBlacklist()
            self.traffic_hijack_element_blacklist = temp_model.from_map(m.get('traffic_hijack_element_blacklist'))

        if m.get('traffic_hijack_element_count') is not None:
            self.traffic_hijack_element_count = m.get('traffic_hijack_element_count')

        if m.get('traffic_hijack_element_whitelist') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementWhitelist()
            self.traffic_hijack_element_whitelist = temp_model.from_map(m.get('traffic_hijack_element_whitelist'))

        if m.get('use_private_crt') is not None:
            self.use_private_crt = m.get('use_private_crt')

        if m.get('use_ssl') is not None:
            self.use_ssl = m.get('use_ssl')

        if m.get('username') is not None:
            self.username = m.get('username')

        if m.get('waitTime_after_completion') is not None:
            self.wait_time_after_completion = m.get('waitTime_after_completion')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementWhitelist(DaraModel):
    def __init__(
        self,
        traffic_hijack_element_whitelist: List[str] = None,
    ):
        self.traffic_hijack_element_whitelist = traffic_hijack_element_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_hijack_element_whitelist is not None:
            result['traffic_hijack_element_whitelist'] = self.traffic_hijack_element_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traffic_hijack_element_whitelist') is not None:
            self.traffic_hijack_element_whitelist = m.get('traffic_hijack_element_whitelist')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonTrafficHijackElementBlacklist(DaraModel):
    def __init__(
        self,
        traffic_hijack_element_blacklist: List[str] = None,
    ):
        self.traffic_hijack_element_blacklist = traffic_hijack_element_blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_hijack_element_blacklist is not None:
            result['traffic_hijack_element_blacklist'] = self.traffic_hijack_element_blacklist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traffic_hijack_element_blacklist') is not None:
            self.traffic_hijack_element_blacklist = m.get('traffic_hijack_element_blacklist')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonSteps(DaraModel):
    def __init__(
        self,
        steps: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsSteps] = None,
    ):
        self.steps = steps

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['steps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.steps = []
        if m.get('steps') is not None:
            for k1 in m.get('steps'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsSteps()
                self.steps.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsSteps(DaraModel):
    def __init__(
        self,
        allow_failure: bool = None,
        auto_extract_cookie: bool = None,
        extracted_variables: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariables = None,
        is_critical: bool = None,
        name: str = None,
        option: str = None,
        step_name: str = None,
        step_type: str = None,
        url: str = None,
        use_generated_cookie: bool = None,
        wait_time_in_secs: int = None,
    ):
        self.allow_failure = allow_failure
        self.auto_extract_cookie = auto_extract_cookie
        self.extracted_variables = extracted_variables
        self.is_critical = is_critical
        self.name = name
        self.option = option
        self.step_name = step_name
        self.step_type = step_type
        self.url = url
        self.use_generated_cookie = use_generated_cookie
        self.wait_time_in_secs = wait_time_in_secs

    def validate(self):
        if self.extracted_variables:
            self.extracted_variables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_failure is not None:
            result['allow_failure'] = self.allow_failure

        if self.auto_extract_cookie is not None:
            result['auto_extract_cookie'] = self.auto_extract_cookie

        if self.extracted_variables is not None:
            result['extracted_variables'] = self.extracted_variables.to_map()

        if self.is_critical is not None:
            result['is_critical'] = self.is_critical

        if self.name is not None:
            result['name'] = self.name

        if self.option is not None:
            result['option'] = self.option

        if self.step_name is not None:
            result['step_name'] = self.step_name

        if self.step_type is not None:
            result['step_type'] = self.step_type

        if self.url is not None:
            result['url'] = self.url

        if self.use_generated_cookie is not None:
            result['use_generated_cookie'] = self.use_generated_cookie

        if self.wait_time_in_secs is not None:
            result['wait_time_in_secs'] = self.wait_time_in_secs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow_failure') is not None:
            self.allow_failure = m.get('allow_failure')

        if m.get('auto_extract_cookie') is not None:
            self.auto_extract_cookie = m.get('auto_extract_cookie')

        if m.get('extracted_variables') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariables()
            self.extracted_variables = temp_model.from_map(m.get('extracted_variables'))

        if m.get('is_critical') is not None:
            self.is_critical = m.get('is_critical')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('option') is not None:
            self.option = m.get('option')

        if m.get('step_name') is not None:
            self.step_name = m.get('step_name')

        if m.get('step_type') is not None:
            self.step_type = m.get('step_type')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('use_generated_cookie') is not None:
            self.use_generated_cookie = m.get('use_generated_cookie')

        if m.get('wait_time_in_secs') is not None:
            self.wait_time_in_secs = m.get('wait_time_in_secs')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariables(DaraModel):
    def __init__(
        self,
        extracted_variables: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariables] = None,
    ):
        self.extracted_variables = extracted_variables

    def validate(self):
        if self.extracted_variables:
            for v1 in self.extracted_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extracted_variables'] = []
        if self.extracted_variables is not None:
            for k1 in self.extracted_variables:
                result['extracted_variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extracted_variables = []
        if m.get('extracted_variables') is not None:
            for k1 in m.get('extracted_variables'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariables()
                self.extracted_variables.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariables(DaraModel):
    def __init__(
        self,
        extracted_type: str = None,
        field: str = None,
        name: str = None,
        parser: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariablesParser = None,
    ):
        self.extracted_type = extracted_type
        self.field = field
        self.name = name
        self.parser = parser

    def validate(self):
        if self.parser:
            self.parser.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extracted_type is not None:
            result['extracted_type'] = self.extracted_type

        if self.field is not None:
            result['field'] = self.field

        if self.name is not None:
            result['name'] = self.name

        if self.parser is not None:
            result['parser'] = self.parser.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extracted_type') is not None:
            self.extracted_type = m.get('extracted_type')

        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parser') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariablesParser()
            self.parser = temp_model.from_map(m.get('parser'))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonStepsStepsExtractedVariablesExtractedVariablesParser(DaraModel):
    def __init__(
        self,
        parser_type: str = None,
        value: str = None,
    ):
        self.parser_type = parser_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parser_type is not None:
            result['parser_type'] = self.parser_type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parser_type') is not None:
            self.parser_type = m.get('parser_type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonQuicTarget(DaraModel):
    def __init__(
        self,
        quic_target: List[str] = None,
    ):
        self.quic_target = quic_target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quic_target is not None:
            result['quic_target'] = self.quic_target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quic_target') is not None:
            self.quic_target = m.get('quic_target')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectNonExistString(DaraModel):
    def __init__(
        self,
        expect_non_exist_string: List[str] = None,
    ):
        self.expect_non_exist_string = expect_non_exist_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expect_non_exist_string is not None:
            result['expect_non_exist_string'] = self.expect_non_exist_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expect_non_exist_string') is not None:
            self.expect_non_exist_string = m.get('expect_non_exist_string')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonExpectExistString(DaraModel):
    def __init__(
        self,
        expect_exist_string: List[str] = None,
    ):
        self.expect_exist_string = expect_exist_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expect_exist_string is not None:
            result['expect_exist_string'] = self.expect_exist_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expect_exist_string') is not None:
            self.expect_exist_string = m.get('expect_exist_string')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariables(DaraModel):
    def __init__(
        self,
        config_variables: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariablesConfigVariables] = None,
    ):
        self.config_variables = config_variables

    def validate(self):
        if self.config_variables:
            for v1 in self.config_variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['config_variables'] = []
        if self.config_variables is not None:
            for k1 in self.config_variables:
                result['config_variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_variables = []
        if m.get('config_variables') is not None:
            for k1 in m.get('config_variables'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariablesConfigVariables()
                self.config_variables.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonConfigVariablesConfigVariables(DaraModel):
    def __init__(
        self,
        name: str = None,
        secure: bool = None,
        value: str = None,
    ):
        self.name = name
        self.secure = secure
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.secure is not None:
            result['secure'] = self.secure

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('secure') is not None:
            self.secure = m.get('secure')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfo(DaraModel):
    def __init__(
        self,
        browser_info: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfoBrowserInfo] = None,
    ):
        self.browser_info = browser_info

    def validate(self):
        if self.browser_info:
            for v1 in self.browser_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['browser_info'] = []
        if self.browser_info is not None:
            for k1 in self.browser_info:
                result['browser_info'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.browser_info = []
        if m.get('browser_info') is not None:
            for k1 in m.get('browser_info'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfoBrowserInfo()
                self.browser_info.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserInfoBrowserInfo(DaraModel):
    def __init__(
        self,
        browser: str = None,
        device: str = None,
    ):
        # The browser type.
        self.browser = browser
        # The device type.
        self.device = device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser is not None:
            result['browser'] = self.browser

        if self.device is not None:
            result['device'] = self.device

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browser') is not None:
            self.browser = m.get('browser')

        if m.get('device') is not None:
            self.device = m.get('device')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHosts(DaraModel):
    def __init__(
        self,
        browser_hosts: List[str] = None,
    ):
        self.browser_hosts = browser_hosts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_hosts is not None:
            result['browser_hosts'] = self.browser_hosts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browser_hosts') is not None:
            self.browser_hosts = m.get('browser_hosts')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBrowserHeaders(DaraModel):
    def __init__(
        self,
        browser_headers: List[Dict[str, Any]] = None,
    ):
        self.browser_headers = browser_headers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_headers is not None:
            result['browser_headers'] = self.browser_headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browser_headers') is not None:
            self.browser_headers = m.get('browser_headers')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonBlockedUrlList(DaraModel):
    def __init__(
        self,
        blocked_url_list: List[str] = None,
    ):
        self.blocked_url_list = blocked_url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blocked_url_list is not None:
            result['blocked_url_list'] = self.blocked_url_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('blocked_url_list') is not None:
            self.blocked_url_list = m.get('blocked_url_list')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfo(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        api_action: str = None,
        api_version: str = None,
        auth_style: str = None,
        client_id: str = None,
        client_secret: str = None,
        grant_type: str = None,
        password: str = None,
        region_id: str = None,
        scopes: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfoScopes = None,
        service_name: str = None,
        session_token: str = None,
        token_url: str = None,
        type: str = None,
        use_cookie_session_key: bool = None,
        username: str = None,
        with_addon_resources: bool = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.api_action = api_action
        self.api_version = api_version
        self.auth_style = auth_style
        self.client_id = client_id
        self.client_secret = client_secret
        self.grant_type = grant_type
        self.password = password
        self.region_id = region_id
        self.scopes = scopes
        self.service_name = service_name
        self.session_token = session_token
        self.token_url = token_url
        self.type = type
        self.use_cookie_session_key = use_cookie_session_key
        self.username = username
        self.with_addon_resources = with_addon_resources

    def validate(self):
        if self.scopes:
            self.scopes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['access_key_id'] = self.access_key_id

        if self.access_key_secret is not None:
            result['access_key_secret'] = self.access_key_secret

        if self.api_action is not None:
            result['api_action'] = self.api_action

        if self.api_version is not None:
            result['api_version'] = self.api_version

        if self.auth_style is not None:
            result['auth_style'] = self.auth_style

        if self.client_id is not None:
            result['client_id'] = self.client_id

        if self.client_secret is not None:
            result['client_secret'] = self.client_secret

        if self.grant_type is not None:
            result['grant_type'] = self.grant_type

        if self.password is not None:
            result['password'] = self.password

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.scopes is not None:
            result['scopes'] = self.scopes.to_map()

        if self.service_name is not None:
            result['service_name'] = self.service_name

        if self.session_token is not None:
            result['session_token'] = self.session_token

        if self.token_url is not None:
            result['token_url'] = self.token_url

        if self.type is not None:
            result['type'] = self.type

        if self.use_cookie_session_key is not None:
            result['use_cookie_session_key'] = self.use_cookie_session_key

        if self.username is not None:
            result['username'] = self.username

        if self.with_addon_resources is not None:
            result['with_addon_resources'] = self.with_addon_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_key_id') is not None:
            self.access_key_id = m.get('access_key_id')

        if m.get('access_key_secret') is not None:
            self.access_key_secret = m.get('access_key_secret')

        if m.get('api_action') is not None:
            self.api_action = m.get('api_action')

        if m.get('api_version') is not None:
            self.api_version = m.get('api_version')

        if m.get('auth_style') is not None:
            self.auth_style = m.get('auth_style')

        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')

        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')

        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('scopes') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfoScopes()
            self.scopes = temp_model.from_map(m.get('scopes'))

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        if m.get('session_token') is not None:
            self.session_token = m.get('session_token')

        if m.get('token_url') is not None:
            self.token_url = m.get('token_url')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('use_cookie_session_key') is not None:
            self.use_cookie_session_key = m.get('use_cookie_session_key')

        if m.get('username') is not None:
            self.username = m.get('username')

        if m.get('with_addon_resources') is not None:
            self.with_addon_resources = m.get('with_addon_resources')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAuthInfoScopes(DaraModel):
    def __init__(
        self,
        scopes: List[str] = None,
    ):
        self.scopes = scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scopes is not None:
            result['scopes'] = self.scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertions(DaraModel):
    def __init__(
        self,
        assertions: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertionsAssertions] = None,
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
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertionsAssertions()
                self.assertions.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsOptionJsonAssertionsAssertions(DaraModel):
    def __init__(
        self,
        operator: str = None,
        property: str = None,
        target: str = None,
        type: str = None,
    ):
        # The operator. Valid values:
        # - contains: contains
        # - doesNotContain: does not contain
        # - matches: matches a regular expression
        # - doesNotMatch: does not match a regular expression
        # - is: equal to
        # - isNot: not equal to
        # - lessThan: less than
        # - moreThan: greater than
        self.operator = operator
        # The path to the assertion.
        # - If the assertion type is body_json, the path is json path.
        # - If the assertion type is body_xml, the path is xml path.
        self.property = property
        # The value or character to which the condition of the assertion is compared.
        self.target = target
        # The assertion type. Valid values:
        # - response_time: checks whether the response time meets expectations.
        # - status_code: checks whether the HTTP status code meets expectations.
        # - header: checks whether the fields in the response header meet expectations.
        # - body_text: check whether the content in the response body meets expectations by using text matching.
        # - body_json: check whether the content in the response body meets expectations by using JSON parsing (JSONPath).
        # - body_xml: check whether the content in the response body meets expectations by using XML parsing (XPath).
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

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCities(DaraModel):
    def __init__(
        self,
        isp_city: List[main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCitiesIspCity] = None,
    ):
        self.isp_city = isp_city

    def validate(self):
        if self.isp_city:
            for v1 in self.isp_city:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspCity'] = []
        if self.isp_city is not None:
            for k1 in self.isp_city:
                result['IspCity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city = []
        if m.get('IspCity') is not None:
            for k1 in m.get('IspCity'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCitiesIspCity()
                self.isp_city.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsIspCitiesIspCity(DaraModel):
    def __init__(
        self,
        city: str = None,
        city_name: str = None,
        isp: str = None,
        isp_name: str = None,
        type: str = None,
    ):
        # The city ID.
        self.city = city
        # The city name.
        self.city_name = city_name
        # The carrier ID.
        self.isp = isp
        # The carrier name.
        self.isp_name = isp_name
        # The network type of the detection point. Valid values: IDC, LASTMILE, and MOBILE.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['City'] = self.city

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomSchedule(DaraModel):
    def __init__(
        self,
        days: main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomScheduleDays = None,
        end_hour: int = None,
        start_hour: int = None,
        time_zone: str = None,
    ):
        # The days in a week.
        self.days = days
        # The end time of the detection. Unit: hours.
        self.end_hour = end_hour
        # The start time of the detection. Unit: hours.
        self.start_hour = start_hour
        # The time zone of the detection.
        self.time_zone = time_zone

    def validate(self):
        if self.days:
            self.days.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['days'] = self.days.to_map()

        if self.end_hour is not None:
            result['end_hour'] = self.end_hour

        if self.start_hour is not None:
            result['start_hour'] = self.start_hour

        if self.time_zone is not None:
            result['time_zone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            temp_model = main_models.DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomScheduleDays()
            self.days = temp_model.from_map(m.get('days'))

        if m.get('end_hour') is not None:
            self.end_hour = m.get('end_hour')

        if m.get('start_hour') is not None:
            self.start_hour = m.get('start_hour')

        if m.get('time_zone') is not None:
            self.time_zone = m.get('time_zone')

        return self

class DescribeSiteMonitorAttributeResponseBodySiteMonitorsCustomScheduleDays(DaraModel):
    def __init__(
        self,
        days: List[int] = None,
    ):
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['days'] = self.days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')

        return self

class DescribeSiteMonitorAttributeResponseBodyMetricRules(DaraModel):
    def __init__(
        self,
        metric_rule: List[main_models.DescribeSiteMonitorAttributeResponseBodyMetricRulesMetricRule] = None,
    ):
        self.metric_rule = metric_rule

    def validate(self):
        if self.metric_rule:
            for v1 in self.metric_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetricRule'] = []
        if self.metric_rule is not None:
            for k1 in self.metric_rule:
                result['MetricRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metric_rule = []
        if m.get('MetricRule') is not None:
            for k1 in m.get('MetricRule'):
                temp_model = main_models.DescribeSiteMonitorAttributeResponseBodyMetricRulesMetricRule()
                self.metric_rule.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorAttributeResponseBodyMetricRulesMetricRule(DaraModel):
    def __init__(
        self,
        action_enable: str = None,
        alarm_actions: str = None,
        comparison_operator: str = None,
        dimensions: str = None,
        evaluation_count: str = None,
        expression: str = None,
        level: str = None,
        metric_name: str = None,
        namespace: str = None,
        ok_actions: str = None,
        period: str = None,
        rule_id: str = None,
        rule_name: str = None,
        state_value: str = None,
        statistics: str = None,
        threshold: str = None,
    ):
        # Indicates whether the alert rule is enabled. Valid values:
        # 
        # *   true: The alert rule is enabled.
        # *   false: The alert rule is disabled.
        self.action_enable = action_enable
        # The alert contact group to which alert notifications are sent.
        self.alarm_actions = alarm_actions
        # The operator that is used to compare the metric value with the threshold in the alert rule. Valid values:
        # 
        # *   `>=`
        # *   `>`
        # *   `<=`
        # *   `<`
        # *   `=`
        # *   `!=`
        # *   GreaterThanYesterday: greater than the metric value at the same time yesterday
        # *   LessThanYesterday: less than the metric value at the same time yesterday
        # *   GreaterThanLastWeek: greater than the metric value at the same time last week
        # *   LessThanLastWeek: less than the metric value at the same time last week
        # *   GreaterThanLastPeriod: greater than the metric value in the last monitoring cycle
        # *   LessThanLastPeriod: less than the metric value in the last monitoring cycle
        self.comparison_operator = comparison_operator
        # The dimension of the alert rule.
        self.dimensions = dimensions
        # The consecutive number of times for which the metric value meets the alert condition before an alert is triggered.
        self.evaluation_count = evaluation_count
        # The expression that is used to trigger alerts.
        self.expression = expression
        # The alert severity. Valid values:
        # 
        # *   1: critical
        # *   2: warning
        # *   3: information
        self.level = level
        # The metric name.
        self.metric_name = metric_name
        # The namespace of the cloud service.
        # 
        # The value is in the following format: acs_service name.
        self.namespace = namespace
        # The alert contact group that receives alert notifications.
        self.ok_actions = ok_actions
        # The time interval. The value is the same as the interval at which metric data is reported. Unit: seconds.
        # 
        # >  If you specify a statistical period for the alert rule, data is queried based on the statistical period.
        self.period = period
        # The ID of the alert rule.
        self.rule_id = rule_id
        # The name of the alert rule.
        self.rule_name = rule_name
        # The alert status. Valid values:
        # 
        # *   OK: The alert rule has no active alerts.
        # *   ALARM: The alert rule has active alerts.
        self.state_value = state_value
        # The statistical method of the alert rule. Valid values:
        # 
        # *   Availability: the percentage of available detection points
        # *   AvailableNumber: the number of available detection points
        # *   ErrorCodeMaximum: a status code for an alert
        # *   ErrorCodeMinimum: all status codes for a set of alerts
        # *   Average: response time
        self.statistics = statistics
        # The alert threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_enable is not None:
            result['ActionEnable'] = self.action_enable

        if self.alarm_actions is not None:
            result['AlarmActions'] = self.alarm_actions

        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.level is not None:
            result['Level'] = self.level

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.ok_actions is not None:
            result['OkActions'] = self.ok_actions

        if self.period is not None:
            result['Period'] = self.period

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.state_value is not None:
            result['StateValue'] = self.state_value

        if self.statistics is not None:
            result['Statistics'] = self.statistics

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionEnable') is not None:
            self.action_enable = m.get('ActionEnable')

        if m.get('AlarmActions') is not None:
            self.alarm_actions = m.get('AlarmActions')

        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OkActions') is not None:
            self.ok_actions = m.get('OkActions')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('StateValue') is not None:
            self.state_value = m.get('StateValue')

        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

