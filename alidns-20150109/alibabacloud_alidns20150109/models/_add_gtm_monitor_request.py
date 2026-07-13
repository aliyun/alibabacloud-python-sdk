# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class AddGtmMonitorRequest(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        evaluation_count: int = None,
        interval: int = None,
        isp_city_node: List[main_models.AddGtmMonitorRequestIspCityNode] = None,
        lang: str = None,
        monitor_extend_info: str = None,
        protocol_type: str = None,
        timeout: int = None,
    ):
        # The ID of the address pool.
        # 
        # This parameter is required.
        self.addr_pool_id = addr_pool_id
        # The number of consecutive failed health checks.
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds. The value must be 60.
        # 
        # This parameter is required.
        self.interval = interval
        # The list of monitoring nodes.
        # 
        # This parameter is required.
        self.isp_city_node = isp_city_node
        # The language.
        self.lang = lang
        # The extended information. You must pass parameters based on the value of ProtocolType:
        # 
        # For HTTP and HTTPS:
        # 
        # - port: The health check port.
        # 
        # - failureRate: The failure rate.
        # 
        # - code: The return code. A response with a status code greater than this value is considered abnormal. Valid values: 400 and 500.
        # 
        # - host: The host settings.
        # 
        # - path: The URL path.
        # 
        # For PING:
        # 
        # - packetNum: The number of ping packets.
        # 
        # - packetLossRate: The packet loss rate.
        # 
        # - failureRate: The failure rate.
        # 
        # For TCP:
        # 
        # - port: The health check port.
        # 
        # - failureRate: The failure rate.
        # 
        # This parameter is required.
        self.monitor_extend_info = monitor_extend_info
        # The health check protocol. Valid values:
        # 
        # - HTTP
        # 
        # - HTTPS
        # 
        # - PING
        # 
        # - TCP
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The timeout period. Unit: milliseconds. Valid values: 2000, 3000, 5000, and 10000.
        # 
        # This parameter is required.
        self.timeout = timeout

    def validate(self):
        if self.isp_city_node:
            for v1 in self.isp_city_node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.interval is not None:
            result['Interval'] = self.interval

        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k1 in self.isp_city_node:
                result['IspCityNode'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.AddGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class AddGtmMonitorRequestIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        # The city code.
        # 
        # For more information about the valid values, see the response of the DescribeGtmMonitorAvailableConfig operation.
        self.city_code = city_code
        # For more information about the valid values, see the response of the DescribeGtmMonitorAvailableConfig operation.
        # 
        # - If GroupType is set to Border Gateway Protocol (BGP) or Overseas, you do not need to specify IspCityNode.N.IspCode. The default value is 465.
        # 
        # - If GroupType is not set to BGP or Overseas, you must specify IspCityNode.N.IspCode. The value of IspCityNode.N.IspCode must be consistent with the value of IspCityNode.N.CityCode.
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

