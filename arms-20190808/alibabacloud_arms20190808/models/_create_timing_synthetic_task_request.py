# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateTimingSyntheticTaskRequest(DaraModel):
    def __init__(
        self,
        available_assertions: List[main_models.CreateTimingSyntheticTaskRequestAvailableAssertions] = None,
        common_setting: main_models.CreateTimingSyntheticTaskRequestCommonSetting = None,
        custom_period: main_models.CreateTimingSyntheticTaskRequestCustomPeriod = None,
        frequency: str = None,
        monitor_category: int = None,
        monitor_conf: main_models.CreateTimingSyntheticTaskRequestMonitorConf = None,
        monitors: List[main_models.CreateTimingSyntheticTaskRequestMonitors] = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateTimingSyntheticTaskRequestTags] = None,
        task_type: int = None,
    ):
        # The list of assertions.
        self.available_assertions = available_assertions
        # The general settings.
        self.common_setting = common_setting
        # The general settings.
        self.custom_period = custom_period
        # The detection frequency. Valid values: 1m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, and 24h.
        # 
        # This parameter is required.
        self.frequency = frequency
        # The detection point type. Valid values:
        # 
        # - 1: PC
        # - 2: mobile device
        # 
        # This parameter is required.
        self.monitor_category = monitor_category
        # The monitoring configurations.
        # 
        # This parameter is required.
        self.monitor_conf = monitor_conf
        # The list of detection points.
        # 
        # This parameter is required.
        self.monitors = monitors
        # The name of the task.
        # 
        # This parameter is required.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The parameter is optional.
        self.resource_group_id = resource_group_id
        # The tag list.
        self.tags = tags
        # The type of the task. Valid values:
        # 
        # 1: ICMP. 2: TCP. 3: DNS. 4: HTTP. 5: website speed measurement. 6: file download.
        # 
        # This parameter is required.
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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_assertions = []
        if m.get('AvailableAssertions') is not None:
            for k1 in m.get('AvailableAssertions'):
                temp_model = main_models.CreateTimingSyntheticTaskRequestAvailableAssertions()
                self.available_assertions.append(temp_model.from_map(k1))

        if m.get('CommonSetting') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestCommonSetting()
            self.common_setting = temp_model.from_map(m.get('CommonSetting'))

        if m.get('CustomPeriod') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestCustomPeriod()
            self.custom_period = temp_model.from_map(m.get('CustomPeriod'))

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('MonitorCategory') is not None:
            self.monitor_category = m.get('MonitorCategory')

        if m.get('MonitorConf') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConf()
            self.monitor_conf = temp_model.from_map(m.get('MonitorConf'))

        self.monitors = []
        if m.get('Monitors') is not None:
            for k1 in m.get('Monitors'):
                temp_model = main_models.CreateTimingSyntheticTaskRequestMonitors()
                self.monitors.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateTimingSyntheticTaskRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class CreateTimingSyntheticTaskRequestTags(DaraModel):
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

class CreateTimingSyntheticTaskRequestMonitors(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        client_type: int = None,
        operator_code: str = None,
    ):
        # The city code.
        # 
        # This parameter is required.
        self.city_code = city_code
        # The client type of the detection point. Valid values:
        # 
        # - 1: data center
        # - 2: Internet
        # - 3: mobile device
        # - 4: ECS instance
        # 
        # This parameter is required.
        self.client_type = client_type
        # The carrier code.
        # 
        # This parameter is required.
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

