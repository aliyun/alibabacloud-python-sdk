# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetTimingSyntheticTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTimingSyntheticTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code returned. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetTimingSyntheticTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        available_assertions: List[main_models.GetTimingSyntheticTaskResponseBodyDataAvailableAssertions] = None,
        common_setting: main_models.GetTimingSyntheticTaskResponseBodyDataCommonSetting = None,
        custom_period: main_models.GetTimingSyntheticTaskResponseBodyDataCustomPeriod = None,
        frequency: str = None,
        monitor_category: int = None,
        monitor_conf: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConf = None,
        monitors: List[main_models.GetTimingSyntheticTaskResponseBodyDataMonitors] = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetTimingSyntheticTaskResponseBodyDataTags] = None,
        task_id: str = None,
        task_type: int = None,
    ):
        # The list of assertions.
        self.available_assertions = available_assertions
        # The general settings.
        self.common_setting = common_setting
        # The custom cycle.
        self.custom_period = custom_period
        # The detection frequency. Valid values: 1m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, and 24h.
        self.frequency = frequency
        # The detection point type. 1: PC. 2: mobile device.
        self.monitor_category = monitor_category
        # The monitoring configurations.
        self.monitor_conf = monitor_conf
        # The list of monitoring points.
        self.monitors = monitors
        # The name of the task.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # CREATING: The task is being created. RUNNING: The task is running. PARTIAL_RUNNING: The task is partially running. STOP: The task is stopped. LIMIT_STOP: The task is stopped due to quota insufficiency. EXCEPTION: The task is abnormal. DELETE: The task is deleted. DELETE_EXCEPTION: The task failed to be deleted.
        self.status = status
        # The tag.
        self.tags = tags
        # The ID of the synthetic monitoring task.
        self.task_id = task_id
        # The type of the task. Valid values:
        # 
        # ICMP TCP DNS HTTP Website speed measurement File download
        self.task_type = task_type

    def validate(self):
        if self.available_assertions:
            for v1 in self.available_assertions:
                 if v1:
                    v1.validate()
        if self.common_setting:
            self.common_setting.validate()
        if self.custom_period:
            self.custom_period.validate()
        if self.monitor_conf:
            self.monitor_conf.validate()
        if self.monitors:
            for v1 in self.monitors:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableAssertions'] = []
        if self.available_assertions is not None:
            for k1 in self.available_assertions:
                result['AvailableAssertions'].append(k1.to_map() if k1 else None)

        if self.common_setting is not None:
            result['CommonSetting'] = self.common_setting.to_map()

        if self.custom_period is not None:
            result['CustomPeriod'] = self.custom_period.to_map()

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.monitor_category is not None:
            result['MonitorCategory'] = self.monitor_category

        if self.monitor_conf is not None:
            result['MonitorConf'] = self.monitor_conf.to_map()

        result['Monitors'] = []
        if self.monitors is not None:
            for k1 in self.monitors:
                result['Monitors'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_assertions = []
        if m.get('AvailableAssertions') is not None:
            for k1 in m.get('AvailableAssertions'):
                temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataAvailableAssertions()
                self.available_assertions.append(temp_model.from_map(k1))

        if m.get('CommonSetting') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCommonSetting()
            self.common_setting = temp_model.from_map(m.get('CommonSetting'))

        if m.get('CustomPeriod') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCustomPeriod()
            self.custom_period = temp_model.from_map(m.get('CustomPeriod'))

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('MonitorCategory') is not None:
            self.monitor_category = m.get('MonitorCategory')

        if m.get('MonitorConf') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConf()
            self.monitor_conf = temp_model.from_map(m.get('MonitorConf'))

        self.monitors = []
        if m.get('Monitors') is not None:
            for k1 in m.get('Monitors'):
                temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitors()
                self.monitors.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class GetTimingSyntheticTaskResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetTimingSyntheticTaskResponseBodyDataMonitors(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        client_type: int = None,
        operator_code: str = None,
    ):
        # The city code.
        self.city_code = city_code
        # The client type of the monitoring point. Valid values: 1: data center. 2: Internet. 3: mobile device. 4: ECS instance.
        self.client_type = client_type
        # The carrier code.
        self.operator_code = operator_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConf(DaraModel):
    def __init__(
        self,
        api_http: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTP = None,
        file_download: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfFileDownload = None,
        net_dns: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetDNS = None,
        net_icmp: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetICMP = None,
        net_tcp: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetTCP = None,
        stream: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfStream = None,
        website: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfWebsite = None,
    ):
        # The parameters of the HTTP(S) synthetic test.
        self.api_http = api_http
        # The file download parameters.
        self.file_download = file_download
        # The DNS synthetic test parameters. This parameter is required if the TaskType parameter is set to 3.
        self.net_dns = net_dns
        # The ICMP synthetic test parameters. This parameter is required if the TaskType parameter is set to 1.
        self.net_icmp = net_icmp
        # The TCP synthetic tests parameters. This parameter is required if the TaskType parameter is set to 2.
        self.net_tcp = net_tcp
        # Streaming media dial test configuration.
        self.stream = stream
        # The website-speed measurement parameters.
        self.website = website

    def validate(self):
        if self.api_http:
            self.api_http.validate()
        if self.file_download:
            self.file_download.validate()
        if self.net_dns:
            self.net_dns.validate()
        if self.net_icmp:
            self.net_icmp.validate()
        if self.net_tcp:
            self.net_tcp.validate()
        if self.stream:
            self.stream.validate()
        if self.website:
            self.website.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_http is not None:
            result['ApiHTTP'] = self.api_http.to_map()

        if self.file_download is not None:
            result['FileDownload'] = self.file_download.to_map()

        if self.net_dns is not None:
            result['NetDNS'] = self.net_dns.to_map()

        if self.net_icmp is not None:
            result['NetICMP'] = self.net_icmp.to_map()

        if self.net_tcp is not None:
            result['NetTCP'] = self.net_tcp.to_map()

        if self.stream is not None:
            result['Stream'] = self.stream.to_map()

        if self.website is not None:
            result['Website'] = self.website.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiHTTP') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTP()
            self.api_http = temp_model.from_map(m.get('ApiHTTP'))

        if m.get('FileDownload') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfFileDownload()
            self.file_download = temp_model.from_map(m.get('FileDownload'))

        if m.get('NetDNS') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetDNS()
            self.net_dns = temp_model.from_map(m.get('NetDNS'))

        if m.get('NetICMP') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetICMP()
            self.net_icmp = temp_model.from_map(m.get('NetICMP'))

        if m.get('NetTCP') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfNetTCP()
            self.net_tcp = temp_model.from_map(m.get('NetTCP'))

        if m.get('Stream') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfStream()
            self.stream = temp_model.from_map(m.get('Stream'))

        if m.get('Website') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfWebsite()
            self.website = temp_model.from_map(m.get('Website'))

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfWebsite(DaraModel):
    def __init__(
        self,
        automatic_scrolling: int = None,
        custom_header: int = None,
        custom_header_content: Dict[str, str] = None,
        dnshijack_whitelist: str = None,
        disable_cache: int = None,
        disable_compression: int = None,
        element_blacklist: str = None,
        filter_invalid_ip: int = None,
        flow_hijack_jump_times: int = None,
        flow_hijack_logo: str = None,
        ignore_certificate_error: int = None,
        monitor_timeout: int = None,
        page_tamper: str = None,
        redirection: int = None,
        slow_element_threshold: int = None,
        target_url: str = None,
        verify_string_blacklist: str = None,
        verify_string_whitelist: str = None,
        wait_completion_time: int = None,
    ):
        # Specifies whether to automatically scroll up and down the screen to load a page. 0: No. 1: Yes. Default value: 0.
        self.automatic_scrolling = automatic_scrolling
        # Specifies whether to create a custom header. 0: No. 1: The first packet is modified. 2: All packets are modified. Default value: 0.
        self.custom_header = custom_header
        # The custom header. Format: JSON map.
        self.custom_header_content = custom_header_content
        # When resolving a domain name (such as www.aliyun.com), if the resolved IP address or CNAME is not in the DNS hijacking whitelist, the user will fail to access or return a non-Aliyun target IP; if the IP or CNAME in the resolution result is in the DNS whitelist, it will be deemed that no DNS hijacking has occurred.
        # 
        # Fill in the format: `domain name: matching rule`. Matching rules support IP, IP wildcard, subnet mask and CNAME. You can fill in multiple matching rules, and multiple matching rules are separated by vertical bars (|). 
        # 
        # For example: `www.aliyun.com:203.0.3.55|203.3.44.67`, which means that all IPs except 203.0.3.55 and 203.3.44.67 under the www.aliyun.com domain name are hijacked.
        self.dnshijack_whitelist = dnshijack_whitelist
        # Specifies whether to disable the cache. 0: No. 1: Yes. Default value: 1.
        self.disable_cache = disable_cache
        # Specifies whether to accept compressed files based on the HTTP Accept-Encoding request header. 0: No. 1: Yes. Default value: 0.
        self.disable_compression = disable_compression
        # If an element configured in the element blacklist appears during page loading, no request will be made to load the element.
        self.element_blacklist = element_blacklist
        # Specifies whether to exclude invalid IP addresses.
        # 
        # *   1: No
        # *   0: Yes
        self.filter_invalid_ip = filter_invalid_ip
        # Identify elements: Set the total number of elements to browse the page.
        self.flow_hijack_jump_times = flow_hijack_jump_times
        # Hijacking flag: Set the key information for matching. Fill in the hijacking judgment keyword or key element, and asterisks (*) are allowed.
        self.flow_hijack_logo = flow_hijack_logo
        # Specifies whether to ignore SSL certificate errors during browsing. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_error = ignore_certificate_error
        # The monitoring timeout period. Unit: milliseconds. Default value: 20000. Minimum value: 5000. Maximum value: 300000.
        self.monitor_timeout = monitor_timeout
        # If any element other than the domain name setting appears on the monitoring page, it means that the page has been tampered. Common manifestations include pop-up ads, floating ads, jumps, etc.
        # 
        # Fill in the format: `domain name: element`. Elements support wildcards, and multiple elements can be filled in. Multiple elements are separated by vertical bars (|). For example: `www.aliyun.com:|/cc/bb/a.gif|/vv/bb/cc.jpg`, which means that all elements except the basic document, /cc/bb/a.gif and /vv/bb/cc.jpg under the www.aliyun.com domain name are considered to be tampered with.
        self.page_tamper = page_tamper
        # Specifies whether to continue browsing after redirection. 0: No, 1:Yes. Default value: 1.
        self.redirection = redirection
        # The time threshold that is used to define a slow element. Unit: milliseconds. Default value: 5000. Minimum value: 1. Maximum value: 300000.
        self.slow_element_threshold = slow_element_threshold
        # The destination URL.
        self.target_url = target_url
        # The verification string is an arbitrary string in the source code of the monitoring page. If the source code returned by the client contains any string in the blacklist, an error 650 &quot;Verification string failed&quot; will be reported. Multiple strings are separated by vertical bars (|).
        self.verify_string_blacklist = verify_string_blacklist
        # The verification string is an arbitrary string in the source code of the monitoring page. The source code returned by the client must contain all the strings in the whitelist, otherwise an error 650 &quot;Verification string failed&quot; will be reported. Multiple strings are separated by a vertical bar (|).
        self.verify_string_whitelist = verify_string_whitelist
        # The maximum waiting time. Unit: milliseconds. Default value: 5000. Minimum value: 5000. Maximum value: 300000.
        self.wait_completion_time = wait_completion_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatic_scrolling is not None:
            result['AutomaticScrolling'] = self.automatic_scrolling

        if self.custom_header is not None:
            result['CustomHeader'] = self.custom_header

        if self.custom_header_content is not None:
            result['CustomHeaderContent'] = self.custom_header_content

        if self.dnshijack_whitelist is not None:
            result['DNSHijackWhitelist'] = self.dnshijack_whitelist

        if self.disable_cache is not None:
            result['DisableCache'] = self.disable_cache

        if self.disable_compression is not None:
            result['DisableCompression'] = self.disable_compression

        if self.element_blacklist is not None:
            result['ElementBlacklist'] = self.element_blacklist

        if self.filter_invalid_ip is not None:
            result['FilterInvalidIP'] = self.filter_invalid_ip

        if self.flow_hijack_jump_times is not None:
            result['FlowHijackJumpTimes'] = self.flow_hijack_jump_times

        if self.flow_hijack_logo is not None:
            result['FlowHijackLogo'] = self.flow_hijack_logo

        if self.ignore_certificate_error is not None:
            result['IgnoreCertificateError'] = self.ignore_certificate_error

        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout

        if self.page_tamper is not None:
            result['PageTamper'] = self.page_tamper

        if self.redirection is not None:
            result['Redirection'] = self.redirection

        if self.slow_element_threshold is not None:
            result['SlowElementThreshold'] = self.slow_element_threshold

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.verify_string_blacklist is not None:
            result['VerifyStringBlacklist'] = self.verify_string_blacklist

        if self.verify_string_whitelist is not None:
            result['VerifyStringWhitelist'] = self.verify_string_whitelist

        if self.wait_completion_time is not None:
            result['WaitCompletionTime'] = self.wait_completion_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticScrolling') is not None:
            self.automatic_scrolling = m.get('AutomaticScrolling')

        if m.get('CustomHeader') is not None:
            self.custom_header = m.get('CustomHeader')

        if m.get('CustomHeaderContent') is not None:
            self.custom_header_content = m.get('CustomHeaderContent')

        if m.get('DNSHijackWhitelist') is not None:
            self.dnshijack_whitelist = m.get('DNSHijackWhitelist')

        if m.get('DisableCache') is not None:
            self.disable_cache = m.get('DisableCache')

        if m.get('DisableCompression') is not None:
            self.disable_compression = m.get('DisableCompression')

        if m.get('ElementBlacklist') is not None:
            self.element_blacklist = m.get('ElementBlacklist')

        if m.get('FilterInvalidIP') is not None:
            self.filter_invalid_ip = m.get('FilterInvalidIP')

        if m.get('FlowHijackJumpTimes') is not None:
            self.flow_hijack_jump_times = m.get('FlowHijackJumpTimes')

        if m.get('FlowHijackLogo') is not None:
            self.flow_hijack_logo = m.get('FlowHijackLogo')

        if m.get('IgnoreCertificateError') is not None:
            self.ignore_certificate_error = m.get('IgnoreCertificateError')

        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')

        if m.get('PageTamper') is not None:
            self.page_tamper = m.get('PageTamper')

        if m.get('Redirection') is not None:
            self.redirection = m.get('Redirection')

        if m.get('SlowElementThreshold') is not None:
            self.slow_element_threshold = m.get('SlowElementThreshold')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('VerifyStringBlacklist') is not None:
            self.verify_string_blacklist = m.get('VerifyStringBlacklist')

        if m.get('VerifyStringWhitelist') is not None:
            self.verify_string_whitelist = m.get('VerifyStringWhitelist')

        if m.get('WaitCompletionTime') is not None:
            self.wait_completion_time = m.get('WaitCompletionTime')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfStream(DaraModel):
    def __init__(
        self,
        custom_header_content: Dict[str, str] = None,
        player_type: int = None,
        stream_address_type: int = None,
        stream_monitor_timeout: int = None,
        stream_type: int = None,
        target_url: str = None,
        white_list: str = None,
    ):
        # Custom header, JSON Map format.
        self.custom_header_content = custom_header_content
        # Player, default is 12 if not specified.
        # 
        # - 12: VLC
        # - 2: Flash Player
        self.player_type = player_type
        # Resource address type:
        # 
        # - 1: Resource address.
        # - 0: Page address. If not passed, the default value is 0.
        self.stream_address_type = stream_address_type
        # Monitoring duration, in seconds, supports up to 60 seconds. If not specified, the default value is 60 seconds.
        self.stream_monitor_timeout = stream_monitor_timeout
        # Audio and video flag:
        # 
        # - 0: video
        # - 1: audio
        self.stream_type = stream_type
        # Streaming media resource address.
        self.target_url = target_url
        # DNS hijacking whitelist. Matching rules support IP, IP wildcard, subnet mask and CNAME. You can fill in multiple matching rules, and multiple matching rules are separated by vertical bars (|). For example: `www.aliyun.com:203.0.3.55|203.3.44.67`, which means that all IPs except 203.0.3.55 and 203.3.44.67 under the www.aliyun.com domain name are hijacked.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_header_content is not None:
            result['CustomHeaderContent'] = self.custom_header_content

        if self.player_type is not None:
            result['PlayerType'] = self.player_type

        if self.stream_address_type is not None:
            result['StreamAddressType'] = self.stream_address_type

        if self.stream_monitor_timeout is not None:
            result['StreamMonitorTimeout'] = self.stream_monitor_timeout

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaderContent') is not None:
            self.custom_header_content = m.get('CustomHeaderContent')

        if m.get('PlayerType') is not None:
            self.player_type = m.get('PlayerType')

        if m.get('StreamAddressType') is not None:
            self.stream_address_type = m.get('StreamAddressType')

        if m.get('StreamMonitorTimeout') is not None:
            self.stream_monitor_timeout = m.get('StreamMonitorTimeout')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfNetTCP(DaraModel):
    def __init__(
        self,
        connect_times: int = None,
        interval: int = None,
        target_url: str = None,
        timeout: int = None,
        tracert_enable: bool = None,
        tracert_num_max: int = None,
        tracert_timeout: int = None,
    ):
        # The number of TCP connections that are established in a test. Minimum value: 1. Maximum value: 16. Default value: 4.
        self.connect_times = connect_times
        # The interval at which TCP connections are established. Unit: milliseconds. Minimum value: 200. Maximum value: 10000. Default value: 200.
        self.interval = interval
        # The destination host IP address.
        self.target_url = target_url
        # The timeout period for the TCP synthetic test. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 20000.
        self.timeout = timeout
        # Specifies whether to enable the tracert command. Default value: true.
        self.tracert_enable = tracert_enable
        # The maximum number of hops for tracert. Minimum value: 1. Maximum value: 128. Default value: 20.
        self.tracert_num_max = tracert_num_max
        # The timeout period of tracert. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 60000.
        self.tracert_timeout = tracert_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_times is not None:
            result['ConnectTimes'] = self.connect_times

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.tracert_enable is not None:
            result['TracertEnable'] = self.tracert_enable

        if self.tracert_num_max is not None:
            result['TracertNumMax'] = self.tracert_num_max

        if self.tracert_timeout is not None:
            result['TracertTimeout'] = self.tracert_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectTimes') is not None:
            self.connect_times = m.get('ConnectTimes')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TracertEnable') is not None:
            self.tracert_enable = m.get('TracertEnable')

        if m.get('TracertNumMax') is not None:
            self.tracert_num_max = m.get('TracertNumMax')

        if m.get('TracertTimeout') is not None:
            self.tracert_timeout = m.get('TracertTimeout')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfNetICMP(DaraModel):
    def __init__(
        self,
        interval: int = None,
        package_num: int = None,
        package_size: int = None,
        split_package: bool = None,
        target_url: str = None,
        timeout: int = None,
        tracert_enable: bool = None,
        tracert_num_max: int = None,
        tracert_timeout: int = None,
    ):
        # The interval at which ICMP packets are sent. Unit: milliseconds. Minimum value: 200. Maximum value: 2000. Default value: 200.
        self.interval = interval
        # The number of ICMP packets that are sent. Minimum value: 1. Maximum value: 50. Default value: 4.
        self.package_num = package_num
        # The size of each ICMP packet. Unit: bytes. Valid values: 32, 64, 128, 256, 512, 1024.
        self.package_size = package_size
        # Specifies whether to split ICMP packets. Default value: true.
        self.split_package = split_package
        # The destination host IP address or domain name
        self.target_url = target_url
        # The timeout period for the TCP synthetic test. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 20000.
        self.timeout = timeout
        # Specifies whether to enable the tracert command. Default value: true.
        self.tracert_enable = tracert_enable
        # The maximum number of hops for tracert. Minimum value: 1. Maximum value: 128. Default value: 64.
        self.tracert_num_max = tracert_num_max
        # The timeout period of tracert. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 60000.
        self.tracert_timeout = tracert_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.package_num is not None:
            result['PackageNum'] = self.package_num

        if self.package_size is not None:
            result['PackageSize'] = self.package_size

        if self.split_package is not None:
            result['SplitPackage'] = self.split_package

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.tracert_enable is not None:
            result['TracertEnable'] = self.tracert_enable

        if self.tracert_num_max is not None:
            result['TracertNumMax'] = self.tracert_num_max

        if self.tracert_timeout is not None:
            result['TracertTimeout'] = self.tracert_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('PackageNum') is not None:
            self.package_num = m.get('PackageNum')

        if m.get('PackageSize') is not None:
            self.package_size = m.get('PackageSize')

        if m.get('SplitPackage') is not None:
            self.split_package = m.get('SplitPackage')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TracertEnable') is not None:
            self.tracert_enable = m.get('TracertEnable')

        if m.get('TracertNumMax') is not None:
            self.tracert_num_max = m.get('TracertNumMax')

        if m.get('TracertTimeout') is not None:
            self.tracert_timeout = m.get('TracertTimeout')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfNetDNS(DaraModel):
    def __init__(
        self,
        dns_server_ip_type: int = None,
        ns_server: str = None,
        query_method: int = None,
        target_url: str = None,
        timeout: int = None,
    ):
        # The IP version of the DNS server. 0: IPv4. 1: IPv6. 2: A version is automatically selected. Default value: 0.
        self.dns_server_ip_type = dns_server_ip_type
        # The IP address of the DNS server. Default value: 114.114.114.114.
        self.ns_server = ns_server
        # The DNS query. 0: recursive, 1: iterative. Default value: 0.
        self.query_method = query_method
        # The destination domain name.
        self.target_url = target_url
        # The timeout period for the DNS synthetic test. Unit: milliseconds. The minimum value is 1000 and the maximum value is 45000. Default value: 5000.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_server_ip_type is not None:
            result['DnsServerIpType'] = self.dns_server_ip_type

        if self.ns_server is not None:
            result['NsServer'] = self.ns_server

        if self.query_method is not None:
            result['QueryMethod'] = self.query_method

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsServerIpType') is not None:
            self.dns_server_ip_type = m.get('DnsServerIpType')

        if m.get('NsServer') is not None:
            self.ns_server = m.get('NsServer')

        if m.get('QueryMethod') is not None:
            self.query_method = m.get('QueryMethod')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfFileDownload(DaraModel):
    def __init__(
        self,
        connection_timeout: int = None,
        custom_header_content: Dict[str, str] = None,
        download_kernel: int = None,
        ignore_certificate_auth_error: int = None,
        ignore_certificate_canceled_error: int = None,
        ignore_certificate_out_of_date_error: int = None,
        ignore_certificate_status_error: int = None,
        ignore_certificate_untrustworthy_error: int = None,
        ignore_certificate_using_error: int = None,
        ignore_invalid_host_error: int = None,
        monitor_timeout: int = None,
        quick_protocol: int = None,
        redirection: int = None,
        target_url: str = None,
        transmission_size: int = None,
        validate_keywords: str = None,
        verify_way: int = None,
        white_list: str = None,
    ):
        # The connection timeout period. Unit: milliseconds. Minimum value: 1000. Maximum value: 120000. Default value: 5000.
        self.connection_timeout = connection_timeout
        # The content of the custom request header.
        self.custom_header_content = custom_header_content
        # The kernel type.
        # 
        # *   1: curl
        # *   0: WinInet
        self.download_kernel = download_kernel
        # Specifies whether to ignore CA certificate authentication errors. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_auth_error = ignore_certificate_auth_error
        # Specifies whether to ignore certificate revocation errors. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_canceled_error = ignore_certificate_canceled_error
        # Specifies whether to ignore certificate invalidity. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_out_of_date_error = ignore_certificate_out_of_date_error
        # Specifies whether to ignore certificate status errors. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_status_error = ignore_certificate_status_error
        # Specifies whether to ignore certificate incredibility. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_untrustworthy_error = ignore_certificate_untrustworthy_error
        # Specifies whether to ignore certificate usage errors. 0: No. 1: Yes. Default value: 1.
        self.ignore_certificate_using_error = ignore_certificate_using_error
        # Specifies whether to ignore host invalidity. 0: No. 1: Yes. Default value: 1.
        self.ignore_invalid_host_error = ignore_invalid_host_error
        # The monitoring timeout period. Unit: milliseconds. Minimum value: 1000. Maximum value: 120000. Default value: 60000.
        self.monitor_timeout = monitor_timeout
        # The QUIC protocol type.
        # 
        # *   1: http1
        # *   2: http2
        # *   3: http3
        self.quick_protocol = quick_protocol
        # Specifies whether to support redirection. 0: No. 1: Yes. Default value: 1.
        self.redirection = redirection
        # The file download URL.
        self.target_url = target_url
        # The maximum file size of a single transfer. Unit: KB. Minimum value: 1. Maximum value: 20480. Valid values: 2048.
        self.transmission_size = transmission_size
        # Verify keywords.
        self.validate_keywords = validate_keywords
        # Verification method.
        # 
        # - 0: No verification
        # - 1: Verification string
        # - 2: MD5 verification
        self.verify_way = verify_way
        # DNS hijacking whitelist. Matching rules support IP, IP wildcard, subnet mask and CNAME. You can fill in multiple matching rules, and multiple matching rules are separated by vertical bars (|). For example: `www.aliyun.com:203.0.3.55|203.3.44.67`, which means that all IPs except 203.0.3.55 and 203.3.44.67 under the www.aliyun.com domain name are hijacked.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_timeout is not None:
            result['ConnectionTimeout'] = self.connection_timeout

        if self.custom_header_content is not None:
            result['CustomHeaderContent'] = self.custom_header_content

        if self.download_kernel is not None:
            result['DownloadKernel'] = self.download_kernel

        if self.ignore_certificate_auth_error is not None:
            result['IgnoreCertificateAuthError'] = self.ignore_certificate_auth_error

        if self.ignore_certificate_canceled_error is not None:
            result['IgnoreCertificateCanceledError'] = self.ignore_certificate_canceled_error

        if self.ignore_certificate_out_of_date_error is not None:
            result['IgnoreCertificateOutOfDateError'] = self.ignore_certificate_out_of_date_error

        if self.ignore_certificate_status_error is not None:
            result['IgnoreCertificateStatusError'] = self.ignore_certificate_status_error

        if self.ignore_certificate_untrustworthy_error is not None:
            result['IgnoreCertificateUntrustworthyError'] = self.ignore_certificate_untrustworthy_error

        if self.ignore_certificate_using_error is not None:
            result['IgnoreCertificateUsingError'] = self.ignore_certificate_using_error

        if self.ignore_invalid_host_error is not None:
            result['IgnoreInvalidHostError'] = self.ignore_invalid_host_error

        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout

        if self.quick_protocol is not None:
            result['QuickProtocol'] = self.quick_protocol

        if self.redirection is not None:
            result['Redirection'] = self.redirection

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.transmission_size is not None:
            result['TransmissionSize'] = self.transmission_size

        if self.validate_keywords is not None:
            result['ValidateKeywords'] = self.validate_keywords

        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionTimeout') is not None:
            self.connection_timeout = m.get('ConnectionTimeout')

        if m.get('CustomHeaderContent') is not None:
            self.custom_header_content = m.get('CustomHeaderContent')

        if m.get('DownloadKernel') is not None:
            self.download_kernel = m.get('DownloadKernel')

        if m.get('IgnoreCertificateAuthError') is not None:
            self.ignore_certificate_auth_error = m.get('IgnoreCertificateAuthError')

        if m.get('IgnoreCertificateCanceledError') is not None:
            self.ignore_certificate_canceled_error = m.get('IgnoreCertificateCanceledError')

        if m.get('IgnoreCertificateOutOfDateError') is not None:
            self.ignore_certificate_out_of_date_error = m.get('IgnoreCertificateOutOfDateError')

        if m.get('IgnoreCertificateStatusError') is not None:
            self.ignore_certificate_status_error = m.get('IgnoreCertificateStatusError')

        if m.get('IgnoreCertificateUntrustworthyError') is not None:
            self.ignore_certificate_untrustworthy_error = m.get('IgnoreCertificateUntrustworthyError')

        if m.get('IgnoreCertificateUsingError') is not None:
            self.ignore_certificate_using_error = m.get('IgnoreCertificateUsingError')

        if m.get('IgnoreInvalidHostError') is not None:
            self.ignore_invalid_host_error = m.get('IgnoreInvalidHostError')

        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')

        if m.get('QuickProtocol') is not None:
            self.quick_protocol = m.get('QuickProtocol')

        if m.get('Redirection') is not None:
            self.redirection = m.get('Redirection')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('TransmissionSize') is not None:
            self.transmission_size = m.get('TransmissionSize')

        if m.get('ValidateKeywords') is not None:
            self.validate_keywords = m.get('ValidateKeywords')

        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTP(DaraModel):
    def __init__(
        self,
        check_cert: bool = None,
        connect_timeout: int = None,
        method: str = None,
        protocol_alpn_protocol: int = None,
        request_body: main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTPRequestBody = None,
        request_headers: Dict[str, str] = None,
        target_url: str = None,
        timeout: int = None,
    ):
        # Whether to verify the certificate. The default is no.
        self.check_cert = check_cert
        # The connection timeout period. Unit: milliseconds. Default value: 5000. Minimum value: 1000. Maximum value: 300000.
        self.connect_timeout = connect_timeout
        # The request method.
        # 
        # *   POST
        # *   GET
        self.method = method
        # The ALPN protocol version. You can configure this parameter when you perform an HTTPS synthetic test on a WAP mobile client. Valid values:
        # 
        # 0: default
        # 
        # 1: HTTP/1.1
        # 
        # 2: HTTP/2
        # 
        # 3: disables the ALPN protocol
        self.protocol_alpn_protocol = protocol_alpn_protocol
        # The HTTP request body.
        self.request_body = request_body
        # The HTTP request header.
        self.request_headers = request_headers
        # The URL for synthetic monitoring.
        self.target_url = target_url
        # The timeout period. Unit: milliseconds. Default value: 10000. Minimum value: 1000. Maximum value: 300000.
        self.timeout = timeout

    def validate(self):
        if self.request_body:
            self.request_body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_cert is not None:
            result['CheckCert'] = self.check_cert

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        if self.method is not None:
            result['Method'] = self.method

        if self.protocol_alpn_protocol is not None:
            result['ProtocolAlpnProtocol'] = self.protocol_alpn_protocol

        if self.request_body is not None:
            result['RequestBody'] = self.request_body.to_map()

        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckCert') is not None:
            self.check_cert = m.get('CheckCert')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('ProtocolAlpnProtocol') is not None:
            self.protocol_alpn_protocol = m.get('ProtocolAlpnProtocol')

        if m.get('RequestBody') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTPRequestBody()
            self.request_body = temp_model.from_map(m.get('RequestBody'))

        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetTimingSyntheticTaskResponseBodyDataMonitorConfApiHTTPRequestBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        type: str = None,
    ):
        # The content of the request body. Format: JSON string. The parameter is required if the type parameter is set to text/plain, application/json, application/xml, or text/html. Format: JSON string.
        self.content = content
        # The type of the request body. Valid values: text/plain, application/json, application/x-www-form-urlencoded, multipart/form-data, application/xml, and text/html.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetTimingSyntheticTaskResponseBodyDataCustomPeriod(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        start_hour: int = None,
    ):
        # The hour at which the test ends. Valid values: 0 to 24.
        self.end_hour = end_hour
        # The hour at which the test starts. Valid values: 0 to 24.
        self.start_hour = start_hour

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_hour is not None:
            result['EndHour'] = self.end_hour

        if self.start_hour is not None:
            result['StartHour'] = self.start_hour

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndHour') is not None:
            self.end_hour = m.get('EndHour')

        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')

        return self

