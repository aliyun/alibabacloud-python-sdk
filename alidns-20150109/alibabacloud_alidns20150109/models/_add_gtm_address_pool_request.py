# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddGtmAddressPoolRequest(DaraModel):
    def __init__(
        self,
        addr: List[main_models.AddGtmAddressPoolRequestAddr] = None,
        evaluation_count: int = None,
        instance_id: str = None,
        interval: int = None,
        isp_city_node: List[main_models.AddGtmAddressPoolRequestIspCityNode] = None,
        lang: str = None,
        min_available_addr_num: int = None,
        monitor_extend_info: str = None,
        monitor_status: str = None,
        name: str = None,
        protocol_type: str = None,
        timeout: int = None,
        type: str = None,
    ):
        # The address pools.
        # 
        # This parameter is required.
        self.addr = addr
        # The number of consecutive failures.
        self.evaluation_count = evaluation_count
        # The ID of the GTM instance for which you want to create an address pool.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The health check interval. Unit: seconds. Set the value to 60.
        self.interval = interval
        # The monitored nodes.
        self.isp_city_node = isp_city_node
        # The language of the values of specific response parameters.
        self.lang = lang
        # The minimum number of available addresses in the address pool.
        # 
        # This parameter is required.
        self.min_available_addr_num = min_available_addr_num
        # The extended information. The required parameters vary based on the value of ProtocolType.
        # 
        # When ProtocolType is set to HTTP or HTTPS:
        # 
        # *   port: the port that you want to check
        # *   failureRate: the failure rate
        # *   code: the return code. The health check result is deemed abnormal if the returned value is greater than the specified value. Valid values: 400 and 500.
        # *   host: the host settings
        # *   path: the URL path
        # 
        # When ProtocolType is set to PING:
        # 
        # *   packetNum: the number of ping packets
        # *   packetLossRate: the packet loss rate
        # *   failureRate: the failure rate
        # 
        # When ProtocolType is set to TCP:
        # 
        # *   port: the port that you want to check
        # *   failureRate: the failure rate
        self.monitor_extend_info = monitor_extend_info
        # Specifies whether to enable the health check. Valid values:
        # 
        # *   **OPEN**: enables the health check.
        # *   **CLOSE**: disables the health check. This is the default value.
        self.monitor_status = monitor_status
        # The name of the address pool.
        # 
        # This parameter is required.
        self.name = name
        # The health check protocol. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   Ping
        # *   TCP
        self.protocol_type = protocol_type
        # The timeout period. Unit: milliseconds. Valid values: 2000, 3000, 5000, and 10000.
        self.timeout = timeout
        # The type of the address pool. Valid values:
        # 
        # *   **IP**: IPv4 address
        # *   **DOMAIN**: domain name
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

        if self.min_available_addr_num is not None:
            result['MinAvailableAddrNum'] = self.min_available_addr_num

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
                temp_model = main_models.AddGtmAddressPoolRequestAddr()
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
                temp_model = main_models.AddGtmAddressPoolRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MinAvailableAddrNum') is not None:
            self.min_available_addr_num = m.get('MinAvailableAddrNum')

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

class AddGtmAddressPoolRequestIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        # The code of the city where the monitored node is deployed. For more information about specific values, see the response parameters of DescribeGtmMonitorAvailableConfig.
        self.city_code = city_code
        # *   The code of the Internet service provider (ISP) to which the monitored node belongs. For more information about specific values, see the response parameters of DescribeGtmMonitorAvailableConfig.
        # *   If the value of the GroupType parameter is BGP or OVERSEAS, IspCode is optional. The default value is 465.
        # *   If the value of the GroupType parameter is not BGP or OVERSEAS, IspCode is required and is used together with CityCode.
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

class AddGtmAddressPoolRequestAddr(DaraModel):
    def __init__(
        self,
        lba_weight: int = None,
        mode: str = None,
        value: str = None,
    ):
        # The weight of the address pool.
        self.lba_weight = lba_weight
        # The mode of the address pool. Valid values:
        # 
        # *   **SMART**: smart return
        # *   **ONLINE**: always online
        # *   **OFFLINE**: always offline
        self.mode = mode
        # The address in the address pool.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lba_weight is not None:
            result['LbaWeight'] = self.lba_weight

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LbaWeight') is not None:
            self.lba_weight = m.get('LbaWeight')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