class CreateTimingSyntheticTaskRequestMonitorConf(DaraModel):
    def __init__(
        self,
        api_http: main_models.CreateTimingSyntheticTaskRequestMonitorConfApiHTTP = None,
        file_download: main_models.CreateTimingSyntheticTaskRequestMonitorConfFileDownload = None,
        net_dns: main_models.CreateTimingSyntheticTaskRequestMonitorConfNetDNS = None,
        net_icmp: main_models.CreateTimingSyntheticTaskRequestMonitorConfNetICMP = None,
        net_tcp: main_models.CreateTimingSyntheticTaskRequestMonitorConfNetTCP = None,
        stream: main_models.CreateTimingSyntheticTaskRequestMonitorConfStream = None,
        website: main_models.CreateTimingSyntheticTaskRequestMonitorConfWebsite = None,
    ):
        # The parameters of the HTTP(S) synthetic test.
        self.api_http = api_http
        # The parameters of file downloading.
        self.file_download = file_download
        # The parameters of the DNS synthetic test. This parameter is required if the TaskType parameter is set to 3.
        self.net_dns = net_dns
        # The parameters of the ICMP synthetic test. This parameter is required if the TaskType parameter is set to 1.
        self.net_icmp = net_icmp
        # The parameters of the TCP synthetic test. This parameter is required if the TaskType parameter is set to 2.
        self.net_tcp = net_tcp
        # The parameters of the streaming-media synthetic test.
        self.stream = stream
        # The parameters of the website speed measurement.
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
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfApiHTTP()
            self.api_http = temp_model.from_map(m.get('ApiHTTP'))

        if m.get('FileDownload') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfFileDownload()
            self.file_download = temp_model.from_map(m.get('FileDownload'))

        if m.get('NetDNS') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfNetDNS()
            self.net_dns = temp_model.from_map(m.get('NetDNS'))

        if m.get('NetICMP') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfNetICMP()
            self.net_icmp = temp_model.from_map(m.get('NetICMP'))

        if m.get('NetTCP') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfNetTCP()
            self.net_tcp = temp_model.from_map(m.get('NetTCP'))

        if m.get('Stream') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfStream()
            self.stream = temp_model.from_map(m.get('Stream'))

        if m.get('Website') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfWebsite()
            self.website = temp_model.from_map(m.get('Website'))

        return self

class CreateTimingSyntheticTaskRequestMonitorConfWebsite(DaraModel):
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
        # Specifies whether to automatically scroll up and down the screen to load a page.
        # 
        # *   0 (default): no
        # *   1: yes
        self.automatic_scrolling = automatic_scrolling
        # Specifies whether to create a custom header.
        # 
        # *   0 (default): No custom header is created.
        # *   1: A custom header is created for the first packet.
        # *   2: A custom header is created for all packets.
        self.custom_header = custom_header
        # The custom header. Format: JSON map.
        self.custom_header_content = custom_header_content
        # If the IP address or CNAME record resolved from a domain name is not included in the DNS whitelist, you cannot access the domain name, or an IP address that belongs to a different domain name is returned. If the IP address or CNAME record is included in the DNS whitelist, DNS hijacking does not occur.
        # 
        # Format: \\<domain name>:\\<objects>. The objects can be IP addresses, wildcard mask, subnet mask, or CNAME records. Separate multiple objects with vertical bars (|). Example: www.aliyun.com:203.0.3.55|203.3.44.67. It indicates that all IP addresses that belong to the www.aliyun.com domain name except 203.0.3.55 and 203.3.44.67 are hijacked.
        self.dnshijack_whitelist = dnshijack_whitelist
        # Specifies whether to disable caching.
        # 
        # *   0: no
        # *   1 (default): yes
        self.disable_cache = disable_cache
        # Specifies whether to accept compressed files based on the HTTP Accept-Encoding request header. Valid values: 0: no. 1: yes. Default value: 0.
        self.disable_compression = disable_compression
        # The elements not to be loaded in the page loading process.
        self.element_blacklist = element_blacklist
        # Specifies whether to exclude invalid IP addresses. Valid values: 0: yes. 1: no. Default value: 0.
        self.filter_invalid_ip = filter_invalid_ip
        # The total number of elements on the page.
        self.flow_hijack_jump_times = flow_hijack_jump_times
        # The keyword that is used to identify hijacking. Asterisks (\\*) are allowed.
        self.flow_hijack_logo = flow_hijack_logo
        # Specifies whether to ignore certificate errors during certificate verification in the SSL handshake process and continue browsing. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_error = ignore_certificate_error
        # The monitoring timeout period. Unit: milliseconds. This parameter is optional. Default value: 20000.
        self.monitor_timeout = monitor_timeout
        # Elements that are not included in the whitelist and appear on the page are tampered with. These elements can be pop-up ads, floating ads, and page redirection.
        # 
        # Format: \\<domain name>:\\<elements>. The elements can be wildcard masks. Separate multiple elements with vertical bars (|). Example: www.aliyun.com:|/cc/bb/a.gif|/vv/bb/cc.jpg. It indicates that all elements that belong to the www.aliyun.com domain name except the basic documents, /cc/bb/a.gif, and /vv/bb/cc.jpg are tampered with.
        self.page_tamper = page_tamper
        # Specifies whether to continue browsing after redirection. Valid values: 0: no. 1: yes. Default value: 1.
        self.redirection = redirection
        # The time threshold that is used to define a slow element. Unit: milliseconds. Default value: 5000. Minimum value: 1. Maximum value: 300000.
        self.slow_element_threshold = slow_element_threshold
        # The URL of the website.
        # 
        # This parameter is required.
        self.target_url = target_url
        # An arbitrary string in the source code of the page for verification. If the source code returned by the client contains a string that is in the blacklist, the 650 error code is reported, which indicates that the string fails to be verified. Separate multiple strings with vertical bars (|).
        self.verify_string_blacklist = verify_string_blacklist
        # An arbitrary string in the source code of the page for verification. If the source code returned by the client contains a string that is not in the whitelist, the 650 error code is reported, which indicates that the string fails to be verified. Separate multiple strings with vertical bars (|).
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