class GetTimingSyntheticTaskResponseBodyDataCommonSetting(DaraModel):
    def __init__(
        self,
        custom_host: main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHost = None,
        custom_prometheus_setting: main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomPrometheusSetting = None,
        custom_vpcsetting: main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomVPCSetting = None,
        ip_type: int = None,
        is_open_trace: bool = None,
        monitor_samples: int = None,
        trace_client_type: int = None,
        xtrace_region: str = None,
    ):
        # The custom host.
        self.custom_host = custom_host
        # The reserved parameters.
        self.custom_prometheus_setting = custom_prometheus_setting
        # User VPC information. If the dial-up is to the Alibaba Cloud intranet address, you need to configure the VPC information.
        self.custom_vpcsetting = custom_vpcsetting
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4
        # *   2: IPv6
        self.ip_type = ip_type
        # Whether to enable tracing.
        self.is_open_trace = is_open_trace
        # Specifies whether to evenly distribute monitoring samples. Valid values:
        # 
        # *   0: No
        # *   1: Yes
        self.monitor_samples = monitor_samples
        # Tracing client type:
        # 
        # - 0: ARMS Agent
        # - 1: Open Telemetry
        # - 2: Jaeger
        self.trace_client_type = trace_client_type
        # Tracing data reporting region.
        self.xtrace_region = xtrace_region

    def validate(self):
        if self.custom_host:
            self.custom_host.validate()
        if self.custom_prometheus_setting:
            self.custom_prometheus_setting.validate()
        if self.custom_vpcsetting:
            self.custom_vpcsetting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_host is not None:
            result['CustomHost'] = self.custom_host.to_map()

        if self.custom_prometheus_setting is not None:
            result['CustomPrometheusSetting'] = self.custom_prometheus_setting.to_map()

        if self.custom_vpcsetting is not None:
            result['CustomVPCSetting'] = self.custom_vpcsetting.to_map()

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.is_open_trace is not None:
            result['IsOpenTrace'] = self.is_open_trace

        if self.monitor_samples is not None:
            result['MonitorSamples'] = self.monitor_samples

        if self.trace_client_type is not None:
            result['TraceClientType'] = self.trace_client_type

        if self.xtrace_region is not None:
            result['XtraceRegion'] = self.xtrace_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHost') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHost()
            self.custom_host = temp_model.from_map(m.get('CustomHost'))

        if m.get('CustomPrometheusSetting') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomPrometheusSetting()
            self.custom_prometheus_setting = temp_model.from_map(m.get('CustomPrometheusSetting'))

        if m.get('CustomVPCSetting') is not None:
            temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomVPCSetting()
            self.custom_vpcsetting = temp_model.from_map(m.get('CustomVPCSetting'))

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('IsOpenTrace') is not None:
            self.is_open_trace = m.get('IsOpenTrace')

        if m.get('MonitorSamples') is not None:
            self.monitor_samples = m.get('MonitorSamples')

        if m.get('TraceClientType') is not None:
            self.trace_client_type = m.get('TraceClientType')

        if m.get('XtraceRegion') is not None:
            self.xtrace_region = m.get('XtraceRegion')

        return self

class GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomVPCSetting(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        secure_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # Security group ID. This security group is where the dial-up client is located. The security group limits the inbound and outbound rules of the dial-up client in the VPC. You need to set the inbound rules of the security group where your VPC is located to allow the security group where the dial-up client is located to access. Otherwise, the dial-up client cannot smoothly access the resources in your VPC.
        self.secure_group_id = secure_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secure_group_id is not None:
            result['SecureGroupId'] = self.secure_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecureGroupId') is not None:
            self.secure_group_id = m.get('SecureGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomPrometheusSetting(DaraModel):
    def __init__(
        self,
        prometheus_cluster_id: str = None,
        prometheus_cluster_region: str = None,
        prometheus_labels: Dict[str, str] = None,
    ):
        # A reserved parameter.
        self.prometheus_cluster_id = prometheus_cluster_id
        # A reserved parameter.
        self.prometheus_cluster_region = prometheus_cluster_region
        # A reserved parameter.
        self.prometheus_labels = prometheus_labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_cluster_id is not None:
            result['PrometheusClusterId'] = self.prometheus_cluster_id

        if self.prometheus_cluster_region is not None:
            result['PrometheusClusterRegion'] = self.prometheus_cluster_region

        if self.prometheus_labels is not None:
            result['PrometheusLabels'] = self.prometheus_labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusClusterId') is not None:
            self.prometheus_cluster_id = m.get('PrometheusClusterId')

        if m.get('PrometheusClusterRegion') is not None:
            self.prometheus_cluster_region = m.get('PrometheusClusterRegion')

        if m.get('PrometheusLabels') is not None:
            self.prometheus_labels = m.get('PrometheusLabels')

        return self

class GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHost(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHostHosts] = None,
        select_type: int = None,
    ):
        # The list of hosts.
        self.hosts = hosts
        # The selection mode. 0: Random. 1: Polling.
        self.select_type = select_type

    def validate(self):
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHostHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        return self

class GetTimingSyntheticTaskResponseBodyDataCommonSettingCustomHostHosts(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_type: int = None,
        ips: List[str] = None,
    ):
        # The domain name.
        self.domain = domain
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4
        # *   2: IPv6
        self.ip_type = ip_type
        # The list of IP addresses.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.ips is not None:
            result['Ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        return self

class GetTimingSyntheticTaskResponseBodyDataAvailableAssertions(DaraModel):
    def __init__(
        self,
        expect: str = None,
        operator: str = None,
        target: str = None,
        type: str = None,
    ):
        # The expected value.
        self.expect = expect
        # The condition. gt: greater than. gte: greater than or equal to. lt: less than. lte: less than or equal to. eq: equal to. neq: not equal to. ctn: contain. nctn: does not contain. exist: exist. n_exist: does not exist. belong: belong to. n_belong: does not belong to. reg_match: regular expression.
        self.operator = operator
        # The check target. If you set the type parameter to HttpResCode, HttpResBody, or HttpResponseTime, you do not need to set the target parameter. If you set the type parameter to HttpResHead, you must specify the key in the header. If you set the type parameter to HttpResBodyJson, use jsonPath.
        self.target = target
        # The assertion type. Valid values: HttpResCode, HttpResHead, HttpResBody, HttpResBodyJson, HttpResponseTime, IcmpPackLoss (packet loss rate), IcmpPackMaxLatency (maximum packet latency), IcmpPackAvgLatency (average packet latency), TraceRouteHops (number of hops), DnsARecord (A record), DnsCName (CNAME), websiteTTFB (time to first packet), websiteTTLB (time to last packet), websiteFST (first paint time), websiteFFST (first meaningful paint), websiteOnload (full loaded time). For more information, see the following description.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expect is not None:
            result['Expect'] = self.expect

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expect') is not None:
            self.expect = m.get('Expect')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

