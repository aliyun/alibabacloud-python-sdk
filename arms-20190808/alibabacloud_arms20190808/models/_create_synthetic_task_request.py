# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreateSyntheticTaskRequest(DaraModel):
    def __init__(
        self,
        common_param: main_models.CreateSyntheticTaskRequestCommonParam = None,
        download: main_models.CreateSyntheticTaskRequestDownload = None,
        extend_interval: main_models.CreateSyntheticTaskRequestExtendInterval = None,
        interval_time: str = None,
        interval_type: str = None,
        ip_type: int = None,
        monitor_list: List[main_models.CreateSyntheticTaskRequestMonitorList] = None,
        navigation: main_models.CreateSyntheticTaskRequestNavigation = None,
        net: main_models.CreateSyntheticTaskRequestNet = None,
        protocol: main_models.CreateSyntheticTaskRequestProtocol = None,
        region_id: str = None,
        task_name: str = None,
        task_type: int = None,
        update_task: bool = None,
        url: str = None,
    ):
        # The common parameters.
        self.common_param = common_param
        # The file download task.
        self.download = download
        # The frequency.
        self.extend_interval = extend_interval
        # The interval at which synthetic monitoring is performed. Unit: minutes. Valid values:
        # 
        # *   1
        # *   5
        # *   10
        # *   15
        # *   20
        # *   30
        # *   60
        # *   120
        # *   180
        # *   240
        # *   360
        # *   480
        # *   720
        # *   1440
        # 
        # This parameter is required.
        self.interval_time = interval_time
        # The interval type.
        # 
        # *   0: daily
        # *   1: custom frequency
        # 
        # This parameter is required.
        self.interval_type = interval_type
        # The IP address type:
        # 
        # *   0: an automatic IP address
        # *   1: IPv4
        # *   2: IPv6
        # 
        # This parameter is required.
        self.ip_type = ip_type
        # The list of monitoring points.
        # 
        # This parameter is required.
        self.monitor_list = monitor_list
        # The monitoring items that are associated with the browse tasks.
        self.navigation = navigation
        # The network synthetic monitoring task.
        self.net = net
        # The API performance synthetic monitoring task.
        self.protocol = protocol
        # The ID of the region in which the application is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the task. To update a synthetic monitoring task, enter the task name and set the **UpdateTask** parameter to **true**.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The type of the monitoring task. Valid values:
        # 
        # 1.  3: web page performance - IE
        # 2.  34: web Page Performance - Chrome
        # 3.  0: network quality
        # 4.  40: file download
        # 5.  7:API performance
        # 
        # This parameter is required.
        self.task_type = task_type
        # Specifies whether to update existing synthetic monitoring tasks.
        # 
        # *   true: updates existing synthetic monitoring tasks.
        # *   false: creates new synthetic monitoring tasks.
        self.update_task = update_task
        # The URL for synthetic monitoring.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        if self.common_param:
            self.common_param.validate()
        if self.download:
            self.download.validate()
        if self.extend_interval:
            self.extend_interval.validate()
        if self.monitor_list:
            for v1 in self.monitor_list:
                 if v1:
                    v1.validate()
        if self.navigation:
            self.navigation.validate()
        if self.net:
            self.net.validate()
        if self.protocol:
            self.protocol.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_param is not None:
            result['CommonParam'] = self.common_param.to_map()

        if self.download is not None:
            result['Download'] = self.download.to_map()

        if self.extend_interval is not None:
            result['ExtendInterval'] = self.extend_interval.to_map()

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.interval_type is not None:
            result['IntervalType'] = self.interval_type

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        result['MonitorList'] = []
        if self.monitor_list is not None:
            for k1 in self.monitor_list:
                result['MonitorList'].append(k1.to_map() if k1 else None)

        if self.navigation is not None:
            result['Navigation'] = self.navigation.to_map()

        if self.net is not None:
            result['Net'] = self.net.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.update_task is not None:
            result['UpdateTask'] = self.update_task

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonParam') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestCommonParam()
            self.common_param = temp_model.from_map(m.get('CommonParam'))

        if m.get('Download') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestDownload()
            self.download = temp_model.from_map(m.get('Download'))

        if m.get('ExtendInterval') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestExtendInterval()
            self.extend_interval = temp_model.from_map(m.get('ExtendInterval'))

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('IntervalType') is not None:
            self.interval_type = m.get('IntervalType')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        self.monitor_list = []
        if m.get('MonitorList') is not None:
            for k1 in m.get('MonitorList'):
                temp_model = main_models.CreateSyntheticTaskRequestMonitorList()
                self.monitor_list.append(temp_model.from_map(k1))

        if m.get('Navigation') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestNavigation()
            self.navigation = temp_model.from_map(m.get('Navigation'))

        if m.get('Net') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestNet()
            self.net = temp_model.from_map(m.get('Net'))

        if m.get('Protocol') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestProtocol()
            self.protocol = temp_model.from_map(m.get('Protocol'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('UpdateTask') is not None:
            self.update_task = m.get('UpdateTask')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class CreateSyntheticTaskRequestProtocol(DaraModel):
    def __init__(
        self,
        character_encoding: int = None,
        custom_host: int = None,
        custom_host_ip: str = None,
        protocol_connection_time: int = None,
        protocol_monitor_timeout: str = None,
        received_data_size: int = None,
        request_content: main_models.CreateSyntheticTaskRequestProtocolRequestContent = None,
        verify_content: str = None,
        verify_way: int = None,
    ):
        # The encoding format.
        # 
        # *   0: UTF-8
        # *   1: GBK
        # *   2: GB2312
        # *   3: Unicode
        self.character_encoding = character_encoding
        # The custom host mode.
        # 
        # *   1: round robin
        # *   0: random
        self.custom_host = custom_host
        # The custom host IP address. You can enter multiple IP addresses. Separate the IP addresses with commas (,).
        self.custom_host_ip = custom_host_ip
        # The connection timeout period of the protocol. Unit: seconds.
        self.protocol_connection_time = protocol_connection_time
        # The timeout period of API performance synthetic monitoring. Unit: seconds.
        self.protocol_monitor_timeout = protocol_monitor_timeout
        # The size of the received data. This parameter is required when you set the value of the VerifyWay parameter to 2.
        self.received_data_size = received_data_size
        # The request content, including the request header and request body.
        self.request_content = request_content
        # The verification string.
        self.verify_content = verify_content
        # The method that is used to verify the response content.
        # 
        # *   0: no verification.
        # *   1: exact match with the verification string.
        # *   2: partial match with the verification string.
        # *   3: MD5 verification.
        self.verify_way = verify_way

    def validate(self):
        if self.request_content:
            self.request_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_encoding is not None:
            result['CharacterEncoding'] = self.character_encoding

        if self.custom_host is not None:
            result['CustomHost'] = self.custom_host

        if self.custom_host_ip is not None:
            result['CustomHostIp'] = self.custom_host_ip

        if self.protocol_connection_time is not None:
            result['ProtocolConnectionTime'] = self.protocol_connection_time

        if self.protocol_monitor_timeout is not None:
            result['ProtocolMonitorTimeout'] = self.protocol_monitor_timeout

        if self.received_data_size is not None:
            result['ReceivedDataSize'] = self.received_data_size

        if self.request_content is not None:
            result['RequestContent'] = self.request_content.to_map()

        if self.verify_content is not None:
            result['VerifyContent'] = self.verify_content

        if self.verify_way is not None:
            result['VerifyWay'] = self.verify_way

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterEncoding') is not None:
            self.character_encoding = m.get('CharacterEncoding')

        if m.get('CustomHost') is not None:
            self.custom_host = m.get('CustomHost')

        if m.get('CustomHostIp') is not None:
            self.custom_host_ip = m.get('CustomHostIp')

        if m.get('ProtocolConnectionTime') is not None:
            self.protocol_connection_time = m.get('ProtocolConnectionTime')

        if m.get('ProtocolMonitorTimeout') is not None:
            self.protocol_monitor_timeout = m.get('ProtocolMonitorTimeout')

        if m.get('ReceivedDataSize') is not None:
            self.received_data_size = m.get('ReceivedDataSize')

        if m.get('RequestContent') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestProtocolRequestContent()
            self.request_content = temp_model.from_map(m.get('RequestContent'))

        if m.get('VerifyContent') is not None:
            self.verify_content = m.get('VerifyContent')

        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')

        return self

class CreateSyntheticTaskRequestProtocolRequestContent(DaraModel):
    def __init__(
        self,
        body: main_models.CreateSyntheticTaskRequestProtocolRequestContentBody = None,
        header: List[main_models.CreateSyntheticTaskRequestProtocolRequestContentHeader] = None,
        method: str = None,
    ):
        # The custom body of a request to initiate an API performance synthetic monitoring task.
        self.body = body
        # The custom header of a request to initiate an API performance synthetic monitoring task.
        self.header = header
        # The request method.
        # 
        # *   POST
        # *   GET
        self.method = method

    def validate(self):
        if self.body:
            self.body.validate()
        if self.header:
            for v1 in self.header:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        result['Header'] = []
        if self.header is not None:
            for k1 in self.header:
                result['Header'].append(k1.to_map() if k1 else None)

        if self.method is not None:
            result['Method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.CreateSyntheticTaskRequestProtocolRequestContentBody()
            self.body = temp_model.from_map(m.get('Body'))

        self.header = []
        if m.get('Header') is not None:
            for k1 in m.get('Header'):
                temp_model = main_models.CreateSyntheticTaskRequestProtocolRequestContentHeader()
                self.header.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        return self

class CreateSyntheticTaskRequestProtocolRequestContentHeader(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the request header.
        self.key = key
        # The value of the request header.
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

class CreateSyntheticTaskRequestProtocolRequestContentBody(DaraModel):
    def __init__(
        self,
        form_data: List[main_models.CreateSyntheticTaskRequestProtocolRequestContentBodyFormData] = None,
        language: str = None,
        mode: str = None,
        raw: str = None,
        url_encoding: List[main_models.CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding] = None,
    ):
        # The data that is passed when the **Mode** parameter is set to **form-data**.
        self.form_data = form_data
        # The language that is selected when the Mode parameter is set to raw.
        # 
        # *   json
        # *   xml
        # *   javascript
        # *   html
        # *   text
        self.language = language
        # The data type of the content.
        # 
        # *   form-data
        # *   x-www-form-urlencoded
        # *   raw
        self.mode = mode
        # The data that is passed when the **Mode** parameter is set to **raw**.
        self.raw = raw
        # The data that is passed when the **Mode** parameter is set to **x-www-form-urlencoded**.
        self.url_encoding = url_encoding

    def validate(self):
        if self.form_data:
            for v1 in self.form_data:
                 if v1:
                    v1.validate()
        if self.url_encoding:
            for v1 in self.url_encoding:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FormData'] = []
        if self.form_data is not None:
            for k1 in self.form_data:
                result['FormData'].append(k1.to_map() if k1 else None)

        if self.language is not None:
            result['Language'] = self.language

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.raw is not None:
            result['Raw'] = self.raw

        result['UrlEncoding'] = []
        if self.url_encoding is not None:
            for k1 in self.url_encoding:
                result['UrlEncoding'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.form_data = []
        if m.get('FormData') is not None:
            for k1 in m.get('FormData'):
                temp_model = main_models.CreateSyntheticTaskRequestProtocolRequestContentBodyFormData()
                self.form_data.append(temp_model.from_map(k1))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Raw') is not None:
            self.raw = m.get('Raw')

        self.url_encoding = []
        if m.get('UrlEncoding') is not None:
            for k1 in m.get('UrlEncoding'):
                temp_model = main_models.CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding()
                self.url_encoding.append(temp_model.from_map(k1))

        return self

class CreateSyntheticTaskRequestProtocolRequestContentBodyUrlEncoding(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of **x-www-form-urlencoded**.
        self.key = key
        # The value of **x-www-form-urlencoded**.
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

class CreateSyntheticTaskRequestProtocolRequestContentBodyFormData(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of **form-data**.
        self.key = key
        # The value of **form-data**.
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

class CreateSyntheticTaskRequestNet(DaraModel):
    def __init__(
        self,
        net_dnsns: str = None,
        net_dnsquery_method: int = None,
        net_dnsserver: int = None,
        net_dnsswitch: int = None,
        net_dnstimeout: int = None,
        net_dig_switch: int = None,
        net_icmpactive: int = None,
        net_icmpdata_cut: int = None,
        net_icmpinterval: int = None,
        net_icmpnum: int = None,
        net_icmpsize: int = None,
        net_icmpswitch: int = None,
        net_icmptimeout: int = None,
        net_trace_route_num: int = None,
        net_trace_route_switch: int = None,
        net_trace_route_timeout: int = None,
        white_list: str = None,
    ):
        # The DNS server.
        self.net_dnsns = net_dnsns
        # The DNS query method. Valid values:
        # 
        # *   1: recursion
        # *   2: iteration
        self.net_dnsquery_method = net_dnsquery_method
        # The IP address type of the DNS server.
        # 
        # *   0: IPv4
        # *   1: IPv6
        # *   2: an automatic IP address
        self.net_dnsserver = net_dnsserver
        # Specifies whether to enable domain name system (DNS) monitoring.
        # 
        # *   0: Off.
        # *   1: On. You must set DNS parameters if you want to enable DNS monitoring.
        self.net_dnsswitch = net_dnsswitch
        # The timeout period of DNS monitoring. Default value: 5 seconds. Valid values: 0 to 45 seconds.
        self.net_dnstimeout = net_dnstimeout
        # Specifies whether to display the data in the DIG format. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.net_dig_switch = net_dig_switch
        # The protocol type. Valid values:
        # 
        # *   0: ICMP
        # *   1: TCP
        self.net_icmpactive = net_icmpactive
        # Specifies whether to split packages.
        # 
        # *   0: no
        # *   1: yes
        self.net_icmpdata_cut = net_icmpdata_cut
        # The interval at which the network synthetic monitoring task is executed. Unit: seconds.
        self.net_icmpinterval = net_icmpinterval
        # The number of packages.
        self.net_icmpnum = net_icmpnum
        # The package size.
        self.net_icmpsize = net_icmpsize
        # Specifies whether to enable ping monitoring.
        # 
        # *   0: Off.
        # *   1: On. You must set Internet control message protocol (ICMP) parameters if you want to enable ping monitoring.
        self.net_icmpswitch = net_icmpswitch
        # The timeout period of Ping monitoring.
        self.net_icmptimeout = net_icmptimeout
        # The maximum number of active monitoring points.
        self.net_trace_route_num = net_trace_route_num
        # Specifies whether to enable tracert monitoring.
        # 
        # *   0: Off.
        # *   1: On. You must set the tracert parameters if you want to enable tracert monitoring.
        self.net_trace_route_switch = net_trace_route_switch
        # The timeout period of tracert monitoring. Valid values: 0 to 300 seconds.
        self.net_trace_route_timeout = net_trace_route_timeout
        # The whitelist for DNS hijacking. The format is `Domain name: Matching rule`.
        # 
        # >  Wireless application protocol (WAP) networks do not support DNS hijacking.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_dnsns is not None:
            result['NetDNSNs'] = self.net_dnsns

        if self.net_dnsquery_method is not None:
            result['NetDNSQueryMethod'] = self.net_dnsquery_method

        if self.net_dnsserver is not None:
            result['NetDNSServer'] = self.net_dnsserver

        if self.net_dnsswitch is not None:
            result['NetDNSSwitch'] = self.net_dnsswitch

        if self.net_dnstimeout is not None:
            result['NetDNSTimeout'] = self.net_dnstimeout

        if self.net_dig_switch is not None:
            result['NetDigSwitch'] = self.net_dig_switch

        if self.net_icmpactive is not None:
            result['NetICMPActive'] = self.net_icmpactive

        if self.net_icmpdata_cut is not None:
            result['NetICMPDataCut'] = self.net_icmpdata_cut

        if self.net_icmpinterval is not None:
            result['NetICMPInterval'] = self.net_icmpinterval

        if self.net_icmpnum is not None:
            result['NetICMPNum'] = self.net_icmpnum

        if self.net_icmpsize is not None:
            result['NetICMPSize'] = self.net_icmpsize

        if self.net_icmpswitch is not None:
            result['NetICMPSwitch'] = self.net_icmpswitch

        if self.net_icmptimeout is not None:
            result['NetICMPTimeout'] = self.net_icmptimeout

        if self.net_trace_route_num is not None:
            result['NetTraceRouteNum'] = self.net_trace_route_num

        if self.net_trace_route_switch is not None:
            result['NetTraceRouteSwitch'] = self.net_trace_route_switch

        if self.net_trace_route_timeout is not None:
            result['NetTraceRouteTimeout'] = self.net_trace_route_timeout

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetDNSNs') is not None:
            self.net_dnsns = m.get('NetDNSNs')

        if m.get('NetDNSQueryMethod') is not None:
            self.net_dnsquery_method = m.get('NetDNSQueryMethod')

        if m.get('NetDNSServer') is not None:
            self.net_dnsserver = m.get('NetDNSServer')

        if m.get('NetDNSSwitch') is not None:
            self.net_dnsswitch = m.get('NetDNSSwitch')

        if m.get('NetDNSTimeout') is not None:
            self.net_dnstimeout = m.get('NetDNSTimeout')

        if m.get('NetDigSwitch') is not None:
            self.net_dig_switch = m.get('NetDigSwitch')

        if m.get('NetICMPActive') is not None:
            self.net_icmpactive = m.get('NetICMPActive')

        if m.get('NetICMPDataCut') is not None:
            self.net_icmpdata_cut = m.get('NetICMPDataCut')

        if m.get('NetICMPInterval') is not None:
            self.net_icmpinterval = m.get('NetICMPInterval')

        if m.get('NetICMPNum') is not None:
            self.net_icmpnum = m.get('NetICMPNum')

        if m.get('NetICMPSize') is not None:
            self.net_icmpsize = m.get('NetICMPSize')

        if m.get('NetICMPSwitch') is not None:
            self.net_icmpswitch = m.get('NetICMPSwitch')

        if m.get('NetICMPTimeout') is not None:
            self.net_icmptimeout = m.get('NetICMPTimeout')

        if m.get('NetTraceRouteNum') is not None:
            self.net_trace_route_num = m.get('NetTraceRouteNum')

        if m.get('NetTraceRouteSwitch') is not None:
            self.net_trace_route_switch = m.get('NetTraceRouteSwitch')

        if m.get('NetTraceRouteTimeout') is not None:
            self.net_trace_route_timeout = m.get('NetTraceRouteTimeout')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class CreateSyntheticTaskRequestNavigation(DaraModel):
    def __init__(
        self,
        dnshijack_white_list: str = None,
        element_blacklist: str = None,
        execute_active_x: int = None,
        execute_application: int = None,
        execute_script: int = None,
        filter_invalid_ip: int = None,
        flow_hijack_jump_times: int = None,
        flow_hijack_logo: str = None,
        monitor_timeout: str = None,
        nav_automatic_scrolling: str = None,
        nav_custom_header: str = None,
        nav_custom_header_content: str = None,
        nav_custom_host: int = None,
        nav_custom_host_ip: str = None,
        nav_disable_cache: int = None,
        nav_disable_compression: str = None,
        nav_ignore_certificate_error: int = None,
        nav_redirection: int = None,
        nav_return_element: int = None,
        page_tamper: str = None,
        process_name: str = None,
        quicdomain: str = None,
        quicversion: int = None,
        request_header: int = None,
        response_header: int = None,
        slow_element_threshold: float = None,
        verify_string_blacklist: str = None,
        verify_string_white_list: str = None,
        wait_completion_time: float = None,
    ):
        # The whitelist for DNS hijacking.
        self.dnshijack_white_list = dnshijack_white_list
        # The element blacklist.
        self.element_blacklist = element_blacklist
        # Specifies whether to execute ActiveX.
        # 
        # *   3: yes
        # *   0: no
        # 
        # >  This parameter is supported only by IE Full Elements.
        self.execute_active_x = execute_active_x
        # Specifies whether to run applets.
        # 
        # *   1: yes
        # *   0: no
        # 
        # >  This parameter is supported only by IE Full Elements.
        self.execute_application = execute_application
        # Specifies whether to execute scripts.
        # 
        # *   1: yes
        # *   0: no
        # 
        # >  This parameter is supported only by IE Full Elements.
        self.execute_script = execute_script
        # Specifies whether to filter invalid IP addresses.
        # 
        # *   1: no
        # *   0: yes
        self.filter_invalid_ip = filter_invalid_ip
        # The element that is used in DNS hijacking.
        self.flow_hijack_jump_times = flow_hijack_jump_times
        # The tag that is used in DNS hijacking.
        self.flow_hijack_logo = flow_hijack_logo
        # The timeout period of monitoring. Unit: seconds.
        self.monitor_timeout = monitor_timeout
        # Specifies whether to automatically scroll up and down the screen to load a page.
        # 
        # *   1: yes
        # *   0: no
        self.nav_automatic_scrolling = nav_automatic_scrolling
        # The method that is used to customize the header. Valid values:
        # 
        # *   0: disables the customer header.
        # *   1: modifies the first package.
        # *   2: modifies all packages.
        self.nav_custom_header = nav_custom_header
        # The format of the custom header. You can specify multiple fields. Separate the fields with vertical bars (|).
        self.nav_custom_header_content = nav_custom_header_content
        # The custom host mode.
        # 
        # *   1: round robin
        # *   0: random
        self.nav_custom_host = nav_custom_host
        # The custom host IP address. You can enter multiple IP addresses. Separate the IP addresses with commas (,).
        self.nav_custom_host_ip = nav_custom_host_ip
        # Specifies whether to disable caching.
        # 
        # *   1: disable
        # *   0: enable
        self.nav_disable_cache = nav_disable_cache
        # Specifies whether to enable the feature of using the Accept-Encoding field to determine whether to accept compressed files.
        # 
        # *   1: disable
        # *   0: enable
        self.nav_disable_compression = nav_disable_compression
        # Specifies whether to ignore certificate errors during certificate verification in the SSL handshake and continue browsing.
        # 
        # *   1: ignore
        # *   0: does not ignore
        self.nav_ignore_certificate_error = nav_ignore_certificate_error
        # Specifies whether to continue browsing after a redirection occurs.
        # 
        # *   1: yes
        # *   0: no
        self.nav_redirection = nav_redirection
        # Specifies whether to return the elements on the page.
        # 
        # *   1: no. Returns the basic document data.
        # *   2: yes. Returns all document data.
        self.nav_return_element = nav_return_element
        # The web page defacement.
        self.page_tamper = page_tamper
        # The process ID.
        self.process_name = process_name
        # The domain name of the QUIC request element.
        # 
        # >  This parameter is supported by all elements of only Chrome
        self.quicdomain = quicdomain
        # The Quick UDP Internet Connections (QUIC) protocol version. Default value: 0. Valid values:
        # 
        # *
        # *   35
        # *   39
        # *   43
        # *   44
        # 
        # >  This parameter is supported by all elements of only Chrome
        self.quicversion = quicversion
        # Specifies whether to return the request header.
        # 
        # *   0: does not return the response header.
        # *   1: returns the basic document header.
        # *   2: returns all headers.
        self.request_header = request_header
        # The method that is used to return the response header. Valid values:
        # 
        # *   0: does not return the response header.
        # *   1: returns the basic document header.
        # *   2: returns all headers.
        self.response_header = response_header
        # The time threshold that is used to define a slow element. Unit: seconds.
        self.slow_element_threshold = slow_element_threshold
        # The blacklist for string verification.
        self.verify_string_blacklist = verify_string_blacklist
        # The whitelist for string verification.
        self.verify_string_white_list = verify_string_white_list
        # The timeout period of waiting for the monitoring to complete.
        self.wait_completion_time = wait_completion_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnshijack_white_list is not None:
            result['DNSHijackWhiteList'] = self.dnshijack_white_list

        if self.element_blacklist is not None:
            result['ElementBlacklist'] = self.element_blacklist

        if self.execute_active_x is not None:
            result['ExecuteActiveX'] = self.execute_active_x

        if self.execute_application is not None:
            result['ExecuteApplication'] = self.execute_application

        if self.execute_script is not None:
            result['ExecuteScript'] = self.execute_script

        if self.filter_invalid_ip is not None:
            result['FilterInvalidIP'] = self.filter_invalid_ip

        if self.flow_hijack_jump_times is not None:
            result['FlowHijackJumpTimes'] = self.flow_hijack_jump_times

        if self.flow_hijack_logo is not None:
            result['FlowHijackLogo'] = self.flow_hijack_logo

        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout

        if self.nav_automatic_scrolling is not None:
            result['NavAutomaticScrolling'] = self.nav_automatic_scrolling

        if self.nav_custom_header is not None:
            result['NavCustomHeader'] = self.nav_custom_header

        if self.nav_custom_header_content is not None:
            result['NavCustomHeaderContent'] = self.nav_custom_header_content

        if self.nav_custom_host is not None:
            result['NavCustomHost'] = self.nav_custom_host

        if self.nav_custom_host_ip is not None:
            result['NavCustomHostIp'] = self.nav_custom_host_ip

        if self.nav_disable_cache is not None:
            result['NavDisableCache'] = self.nav_disable_cache

        if self.nav_disable_compression is not None:
            result['NavDisableCompression'] = self.nav_disable_compression

        if self.nav_ignore_certificate_error is not None:
            result['NavIgnoreCertificateError'] = self.nav_ignore_certificate_error

        if self.nav_redirection is not None:
            result['NavRedirection'] = self.nav_redirection

        if self.nav_return_element is not None:
            result['NavReturnElement'] = self.nav_return_element

        if self.page_tamper is not None:
            result['PageTamper'] = self.page_tamper

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.quicdomain is not None:
            result['QUICDomain'] = self.quicdomain

        if self.quicversion is not None:
            result['QUICVersion'] = self.quicversion

        if self.request_header is not None:
            result['RequestHeader'] = self.request_header

        if self.response_header is not None:
            result['ResponseHeader'] = self.response_header

        if self.slow_element_threshold is not None:
            result['SlowElementThreshold'] = self.slow_element_threshold

        if self.verify_string_blacklist is not None:
            result['VerifyStringBlacklist'] = self.verify_string_blacklist

        if self.verify_string_white_list is not None:
            result['VerifyStringWhiteList'] = self.verify_string_white_list

        if self.wait_completion_time is not None:
            result['WaitCompletionTime'] = self.wait_completion_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNSHijackWhiteList') is not None:
            self.dnshijack_white_list = m.get('DNSHijackWhiteList')

        if m.get('ElementBlacklist') is not None:
            self.element_blacklist = m.get('ElementBlacklist')

        if m.get('ExecuteActiveX') is not None:
            self.execute_active_x = m.get('ExecuteActiveX')

        if m.get('ExecuteApplication') is not None:
            self.execute_application = m.get('ExecuteApplication')

        if m.get('ExecuteScript') is not None:
            self.execute_script = m.get('ExecuteScript')

        if m.get('FilterInvalidIP') is not None:
            self.filter_invalid_ip = m.get('FilterInvalidIP')

        if m.get('FlowHijackJumpTimes') is not None:
            self.flow_hijack_jump_times = m.get('FlowHijackJumpTimes')

        if m.get('FlowHijackLogo') is not None:
            self.flow_hijack_logo = m.get('FlowHijackLogo')

        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')

        if m.get('NavAutomaticScrolling') is not None:
            self.nav_automatic_scrolling = m.get('NavAutomaticScrolling')

        if m.get('NavCustomHeader') is not None:
            self.nav_custom_header = m.get('NavCustomHeader')

        if m.get('NavCustomHeaderContent') is not None:
            self.nav_custom_header_content = m.get('NavCustomHeaderContent')

        if m.get('NavCustomHost') is not None:
            self.nav_custom_host = m.get('NavCustomHost')

        if m.get('NavCustomHostIp') is not None:
            self.nav_custom_host_ip = m.get('NavCustomHostIp')

        if m.get('NavDisableCache') is not None:
            self.nav_disable_cache = m.get('NavDisableCache')

        if m.get('NavDisableCompression') is not None:
            self.nav_disable_compression = m.get('NavDisableCompression')

        if m.get('NavIgnoreCertificateError') is not None:
            self.nav_ignore_certificate_error = m.get('NavIgnoreCertificateError')

        if m.get('NavRedirection') is not None:
            self.nav_redirection = m.get('NavRedirection')

        if m.get('NavReturnElement') is not None:
            self.nav_return_element = m.get('NavReturnElement')

        if m.get('PageTamper') is not None:
            self.page_tamper = m.get('PageTamper')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('QUICDomain') is not None:
            self.quicdomain = m.get('QUICDomain')

        if m.get('QUICVersion') is not None:
            self.quicversion = m.get('QUICVersion')

        if m.get('RequestHeader') is not None:
            self.request_header = m.get('RequestHeader')

        if m.get('ResponseHeader') is not None:
            self.response_header = m.get('ResponseHeader')

        if m.get('SlowElementThreshold') is not None:
            self.slow_element_threshold = m.get('SlowElementThreshold')

        if m.get('VerifyStringBlacklist') is not None:
            self.verify_string_blacklist = m.get('VerifyStringBlacklist')

        if m.get('VerifyStringWhiteList') is not None:
            self.verify_string_white_list = m.get('VerifyStringWhiteList')

        if m.get('WaitCompletionTime') is not None:
            self.wait_completion_time = m.get('WaitCompletionTime')

        return self

class CreateSyntheticTaskRequestMonitorList(DaraModel):
    def __init__(
        self,
        city_code: int = None,
        monitor_type: int = None,
        net_service_id: int = None,
    ):
        # The ID of the city to which the monitoring point belongs.
        # 
        # This parameter is required.
        self.city_code = city_code
        # The carrier type:
        # 
        # *   IDC
        # *   LastMilie
        # 
        # This parameter is required.
        self.monitor_type = monitor_type
        # The ID of the carrier.
        # 
        # This parameter is required.
        self.net_service_id = net_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.monitor_type is not None:
            result['MonitorType'] = self.monitor_type

        if self.net_service_id is not None:
            result['NetServiceId'] = self.net_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')

        return self

class CreateSyntheticTaskRequestExtendInterval(DaraModel):
    def __init__(
        self,
        days: List[int] = None,
        end_hour: int = None,
        end_minute: int = None,
        end_time: str = None,
        start_hour: int = None,
        start_minute: int = None,
        start_time: str = None,
    ):
        # The day on which synthetic monitoring is performed.
        self.days = days
        # The hour at which synthetic monitoring ends.
        self.end_hour = end_hour
        # The minute at which synthetic monitoring ends.
        self.end_minute = end_minute
        # The time when synthetic monitoring ends. The format is `yyyy-MM-dd HH`.
        self.end_time = end_time
        # The hour at which synthetic monitoring starts.
        self.start_hour = start_hour
        # The minute at which synthetic monitoring starts.
        self.start_minute = start_minute
        # The time when synthetic monitoring starts. The format is `yyyy-MM-dd HH`.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['Days'] = self.days

        if self.end_hour is not None:
            result['EndHour'] = self.end_hour

        if self.end_minute is not None:
            result['EndMinute'] = self.end_minute

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_hour is not None:
            result['StartHour'] = self.start_hour

        if self.start_minute is not None:
            result['StartMinute'] = self.start_minute

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('EndHour') is not None:
            self.end_hour = m.get('EndHour')

        if m.get('EndMinute') is not None:
            self.end_minute = m.get('EndMinute')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')

        if m.get('StartMinute') is not None:
            self.start_minute = m.get('StartMinute')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateSyntheticTaskRequestDownload(DaraModel):
    def __init__(
        self,
        connection_timeout: float = None,
        download_custom_header_content: str = None,
        download_custom_host: int = None,
        download_custom_host_ip: str = None,
        download_ignore_certificate_error: str = None,
        download_kernel: int = None,
        download_redirection: int = None,
        download_transmission_size: int = None,
        monitor_timeout: int = None,
        quick_protocol: str = None,
        validate_keywords: str = None,
        verify_way: int = None,
        white_list: str = None,
    ):
        # The connection timeout period.
        self.connection_timeout = connection_timeout
        # The items to be ignored in a certificate error. Pass the values of the check boxes that are separated with vertical bars (|).
        self.download_custom_header_content = download_custom_header_content
        # The custom host mode.
        # 
        # *   1: round robin
        # *   0: random
        self.download_custom_host = download_custom_host
        # The custom host IP address. You can enter multiple IP addresses. Separate the IP addresses with commas (,).
        self.download_custom_host_ip = download_custom_host_ip
        # The items to be ignored in a certificate error. Pass the values of the check boxes that are separated with vertical bars (|).
        self.download_ignore_certificate_error = download_ignore_certificate_error
        # The kernel type.
        # 
        # *   1: curl
        # *   0: WinInet
        self.download_kernel = download_kernel
        # Specifies whether to support redirection.
        self.download_redirection = download_redirection
        # The size of the download file. Unit: KB.
        self.download_transmission_size = download_transmission_size
        # The monitoring duration.
        self.monitor_timeout = monitor_timeout
        # The QUIC protocol type.
        # 
        # *   1: http1
        # *   2: http2
        # *   3: http3
        self.quick_protocol = quick_protocol
        # The keyword that is used in verification.
        self.validate_keywords = validate_keywords
        # The verification method.
        # 
        # *   0: no verification
        # *   1: string verification
        # *   2: MD5 verification
        self.verify_way = verify_way
        # The whitelist for DNS hijacking.
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

        if self.download_custom_header_content is not None:
            result['DownloadCustomHeaderContent'] = self.download_custom_header_content

        if self.download_custom_host is not None:
            result['DownloadCustomHost'] = self.download_custom_host

        if self.download_custom_host_ip is not None:
            result['DownloadCustomHostIp'] = self.download_custom_host_ip

        if self.download_ignore_certificate_error is not None:
            result['DownloadIgnoreCertificateError'] = self.download_ignore_certificate_error

        if self.download_kernel is not None:
            result['DownloadKernel'] = self.download_kernel

        if self.download_redirection is not None:
            result['DownloadRedirection'] = self.download_redirection

        if self.download_transmission_size is not None:
            result['DownloadTransmissionSize'] = self.download_transmission_size

        if self.monitor_timeout is not None:
            result['MonitorTimeout'] = self.monitor_timeout

        if self.quick_protocol is not None:
            result['QuickProtocol'] = self.quick_protocol

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

        if m.get('DownloadCustomHeaderContent') is not None:
            self.download_custom_header_content = m.get('DownloadCustomHeaderContent')

        if m.get('DownloadCustomHost') is not None:
            self.download_custom_host = m.get('DownloadCustomHost')

        if m.get('DownloadCustomHostIp') is not None:
            self.download_custom_host_ip = m.get('DownloadCustomHostIp')

        if m.get('DownloadIgnoreCertificateError') is not None:
            self.download_ignore_certificate_error = m.get('DownloadIgnoreCertificateError')

        if m.get('DownloadKernel') is not None:
            self.download_kernel = m.get('DownloadKernel')

        if m.get('DownloadRedirection') is not None:
            self.download_redirection = m.get('DownloadRedirection')

        if m.get('DownloadTransmissionSize') is not None:
            self.download_transmission_size = m.get('DownloadTransmissionSize')

        if m.get('MonitorTimeout') is not None:
            self.monitor_timeout = m.get('MonitorTimeout')

        if m.get('QuickProtocol') is not None:
            self.quick_protocol = m.get('QuickProtocol')

        if m.get('ValidateKeywords') is not None:
            self.validate_keywords = m.get('ValidateKeywords')

        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class CreateSyntheticTaskRequestCommonParam(DaraModel):
    def __init__(
        self,
        alarm_flag: str = None,
        alert_list: List[main_models.CreateSyntheticTaskRequestCommonParamAlertList] = None,
        alert_notifier_id: str = None,
        alert_policy_id: str = None,
        monitor_samples: int = None,
        start_execution_time: int = None,
    ):
        # Specifies whether to create an alert rule.
        # 
        # *   1: creates an alert.
        # *   0: does not create an alert.
        self.alarm_flag = alarm_flag
        # The alert parameters.
        self.alert_list = alert_list
        # The ID of the alert recipient. Separate multiple recipients with commas (,).
        self.alert_notifier_id = alert_notifier_id
        # The ID of the notification policy.
        self.alert_policy_id = alert_policy_id
        # Specifies whether to evenly distribute monitoring samples. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.monitor_samples = monitor_samples
        # The time when execution starts.
        self.start_execution_time = start_execution_time

    def validate(self):
        if self.alert_list:
            for v1 in self.alert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_flag is not None:
            result['AlarmFlag'] = self.alarm_flag

        result['AlertList'] = []
        if self.alert_list is not None:
            for k1 in self.alert_list:
                result['AlertList'].append(k1.to_map() if k1 else None)

        if self.alert_notifier_id is not None:
            result['AlertNotifierId'] = self.alert_notifier_id

        if self.alert_policy_id is not None:
            result['AlertPolicyId'] = self.alert_policy_id

        if self.monitor_samples is not None:
            result['MonitorSamples'] = self.monitor_samples

        if self.start_execution_time is not None:
            result['StartExecutionTime'] = self.start_execution_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmFlag') is not None:
            self.alarm_flag = m.get('AlarmFlag')

        self.alert_list = []
        if m.get('AlertList') is not None:
            for k1 in m.get('AlertList'):
                temp_model = main_models.CreateSyntheticTaskRequestCommonParamAlertList()
                self.alert_list.append(temp_model.from_map(k1))

        if m.get('AlertNotifierId') is not None:
            self.alert_notifier_id = m.get('AlertNotifierId')

        if m.get('AlertPolicyId') is not None:
            self.alert_policy_id = m.get('AlertPolicyId')

        if m.get('MonitorSamples') is not None:
            self.monitor_samples = m.get('MonitorSamples')

        if m.get('StartExecutionTime') is not None:
            self.start_execution_time = m.get('StartExecutionTime')

        return self

class CreateSyntheticTaskRequestCommonParamAlertList(DaraModel):
    def __init__(
        self,
        is_critical: int = None,
        name: str = None,
        symbols: int = None,
    ):
        # Specifies whether the condition must be met.
        self.is_critical = is_critical
        # The name of the alert rule.
        # 
        # For network synthetic monitoring, use the following names:
        # 
        # *   Latency: PING_SET
        # *   Packet loss rate: PING_LOST_RATE
        # *   Hijacking: HIJACKPER
        self.name = name
        # Specifies how the condition is evaluated. Valid values:
        # 
        # *   1: greater than
        # *   0: less than
        self.symbols = symbols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_critical is not None:
            result['IsCritical'] = self.is_critical

        if self.name is not None:
            result['Name'] = self.name

        if self.symbols is not None:
            result['Symbols'] = self.symbols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsCritical') is not None:
            self.is_critical = m.get('IsCritical')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Symbols') is not None:
            self.symbols = m.get('Symbols')

        return self