class CreateTimingSyntheticTaskRequestMonitorConfStream(DaraModel):
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
        # The custom header. Format: JSON map.
        self.custom_header_content = custom_header_content
        # The player. Default value: 12. Valid values:
        # 
        # *   12: VLC
        # *   2: Flash Player
        self.player_type = player_type
        # The address type of the resource. Valid values:
        # 
        # *   1: resource URL
        # *   0 (default): page URL
        self.stream_address_type = stream_address_type
        # The monitoring duration. Unit: seconds. Maximum and default value: 60.
        self.stream_monitor_timeout = stream_monitor_timeout
        # Specifies whether the resource is a video or audio. Valid values: 0: video. 1: audio.
        self.stream_type = stream_type
        # The resource URL of the streaming media.
        self.target_url = target_url
        # The whitelisted objects that are used to avoid DNS hijacking. The objects can be IP addresses, wildcard mask, subnet mask, or CNAME records. Separate multiple objects with vertical bars (|). Example: www.aliyun.com:203.0.3.55|203.3.44.67. It indicates that all IP addresses that belong to the www.aliyun.com domain name except 203.0.3.55 and 203.3.44.67 are hijacked.
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

class CreateTimingSyntheticTaskRequestMonitorConfNetTCP(DaraModel):
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
        # The number of TCP connections that are established. Minimum value: 1. Maximum value: 16. Default value: 4.
        self.connect_times = connect_times
        # The interval at which TCP connections are established. Unit: milliseconds. Minimum value: 200. Maximum value: 10000. Default value: 200.
        self.interval = interval
        # The IP address of the destination host.
        # 
        # This parameter is required.
        self.target_url = target_url
        # The timeout period for the TCP synthetic test. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 20000.
        self.timeout = timeout
        # Specifies whether to enable the tracert command. Default value: true.
        self.tracert_enable = tracert_enable
        # The maximum number of hops for the tracert command. Minimum value: 1. Maximum value: 128. Default value: 20.
        self.tracert_num_max = tracert_num_max
        # The timeout period of the tracert command. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 60000.
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

class CreateTimingSyntheticTaskRequestMonitorConfNetICMP(DaraModel):
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
        # The size of each ICMP packet. Unit: bytes. Valid values: 32, 64, 128, 256, 512, 1024, 1080, and 1450.
        self.package_size = package_size
        # Specifies whether to split ICMP packets. Default value: true.
        self.split_package = split_package
        # The destination IP address or domain name.
        # 
        # This parameter is required.
        self.target_url = target_url
        # The timeout period for the ICMP synthetic test. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 20000.
        self.timeout = timeout
        # Specifies whether to enable the tracert command. Default value: true.
        self.tracert_enable = tracert_enable
        # The maximum number of hops for the tracert command. Minimum value: 1. Maximum value: 128. Default value: 20.
        self.tracert_num_max = tracert_num_max
        # The timeout period of the tracert command. Unit: milliseconds. Minimum value: 1000. Maximum value: 300000. Default value: 60000.
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

class CreateTimingSyntheticTaskRequestMonitorConfNetDNS(DaraModel):
    def __init__(
        self,
        dns_server_ip_type: int = None,
        ns_server: str = None,
        query_method: int = None,
        target_url: str = None,
        timeout: int = None,
    ):
        # The IP version of the DNS server.
        # 
        # *   0 (default): IPv4.
        # *   1: IPv6.
        # *   2: A version is automatically selected.
        self.dns_server_ip_type = dns_server_ip_type
        # The IP address of the DNS server. Default value: 114.114.114.114.
        self.ns_server = ns_server
        # The DNS query method. Valid values:
        # 
        # *   0 (default): recursive
        # *   1: iterative
        self.query_method = query_method
        # The destination domain name.
        # 
        # This parameter is required.
        self.target_url = target_url
        # The timeout period for the DNS synthetic test. Unit: milliseconds. Minimum value: 1000. Maximum value: 45000. Default value: 5000.
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

