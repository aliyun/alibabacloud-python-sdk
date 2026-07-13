# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddDnsGtmAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr: List[main_models.AddDnsGtmAddressPoolRequestAddr] = None,
        evaluation_count: int = None,
        instance_id: str = None,
        interval: int = None,
        isp_city_node: List[main_models.AddDnsGtmAddressPoolRequestIspCityNode] = None,
        lang: str = None,
        lba_strategy: str = None,
        monitor_extend_info: str = None,
        monitor_status: str = None,
        name: str = None,
        protocol_type: str = None,
        timeout: int = None,
        type: str = None,
    ):
        # The list of addresses in the address pool.
        # 
        # This parameter is required.
        self.addr = addr
        # The number of consecutive failed health checks.
        self.evaluation_count = evaluation_count
        # The instance ID.
        # <props="intl">Call [DescribeDnsGtmInstances](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describednsgtminstances) to obtain the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The health check interval. Unit: seconds.
        self.interval = interval
        # The list of health check nodes. If MonitorStatus is set to OPEN, you must specify at least one valid health check node.
        self.isp_city_node = isp_city_node
        # The language of some returned parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The load balancing policy. Valid values:
        # 
        # - ALL_RR: returns all addresses.
        # 
        # - RATIO: returns addresses by weight.
        # 
        # This parameter is required.
        self.lba_strategy = lba_strategy
        # The extended information. This parameter is a JSON string. The required parameters vary based on the health check protocol:
        # 
        # - HTTP and HTTPS:
        # 
        #   - port: The health check port.
        # 
        #   - host: The host settings.
        # 
        #   - path: The URL path.
        # 
        #   - code: The return code. A response with a status code greater than this value is considered abnormal. Valid values: 400 and 500.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - sni: Specifies whether to enable Server Name Indication (SNI). This parameter is available only for the HTTPS protocol.
        # 
        #     - true: Enable SNI.
        # 
        #     - Other values: Disable SNI.
        # 
        #   - nodeType: The type of the health check node when the address pool type is DOMAIN. Valid values:
        # 
        #     - IPV4
        # 
        #     - IPV6
        # 
        # - PING:
        # 
        #   - failureRate: The failure rate.
        # 
        #   - packetNum: The number of ping packets.
        # 
        #   - packetLossRate: The packet loss rate.
        # 
        #   - nodeType: The type of the health check node when the address pool type is DOMAIN. Valid values:
        # 
        #     - IPV4
        # 
        #     - IPV6
        # 
        # - TCP:
        # 
        #   - port: The health check port.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - nodeType: The type of the health check node when the address pool type is DOMAIN. Valid values:
        # 
        #     - IPV4
        # 
        #     - IPV6
        self.monitor_extend_info = monitor_extend_info
        # The status of the health check feature. Default value: CLOSE. If you set this parameter to OPEN, the health check configuration is verified. Otherwise, the configuration is ignored.
        # 
        # - OPEN: enabled
        # 
        # - CLOSE: disabled
        self.monitor_status = monitor_status
        # The name of the address pool.
        # 
        # This parameter is required.
        self.name = name
        # The health check protocol. Valid values:
        # 
        # - HTTP
        # 
        # - HTTPS
        # 
        # - PING
        # 
        # - TCP
        self.protocol_type = protocol_type
        # The timeout period. Unit: milliseconds.
        self.timeout = timeout
        # The type of the address pool. Valid values:
        # 
        # - IPV4: IPv4 address
        # 
        # - IPV6: IPv6 address
        # 
        # - DOMAIN: domain name
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.addr:
            for v1 in self.addr:
                 if v1:
                    v1.validate()
        if self.isp_city_node:
            for v1 in self.isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addr'] = []
        if self.addr is not None:
            for k1 in self.addr:
                result['Addr'].append(k1.to_map() if k1 else None)

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k1 in self.isp_city_node:
                result['IspCityNode'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.lba_strategy is not None:
            result['LbaStrategy'] = self.lba_strategy

        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info

        if self.monitor_status is not None:
            result['MonitorStatus'] = self.monitor_status

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr = []
        if m.get('Addr') is not None:
            for k1 in m.get('Addr'):
                temp_model = main_models.AddDnsGtmAddressPoolRequestAddr()
                self.addr.append(temp_model.from_map(k1))

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.AddDnsGtmAddressPoolRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LbaStrategy') is not None:
            self.lba_strategy = m.get('LbaStrategy')

        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')

        if m.get('MonitorStatus') is not None:
            self.monitor_status = m.get('MonitorStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AddDnsGtmAddressPoolRequestIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        # The city code. If MonitorStatus is set to OPEN, CityCode is required.
        # 
        # For information about the valid values, see the response of the DescribeDnsGtmMonitorAvailableConfig operation.
        self.city_code = city_code
        # If MonitorStatus is set to OPEN, IspCode is required.
        # For information about the valid values, see the response of the DescribeDnsGtmMonitorAvailableConfig operation.
        self.isp_code = isp_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        return self

class AddDnsGtmAddressPoolRequestAddr(DaraModel):
    def __init__(
        self,
        addr: str = None,
        attribute_info: str = None,
        lba_weight: int = None,
        mode: str = None,
        remark: str = None,
    ):
        # The address.
        # 
        # This parameter is required.
        self.addr = addr
        # The source region of the address. This parameter is a JSON string.
        # 
        # - lineCode: The line code of the source region.
        # 
        # - lineCodeRectifyType: The rectification type for the line code. Default value: AUTO.
        # 
        #   - NO_NEED: No rectification is performed.
        # 
        #   - RECTIFIED: The line code is rectified.
        # 
        #   - AUTO: The line code is automatically rectified.
        # 
        # This parameter is required.
        self.attribute_info = attribute_info
        # The weight.
        self.lba_weight = lba_weight
        # The mode. Valid values:
        # 
        # - SMART: smart return
        # 
        # - ONLINE: always online
        # 
        # - OFFLINE: always offline
        # 
        # This parameter is required.
        self.mode = mode
        # The remarks.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr is not None:
            result['Addr'] = self.addr

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')

        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')

        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

