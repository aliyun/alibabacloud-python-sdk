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
        # The number of consecutive failures.
        # 
        # This parameter is required.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds. Set the value to 60.
        # 
        # This parameter is required.
        self.interval = interval
        # The nodes for monitoring.
        # 
        # This parameter is required.
        self.isp_city_node = isp_city_node
        # The language.
        self.lang = lang
        # The extended information. The required parameters vary based on the health check protocol.
        # 
        # HTTP or HTTPS
        # 
        # *   port: the port that you want to check
        # *   failureRate: the failure rate
        # *   code: the return code. The health check result is deemed abnormal if the returned value is greater than the specified value. Valid values: 400 and 500.
        # *   host: the host settings
        # *   path: the URL path
        # 
        # PING
        # 
        # *   packetNum: the number of ping packets
        # *   packetLossRate: the packet loss rate
        # *   failureRate: the failure rate
        # 
        # TCP
        # 
        # *   port: the port that you want to check
        # *   failureRate: the failure rate
        # 
        # This parameter is required.
        self.monitor_extend_info = monitor_extend_info
        # The protocol used for the health check. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # *   PING
        # *   TCP
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The health check timeout period. Unit: milliseconds. Valid values: 2000, 3000, 5000, and 10000.
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
        # Specify the parameter according to the value of CityCode returned by the DescribeGtmMonitorAvailableConfig operation.
        self.city_code = city_code
        # The Internet service provider (ISP) node. Specify the parameter according to the value of IspCode returned by the DescribeGtmMonitorAvailableConfig operation.
        # 
        # *   If the return value of GroupType for the DescribeGtmMonitorAvailableConfig operation is BGP or Overseas, IspCode is not required and is set to 465 by default.
        # *   If the return value of GroupType for the DescribeGtmMonitorAvailableConfig operation is not BGP or Overseas, IspCode is required. When IspCode is specified, CityCode is required.
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