class CreateTimingSyntheticTaskRequestMonitorConfFileDownload(DaraModel):
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
        # Unit: milliseconds. Minimum value: 1000. Maximum value: 120000. Default value: 5000.
        self.connection_timeout = connection_timeout
        # The content of the custom request header.
        self.custom_header_content = custom_header_content
        # The kernel type. Valid values:
        # 
        # *   1: curl
        # *   0: WinInet
        # 
        # Default value: 1
        self.download_kernel = download_kernel
        # Specifies whether to ignore CA certificate authentication errors. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_auth_error = ignore_certificate_auth_error
        # Specifies whether to ignore certificate revocation errors. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_canceled_error = ignore_certificate_canceled_error
        # Specifies whether to ignore certificate invalidity. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_out_of_date_error = ignore_certificate_out_of_date_error
        # Specifies whether to ignore certificate status errors. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_status_error = ignore_certificate_status_error
        # Specifies whether to ignore certificate incredibility. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_untrustworthy_error = ignore_certificate_untrustworthy_error
        # Specifies whether to ignore certificate usage errors. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_certificate_using_error = ignore_certificate_using_error
        # Specifies whether to ignore host invalidity. Valid values: 0: no. 1: yes. Default value: 1.
        self.ignore_invalid_host_error = ignore_invalid_host_error
        # The monitoring timeout period. Unit: milliseconds. Minimum value: 1000. Maximum value: 120000. Default value: 60000.
        self.monitor_timeout = monitor_timeout
        # The QUIC protocol type. Valid values:
        # 
        # *   1: HTTP/1
        # *   2: HTTP/2
        # *   3: HTTP/3
        # 
        # Default value: 1
        self.quick_protocol = quick_protocol
        # Specifies whether to support redirection. Valid values: 0: no. 1: yes. Default value: 1.
        self.redirection = redirection
        # The URL that is used to download the file.
        # 
        # This parameter is required.
        self.target_url = target_url
        # The maximum file size of a single transfer. Unit: KB. Minimum value: 1. Maximum value: 20480. Valid values: 2048.
        self.transmission_size = transmission_size
        # The keyword that is used in verification.
        self.validate_keywords = validate_keywords
        # The verification method. Valid values:
        # 
        # *   0: no verification
        # *   1: string verification
        # *   2: MD5 verification
        self.verify_way = verify_way
        # The whitelisted objects that are used to avoid DNS hijacking. The objects can be IP addresses, wildcard mask, subnet mask, or CNAME records. Separate multiple objects with vertical bars (|). Example: www.aliyun.com:203.0.3.55|203.3.44.67. It indicates that all IP addresses that belong to the www.aliyun.com domain name except 203.0.3.55 and 203.3.44.67 are hijacked.
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

class CreateTimingSyntheticTaskRequestMonitorConfApiHTTP(DaraModel):
    def __init__(
        self,
        check_cert: bool = None,
        connect_timeout: int = None,
        method: str = None,
        protocol_alpn_protocol: int = None,
        request_body: main_models.CreateTimingSyntheticTaskRequestMonitorConfApiHTTPRequestBody = None,
        request_headers: Dict[str, str] = None,
        target_url: str = None,
        timeout: int = None,
    ):
        # Specifies whether to verify the certificate. Default value: no.
        self.check_cert = check_cert
        # The connection timeout period. Unit: milliseconds. Default value: 5000. Minimum value: 1000. Maximum value: 300000.
        self.connect_timeout = connect_timeout
        # The request method. Valid values: GET and POST.
        self.method = method
        # The ALPN protocol version. You can configure this parameter when you perform an HTTPS synthetic test on a WAP mobile client. Valid values:
        # 
        # 0: default
        # 
        # 1: http/1.1
        # 
        # 2: h2
        # 
        # 3: disables the ALPN protocol
        self.protocol_alpn_protocol = protocol_alpn_protocol
        # The HTTP request body.
        self.request_body = request_body
        # The HTTP request header.
        self.request_headers = request_headers
        # The URL or request path for synthetic monitoring.
        # 
        # This parameter is required.
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
            temp_model = main_models.CreateTimingSyntheticTaskRequestMonitorConfApiHTTPRequestBody()
            self.request_body = temp_model.from_map(m.get('RequestBody'))

        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class CreateTimingSyntheticTaskRequestMonitorConfApiHTTPRequestBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        type: str = None,
    ):
        # The content of the request body. Format: JSON string. The parameter is required if the Type parameter is set to text/plain, application/json, application/xml, or text/html. Format: JSON string.
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

class CreateTimingSyntheticTaskRequestCustomPeriod(DaraModel):
    def __init__(
        self,
        end_hour: int = None,
        start_hour: int = None,
    ):
        # The custom host settings.
        # 
        # This parameter is required.
        self.end_hour = end_hour
        # The list of hosts.
        # 
        # This parameter is required.
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

