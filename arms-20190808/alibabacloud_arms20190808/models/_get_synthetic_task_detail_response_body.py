# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetSyntheticTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_detail: main_models.GetSyntheticTaskDetailResponseBodyTaskDetail = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the task.
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            self.task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskDetail') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetail()
            self.task_detail = temp_model.from_map(m.get('TaskDetail'))

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetail(DaraModel):
    def __init__(
        self,
        common_param: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailCommonParam = None,
        download: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailDownload = None,
        extend_interval: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval = None,
        interval_time: int = None,
        interval_type: int = None,
        ip_type: int = None,
        monitor_list: List[main_models.GetSyntheticTaskDetailResponseBodyTaskDetailMonitorList] = None,
        monitor_list_string: str = None,
        nav: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailNav = None,
        net: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailNet = None,
        protocol: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocol = None,
        task_id: int = None,
        task_name: str = None,
        task_type: int = None,
        url: str = None,
    ):
        # The list of common parameters.
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
        self.interval_time = interval_time
        # The interval type. Valid values:
        # 
        # *   0: daily
        # *   1: custom frequency
        self.interval_type = interval_type
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4.
        # *   2: IPv6.
        self.ip_type = ip_type
        # The detection points.
        self.monitor_list = monitor_list
        # The detection points.
        self.monitor_list_string = monitor_list_string
        # The browser test task.
        self.nav = nav
        # The network synthetic monitoring task.
        self.net = net
        # The synthetic monitoring task of the API performance type.
        self.protocol = protocol
        # The ID of the synthetic monitoring task.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The type of the task. Valid values:
        # 
        # 1.  3: web page performance - IE
        # 2.  34: web page performance - Chrome
        # 3.  0: network quality
        # 4.  40: file download
        # 5.  7: API performance
        self.task_type = task_type
        # The URL for synthetic monitoring.
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
        if self.nav:
            self.nav.validate()
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

        if self.monitor_list_string is not None:
            result['MonitorListString'] = self.monitor_list_string

        if self.nav is not None:
            result['Nav'] = self.nav.to_map()

        if self.net is not None:
            result['Net'] = self.net.to_map()

        if self.protocol is not None:
            result['Protocol'] = self.protocol.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonParam') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailCommonParam()
            self.common_param = temp_model.from_map(m.get('CommonParam'))

        if m.get('Download') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailDownload()
            self.download = temp_model.from_map(m.get('Download'))

        if m.get('ExtendInterval') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval()
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
                temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailMonitorList()
                self.monitor_list.append(temp_model.from_map(k1))

        if m.get('MonitorListString') is not None:
            self.monitor_list_string = m.get('MonitorListString')

        if m.get('Nav') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailNav()
            self.nav = temp_model.from_map(m.get('Nav'))

        if m.get('Net') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailNet()
            self.net = temp_model.from_map(m.get('Net'))

        if m.get('Protocol') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocol()
            self.protocol = temp_model.from_map(m.get('Protocol'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocol(DaraModel):
    def __init__(
        self,
        character_encoding: int = None,
        custom_host: int = None,
        custom_host_ip: str = None,
        protocol_connection_timeout: int = None,
        protocol_monitor_timeout: int = None,
        received_data_size: int = None,
        request_content: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent = None,
        verify_content: str = None,
        verify_way: int = None,
    ):
        # The encoding format. Valid values:
        # 
        # *   0: UTF-8
        # *   1: GBK
        # *   2: GB2312
        # *   3: Unicode
        self.character_encoding = character_encoding
        # The custom host. Valid values:
        # 
        # *   1: round robin
        # *   0: random
        self.custom_host = custom_host
        # The custom IP address of the host. Multiple IP addresses are separated with commas (,).
        self.custom_host_ip = custom_host_ip
        # The timeout period.
        self.protocol_connection_timeout = protocol_connection_timeout
        # The timeout period of API performance monitoring. Unit: seconds.
        self.protocol_monitor_timeout = protocol_monitor_timeout
        # The size of the received data. This parameter is returned when **VerifyWay** is set to 2.
        self.received_data_size = received_data_size
        # The request content, including the header and body.
        self.request_content = request_content
        # The verification string.
        self.verify_content = verify_content
        # The method that is used to verify the response content. Valid values:
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

        if self.protocol_connection_timeout is not None:
            result['ProtocolConnectionTimeout'] = self.protocol_connection_timeout

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

        if m.get('ProtocolConnectionTimeout') is not None:
            self.protocol_connection_timeout = m.get('ProtocolConnectionTimeout')

        if m.get('ProtocolMonitorTimeout') is not None:
            self.protocol_monitor_timeout = m.get('ProtocolMonitorTimeout')

        if m.get('ReceivedDataSize') is not None:
            self.received_data_size = m.get('ReceivedDataSize')

        if m.get('RequestContent') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent()
            self.request_content = temp_model.from_map(m.get('RequestContent'))

        if m.get('VerifyContent') is not None:
            self.verify_content = m.get('VerifyContent')

        if m.get('VerifyWay') is not None:
            self.verify_way = m.get('VerifyWay')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContent(DaraModel):
    def __init__(
        self,
        body: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody = None,
        header: List[main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader] = None,
        method: str = None,
    ):
        # The content of the request body.
        self.body = body
        # The request header.
        self.header = header
        # The request method. Valid values:
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
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody()
            self.body = temp_model.from_map(m.get('Body'))

        self.header = []
        if m.get('Header') is not None:
            for k1 in m.get('Header'):
                temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader()
                self.header.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentHeader(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the header in the request parameters.
        self.key = key
        # The value of the header in the request parameters.
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

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBody(DaraModel):
    def __init__(
        self,
        formdata: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata = None,
        language: str = None,
        mode: str = None,
        raw: str = None,
        urlencoded: main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded = None,
    ):
        # The data content. This parameter is returned when Mode is set to form-data.
        self.formdata = formdata
        # The language used when Mode is set to raw. Valid values:
        # 
        # *   json
        # *   xml
        # *   javascript
        # *   html
        # *   text
        self.language = language
        # The type of the content. Valid values:
        # 
        # *   form-data
        # *   x-www-form-urlencoded
        # *   raw
        self.mode = mode
        # The data content. This parameter is returned when **Mode** is set to **raw**.
        self.raw = raw
        # The URL of the body content.
        self.urlencoded = urlencoded

    def validate(self):
        if self.formdata:
            self.formdata.validate()
        if self.urlencoded:
            self.urlencoded.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.formdata is not None:
            result['Formdata'] = self.formdata.to_map()

        if self.language is not None:
            result['Language'] = self.language

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.raw is not None:
            result['Raw'] = self.raw

        if self.urlencoded is not None:
            result['Urlencoded'] = self.urlencoded.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Formdata') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata()
            self.formdata = temp_model.from_map(m.get('Formdata'))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Raw') is not None:
            self.raw = m.get('Raw')

        if m.get('Urlencoded') is not None:
            temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded()
            self.urlencoded = temp_model.from_map(m.get('Urlencoded'))

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyUrlencoded(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetSyntheticTaskDetailResponseBodyTaskDetailProtocolRequestContentBodyFormdata(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the **form-data**.
        self.key = key
        # The value of the form-data.
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

class GetSyntheticTaskDetailResponseBodyTaskDetailNet(DaraModel):
    def __init__(
        self,
        net_dig_switch: int = None,
        net_dns_ns: str = None,
        net_dns_query_method: str = None,
        net_dns_server: int = None,
        net_dns_switch: int = None,
        net_dns_timeout: str = None,
        net_icmp_active: int = None,
        net_icmp_data_cut: int = None,
        net_icmp_interval: int = None,
        net_icmp_num: int = None,
        net_icmp_size: int = None,
        net_icmp_switch: int = None,
        net_icmp_timeout: int = None,
        net_trace_route_num: int = None,
        net_trace_route_switch: int = None,
        net_trace_route_timeout: int = None,
        white_list: str = None,
    ):
        # Indicates whether the data is displayed in the DIG format. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.net_dig_switch = net_dig_switch
        # The NS server.
        self.net_dns_ns = net_dns_ns
        # The DNS query method. Valid values:
        # 
        # *   1: recursive
        # *   2: iterative
        self.net_dns_query_method = net_dns_query_method
        # The type of the DNS server. Valid values:
        # 
        # *   0: ipv4
        # *   1: ipv6
        # *   2: A version is automatically selected.
        self.net_dns_server = net_dns_server
        # Indicates whether DNS test is enabled. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.net_dns_switch = net_dns_switch
        # The timeout period of DNS requests.
        self.net_dns_timeout = net_dns_timeout
        # The protocol type. Valid values:
        # 
        # *   0 : ICMP
        # *   1 : TCP
        self.net_icmp_active = net_icmp_active
        # Indicates whether packets are split. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.net_icmp_data_cut = net_icmp_data_cut
        # The interval at which the synthetic monitoring task is executed.
        self.net_icmp_interval = net_icmp_interval
        # The number of packets.
        self.net_icmp_num = net_icmp_num
        # The packet size.
        self.net_icmp_size = net_icmp_size
        # Indicates whether ICMP test is enabled. Valid values:
        # 
        # *   0: no.
        # *   1: yes. If you set this parameter to 1, you must also set the Icmp parameter.
        self.net_icmp_switch = net_icmp_switch
        # The monitoring timeout period.
        self.net_icmp_timeout = net_icmp_timeout
        # The maximum number of active detection points.
        self.net_trace_route_num = net_trace_route_num
        # Indicates whether Tracert test is enabled. Valid values:
        # 
        # *   0: no
        # *   1: yes. If you set this parameter to 1, you must also set the Tracert parameter.
        self.net_trace_route_switch = net_trace_route_switch
        # The monitoring timeout period. Valid values: 0 to 300. Unit: seconds.
        self.net_trace_route_timeout = net_trace_route_timeout
        # The whitelisted objects that are used to avoid DNS hijacking. Format: `<domain name>:<objects>`.
        # 
        # >  WAP networks do not support hijacking.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net_dig_switch is not None:
            result['NetDigSwitch'] = self.net_dig_switch

        if self.net_dns_ns is not None:
            result['NetDnsNs'] = self.net_dns_ns

        if self.net_dns_query_method is not None:
            result['NetDnsQueryMethod'] = self.net_dns_query_method

        if self.net_dns_server is not None:
            result['NetDnsServer'] = self.net_dns_server

        if self.net_dns_switch is not None:
            result['NetDnsSwitch'] = self.net_dns_switch

        if self.net_dns_timeout is not None:
            result['NetDnsTimeout'] = self.net_dns_timeout

        if self.net_icmp_active is not None:
            result['NetIcmpActive'] = self.net_icmp_active

        if self.net_icmp_data_cut is not None:
            result['NetIcmpDataCut'] = self.net_icmp_data_cut

        if self.net_icmp_interval is not None:
            result['NetIcmpInterval'] = self.net_icmp_interval

        if self.net_icmp_num is not None:
            result['NetIcmpNum'] = self.net_icmp_num

        if self.net_icmp_size is not None:
            result['NetIcmpSize'] = self.net_icmp_size

        if self.net_icmp_switch is not None:
            result['NetIcmpSwitch'] = self.net_icmp_switch

        if self.net_icmp_timeout is not None:
            result['NetIcmpTimeout'] = self.net_icmp_timeout

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
        if m.get('NetDigSwitch') is not None:
            self.net_dig_switch = m.get('NetDigSwitch')

        if m.get('NetDnsNs') is not None:
            self.net_dns_ns = m.get('NetDnsNs')

        if m.get('NetDnsQueryMethod') is not None:
            self.net_dns_query_method = m.get('NetDnsQueryMethod')

        if m.get('NetDnsServer') is not None:
            self.net_dns_server = m.get('NetDnsServer')

        if m.get('NetDnsSwitch') is not None:
            self.net_dns_switch = m.get('NetDnsSwitch')

        if m.get('NetDnsTimeout') is not None:
            self.net_dns_timeout = m.get('NetDnsTimeout')

        if m.get('NetIcmpActive') is not None:
            self.net_icmp_active = m.get('NetIcmpActive')

        if m.get('NetIcmpDataCut') is not None:
            self.net_icmp_data_cut = m.get('NetIcmpDataCut')

        if m.get('NetIcmpInterval') is not None:
            self.net_icmp_interval = m.get('NetIcmpInterval')

        if m.get('NetIcmpNum') is not None:
            self.net_icmp_num = m.get('NetIcmpNum')

        if m.get('NetIcmpSize') is not None:
            self.net_icmp_size = m.get('NetIcmpSize')

        if m.get('NetIcmpSwitch') is not None:
            self.net_icmp_switch = m.get('NetIcmpSwitch')

        if m.get('NetIcmpTimeout') is not None:
            self.net_icmp_timeout = m.get('NetIcmpTimeout')

        if m.get('NetTraceRouteNum') is not None:
            self.net_trace_route_num = m.get('NetTraceRouteNum')

        if m.get('NetTraceRouteSwitch') is not None:
            self.net_trace_route_switch = m.get('NetTraceRouteSwitch')

        if m.get('NetTraceRouteTimeout') is not None:
            self.net_trace_route_timeout = m.get('NetTraceRouteTimeout')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailNav(DaraModel):
    def __init__(
        self,
        dns_hijack_whitelist: str = None,
        element_blacklist: str = None,
        execute_active_x: int = None,
        execute_applet: int = None,
        execute_script: int = None,
        filter_invalid_ip: int = None,
        flow_hijack_jump_times: int = None,
        flow_hijack_logo: str = None,
        monitor_timeout: int = None,
        nav_automatic_scrolling: int = None,
        nav_custom_header: str = None,
        nav_custom_header_content: str = None,
        nav_custom_host: int = None,
        nav_custom_host_ip: str = None,
        nav_disable_cache: int = None,
        nav_disable_compression: int = None,
        nav_ignore_certificate_error: int = None,
        nav_redirect: int = None,
        nav_return_element: int = None,
        page_tampering: str = None,
        process_name: str = None,
        quic_domain: str = None,
        quic_version: int = None,
        request_header: int = None,
        slow_element_threshold: int = None,
        verify_string_blacklist: str = None,
        verify_string_whitelist: str = None,
        wait_completion_time: int = None,
    ):
        # The DNS whitelist.
        self.dns_hijack_whitelist = dns_hijack_whitelist
        # The element blacklist.
        self.element_blacklist = element_blacklist
        # Indicates whether ActiveX is executed. Valid values:
        # 
        # *   3: yes
        # *   0: no
        # 
        # >  Only IE elements support this parameter.
        self.execute_active_x = execute_active_x
        # Indicates whether the applet is executed. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.execute_applet = execute_applet
        # Indicates whether scripts are executed. Valid values:
        # 
        # *   1: yes
        # *   0: no
        # 
        # >  Only IE elements support this parameter.
        self.execute_script = execute_script
        # Indicates whether invalid IP addresses are excluded. Valid values:
        # 
        # *   1: no
        # *   0: yes
        self.filter_invalid_ip = filter_invalid_ip
        # The element that is used in DNS hijacking.
        self.flow_hijack_jump_times = flow_hijack_jump_times
        # The tag that is used in DNS hijacking.
        self.flow_hijack_logo = flow_hijack_logo
        # The monitoring timeout period.
        self.monitor_timeout = monitor_timeout
        # Indicates whether the screen is automatically scrolled up and down to load a page. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.nav_automatic_scrolling = nav_automatic_scrolling
        # Indicates whether a custom header is created. Valid values:
        # 
        # *   0: no
        # *   1: A custom header is created for the first packet.
        # *   2: A custom header is created for all packets.
        self.nav_custom_header = nav_custom_header
        # The format of the custom header. Multiple fields are separated with vertical bars (|).
        self.nav_custom_header_content = nav_custom_header_content
        # The custom host mode. Valid values:
        # 
        # *   1: round robin
        # *   0: random
        self.nav_custom_host = nav_custom_host
        # The custom IP address of the host. Multiple IP addresses are separated with commas (,).
        self.nav_custom_host_ip = nav_custom_host_ip
        # Indicates whether caching is disabled. Valid values:
        # 
        # *   1: Caching is disabled.
        # *   0: Caching is enabled.
        self.nav_disable_cache = nav_disable_cache
        # Indicates whether compression is disabled. Valid values:
        # 
        # *   0: Compression is enabled.
        # *   1: Compression is disabled.
        self.nav_disable_compression = nav_disable_compression
        # Indicates whether certificate errors are ignored during certificate verification in the SSL handshake. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.nav_ignore_certificate_error = nav_ignore_certificate_error
        # Indicates whether redirection is enabled. Valid values:
        # 
        # *   0: no
        # *   1: yes
        self.nav_redirect = nav_redirect
        # Indicates whether the elements on the page are returned.
        # 
        # *   1: no. The basic document data is returned.
        # *   2: yes. All document data is returned.
        self.nav_return_element = nav_return_element
        # The page tampering.
        self.page_tampering = page_tampering
        # The process ID.
        self.process_name = process_name
        # The domain name of the QUIC request element.
        self.quic_domain = quic_domain
        # The QUIC version. Default value: 0. Valid values:
        # 
        # *   35
        # *   39
        # *   43
        # *   44
        # 
        # >  Only Chrome elements support this parameter.
        self.quic_version = quic_version
        # Indicates whether request headers are returned. Valid values:
        # 
        # *   0: no
        # *   1: The headers of base documents are returned.
        # *   2: All headers are returned.
        self.request_header = request_header
        # The time threshold that is used to define a slow element. Unit: seconds.
        self.slow_element_threshold = slow_element_threshold
        # The blacklist for string verification.
        self.verify_string_blacklist = verify_string_blacklist
        # The whitelist for string verification.
        self.verify_string_whitelist = verify_string_whitelist
        # The timeout period of waiting for the monitoring to complete.
        self.wait_completion_time = wait_completion_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_hijack_whitelist is not None:
            result['DnsHijackWhitelist'] = self.dns_hijack_whitelist

        if self.element_blacklist is not None:
            result['ElementBlacklist'] = self.element_blacklist

        if self.execute_active_x is not None:
            result['ExecuteActiveX'] = self.execute_active_x

        if self.execute_applet is not None:
            result['ExecuteApplet'] = self.execute_applet

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

        if self.nav_redirect is not None:
            result['NavRedirect'] = self.nav_redirect

        if self.nav_return_element is not None:
            result['NavReturnElement'] = self.nav_return_element

        if self.page_tampering is not None:
            result['PageTampering'] = self.page_tampering

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.quic_domain is not None:
            result['QuicDomain'] = self.quic_domain

        if self.quic_version is not None:
            result['QuicVersion'] = self.quic_version

        if self.request_header is not None:
            result['RequestHeader'] = self.request_header

        if self.slow_element_threshold is not None:
            result['SlowElementThreshold'] = self.slow_element_threshold

        if self.verify_string_blacklist is not None:
            result['VerifyStringBlacklist'] = self.verify_string_blacklist

        if self.verify_string_whitelist is not None:
            result['VerifyStringWhitelist'] = self.verify_string_whitelist

        if self.wait_completion_time is not None:
            result['WaitCompletionTime'] = self.wait_completion_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsHijackWhitelist') is not None:
            self.dns_hijack_whitelist = m.get('DnsHijackWhitelist')

        if m.get('ElementBlacklist') is not None:
            self.element_blacklist = m.get('ElementBlacklist')

        if m.get('ExecuteActiveX') is not None:
            self.execute_active_x = m.get('ExecuteActiveX')

        if m.get('ExecuteApplet') is not None:
            self.execute_applet = m.get('ExecuteApplet')

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

        if m.get('NavRedirect') is not None:
            self.nav_redirect = m.get('NavRedirect')

        if m.get('NavReturnElement') is not None:
            self.nav_return_element = m.get('NavReturnElement')

        if m.get('PageTampering') is not None:
            self.page_tampering = m.get('PageTampering')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('QuicDomain') is not None:
            self.quic_domain = m.get('QuicDomain')

        if m.get('QuicVersion') is not None:
            self.quic_version = m.get('QuicVersion')

        if m.get('RequestHeader') is not None:
            self.request_header = m.get('RequestHeader')

        if m.get('SlowElementThreshold') is not None:
            self.slow_element_threshold = m.get('SlowElementThreshold')

        if m.get('VerifyStringBlacklist') is not None:
            self.verify_string_blacklist = m.get('VerifyStringBlacklist')

        if m.get('VerifyStringWhitelist') is not None:
            self.verify_string_whitelist = m.get('VerifyStringWhitelist')

        if m.get('WaitCompletionTime') is not None:
            self.wait_completion_time = m.get('WaitCompletionTime')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailMonitorList(DaraModel):
    def __init__(
        self,
        city_code: int = None,
        monitor_type: int = None,
        net_service_id: int = None,
        send_count: int = None,
    ):
        # The city code.
        self.city_code = city_code
        # The type of the detection point.
        self.monitor_type = monitor_type
        # The ID of the network service.
        self.net_service_id = net_service_id
        # The number of times that the system sends detection requests.
        self.send_count = send_count

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

        if self.send_count is not None:
            result['SendCount'] = self.send_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('MonitorType') is not None:
            self.monitor_type = m.get('MonitorType')

        if m.get('NetServiceId') is not None:
            self.net_service_id = m.get('NetServiceId')

        if m.get('SendCount') is not None:
            self.send_count = m.get('SendCount')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailExtendInterval(DaraModel):
    def __init__(
        self,
        days: List[int] = None,
        end_minute: int = None,
        end_time: str = None,
        endhour: int = None,
        start_hour: int = None,
        start_minute: int = None,
        start_time: str = None,
    ):
        # The day on which synthetic monitoring is performed. Valid values:
        # 
        # *   \\-1: every day
        # *   0: Sunday
        # *   1: Monday
        # *   2: Tuesday
        # *   3: Wednesday
        # *   4: Thursday
        # *   5: Friday
        # *   6: Saturday
        self.days = days
        # The minute at which synthetic monitoring ends.
        self.end_minute = end_minute
        # The time when synthetic monitoring ends. Format: `yyyy-MM-dd HH`.
        self.end_time = end_time
        # The hour at which synthetic monitoring ends.
        self.endhour = endhour
        # The hour at which synthetic monitoring starts.
        self.start_hour = start_hour
        # The minute at which synthetic monitoring starts.
        self.start_minute = start_minute
        # The time when synthetic monitoring starts. Format: yyyy-MM-dd HH.
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

        if self.end_minute is not None:
            result['EndMinute'] = self.end_minute

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.endhour is not None:
            result['Endhour'] = self.endhour

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

        if m.get('EndMinute') is not None:
            self.end_minute = m.get('EndMinute')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Endhour') is not None:
            self.endhour = m.get('Endhour')

        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')

        if m.get('StartMinute') is not None:
            self.start_minute = m.get('StartMinute')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetSyntheticTaskDetailResponseBodyTaskDetailDownload(DaraModel):
    def __init__(
        self,
        connection_timeout: int = None,
        download_custom_header_content: str = None,
        download_custom_host: int = None,
        download_custom_host_ip: str = None,
        download_kernel: int = None,
        download_redirect: int = None,
        download_transmission_size: int = None,
        monitor_timeout: int = None,
        quick_protocol: str = None,
        validate_keywords: str = None,
        verify_way: int = None,
        white_list: str = None,
    ):
        # The timeout period of the file download task.
        self.connection_timeout = connection_timeout
        # The items to be ignored in a certificate error. Multiple values are concatenated with vertical bars (|).
        self.download_custom_header_content = download_custom_header_content
        # The custom host. Valid values:
        # 
        # *   1: round robin
        # *   0: random
        self.download_custom_host = download_custom_host
        # The custom IP address of the host. Multiple IP addresses are separated with commas (,).
        self.download_custom_host_ip = download_custom_host_ip
        # The kernel type. Valid values:
        # 
        # *   1: curl
        # *   0: WinInet
        self.download_kernel = download_kernel
        # Indicates whether redirection is supported.
        self.download_redirect = download_redirect
        # The file size. Unit: KB.
        self.download_transmission_size = download_transmission_size
        # The monitoring duration.
        self.monitor_timeout = monitor_timeout
        # The QUIC protocol type. Valid values:
        # 
        # *   1: HTTP/1
        # *   2: HTTP/2
        # *   3: http3
        self.quick_protocol = quick_protocol
        # The keyword that is used in verification.
        self.validate_keywords = validate_keywords
        # The method that is used to verify the response content. Valid values:
        # 
        # *   0: no verification.
        # *   1: exact match with the verification string.
        # *   2: partial match with the verification string.
        # *   3: MD5 verification.
        self.verify_way = verify_way
        # The whitelisted objects that are used to avoid DNS hijacking. Format: `<domain name>:<objects>`.
        # 
        # >  WAP networks do not support hijacking.
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

        if self.download_kernel is not None:
            result['DownloadKernel'] = self.download_kernel

        if self.download_redirect is not None:
            result['DownloadRedirect'] = self.download_redirect

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

        if m.get('DownloadKernel') is not None:
            self.download_kernel = m.get('DownloadKernel')

        if m.get('DownloadRedirect') is not None:
            self.download_redirect = m.get('DownloadRedirect')

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

class GetSyntheticTaskDetailResponseBodyTaskDetailCommonParam(DaraModel):
    def __init__(
        self,
        alarm_flag: int = None,
        alert_list: List[main_models.GetSyntheticTaskDetailResponseBodyTaskDetailCommonParamAlertList] = None,
        alert_notifier_id: str = None,
        alert_policy_id: str = None,
        monitor_samples: str = None,
        start_execution_time: str = None,
    ):
        # The identifier of the alert.
        self.alarm_flag = alarm_flag
        # The list of alerts.
        self.alert_list = alert_list
        # The ID of the alert identifier.
        self.alert_notifier_id = alert_notifier_id
        # The ID of the alert policy.
        self.alert_policy_id = alert_policy_id
        # The monitoring samples.
        self.monitor_samples = monitor_samples
        # The start time of the execution.
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
                temp_model = main_models.GetSyntheticTaskDetailResponseBodyTaskDetailCommonParamAlertList()
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

class GetSyntheticTaskDetailResponseBodyTaskDetailCommonParamAlertList(DaraModel):
    def __init__(
        self,
        general_alert: str = None,
        is_critical: str = None,
        name: str = None,
        serious_alert: str = None,
        symbols: str = None,
    ):
        # The low-risk alert.
        self.general_alert = general_alert
        # Indicates whether the condition is essential.
        self.is_critical = is_critical
        # The alert name.
        self.name = name
        # The Critical-level alert.
        self.serious_alert = serious_alert
        # Greater than or less than.
        self.symbols = symbols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.general_alert is not None:
            result['GeneralAlert'] = self.general_alert

        if self.is_critical is not None:
            result['IsCritical'] = self.is_critical

        if self.name is not None:
            result['Name'] = self.name

        if self.serious_alert is not None:
            result['SeriousAlert'] = self.serious_alert

        if self.symbols is not None:
            result['Symbols'] = self.symbols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeneralAlert') is not None:
            self.general_alert = m.get('GeneralAlert')

        if m.get('IsCritical') is not None:
            self.is_critical = m.get('IsCritical')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SeriousAlert') is not None:
            self.serious_alert = m.get('SeriousAlert')

        if m.get('Symbols') is not None:
            self.symbols = m.get('Symbols')

        return self