class CreateTimingSyntheticTaskRequestCommonSetting(DaraModel):
    def __init__(
        self,
        custom_host: main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomHost = None,
        custom_prometheus_setting: main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomPrometheusSetting = None,
        custom_vpcsetting: main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomVPCSetting = None,
        ip_type: int = None,
        is_open_trace: bool = None,
        monitor_samples: int = None,
        trace_client_type: int = None,
        xtrace_region: str = None,
    ):
        # The custom host settings.
        self.custom_host = custom_host
        # The reserved parameters.
        self.custom_prometheus_setting = custom_prometheus_setting
        # The information about the virtual private cloud (VPC). If the destination URL is an Alibaba Cloud internal endpoint, you need to configure a VPC.
        self.custom_vpcsetting = custom_vpcsetting
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4.
        # *   2: IPv6.
        self.ip_type = ip_type
        # Specifies whether to enable tracing.
        self.is_open_trace = is_open_trace
        # Specifies whether to evenly distribute monitoring samples. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.monitor_samples = monitor_samples
        # The type of the client for tracing. Valid values:
        # 
        # *   0: ARMS agent
        # *   1: OpenTelemetry
        # *   2: Jaeger
        self.trace_client_type = trace_client_type
        # The region to which trace data is reported.
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
            temp_model = main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomHost()
            self.custom_host = temp_model.from_map(m.get('CustomHost'))

        if m.get('CustomPrometheusSetting') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomPrometheusSetting()
            self.custom_prometheus_setting = temp_model.from_map(m.get('CustomPrometheusSetting'))

        if m.get('CustomVPCSetting') is not None:
            temp_model = main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomVPCSetting()
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

class CreateTimingSyntheticTaskRequestCommonSettingCustomVPCSetting(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        secure_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the security group to which the client belongs. The security group specifies the inbound and outbound rules of the client for the VPC. You need to allow the security group to which the client belongs to access the security group to which the VPC belongs. Otherwise, the client cannot access resources in the VPC.
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

class CreateTimingSyntheticTaskRequestCommonSettingCustomPrometheusSetting(DaraModel):
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

class CreateTimingSyntheticTaskRequestCommonSettingCustomHost(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomHostHosts] = None,
        select_type: int = None,
    ):
        # The list of hosts.
        # 
        # This parameter is required.
        self.hosts = hosts
        # The selection mode. Valid values:
        # 
        # *   0: random
        # *   1: polling
        # 
        # This parameter is required.
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
                temp_model = main_models.CreateTimingSyntheticTaskRequestCommonSettingCustomHostHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        return self

class CreateTimingSyntheticTaskRequestCommonSettingCustomHostHosts(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_type: int = None,
        ips: List[str] = None,
    ):
        # The domain name.
        # 
        # This parameter is required.
        self.domain = domain
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4.
        # *   2: IPv6.
        # 
        # This parameter is required.
        self.ip_type = ip_type
        # The list of IP addresses.
        # 
        # This parameter is required.
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

class CreateTimingSyntheticTaskRequestAvailableAssertions(DaraModel):
    def __init__(
        self,
        expect: str = None,
        operator: str = None,
        target: str = None,
        type: str = None,
    ):
        # The expected value.
        # 
        # This parameter is required.
        self.expect = expect
        # The condition. gt: greater than. gte: greater than or equal to. lt: less than. lte: less than or equal to. eq: equal to. neq: not equal to. ctn: contain. nctn: does not contain. exist: exist. n_exist: does not exist. belong: belong to. n_belong: does not belong to. reg_match: regular expression.
        # 
        # This parameter is required.
        self.operator = operator
        # The check target. If you set the type parameter to HttpResCode, HttpResBody, or HttpResponseTime, you do not need to set the target parameter. If you set the type parameter to HttpResHead, you must specify the key in the header. If you set the type parameter to HttpResBodyJson, use jsonPath.
        self.target = target
        # The assertion type. Valid values: HttpResCode, HttpResHead, HttpResBody, HttpResBodyJson, HttpResponseTime, IcmpPackLoss (packet loss rate), IcmpPackMaxLatency (maximum packet latency), IcmpPackAvgLatency (average packet latency), TraceRouteHops (number of hops), DnsARecord (A record), DnsCName (CNAME), websiteTTFB (time to first packet), websiteTTLB (time to last packet), websiteFST (first paint time), websiteFFST (first meaningful paint), websiteOnload (full loaded time). For more information, see the following description.
        # 
        # This parameter is required.
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

