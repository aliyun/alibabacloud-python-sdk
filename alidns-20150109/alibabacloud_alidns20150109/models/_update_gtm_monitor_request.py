# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateGtmMonitorRequest(DaraModel):
    def __init__(
        self,
        evaluation_count: int = None,
        interval: int = None,
        isp_city_node: List[main_models.UpdateGtmMonitorRequestIspCityNode] = None,
        lang: str = None,
        monitor_config_id: str = None,
        monitor_extend_info: str = None,
        protocol_type: str = None,
        timeout: int = None,
    ):
        # The maximum number of consecutive exceptions detected. If the number of consecutive exceptions detected reaches the maximum number, the application service is deemed abnormal.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds. Set the value to 60.
        self.interval = interval
        # The monitored nodes.
        # 
        # This parameter is required.
        self.isp_city_node = isp_city_node
        # The language of the values of specific response parameters.
        self.lang = lang
        # The ID of the health check configuration.
        # 
        # This parameter is required.
        self.monitor_config_id = monitor_config_id
        # The extended information, that is, the parameters required for the protocol. Different protocols require different parameters:
        # 
        # HTTP or HTTPS:
        # 
        # *   port: the port to check.
        # *   failureRate: the failure rate.
        # *   code: the status code threshold. If the returned status code is greater than the specified threshold, the application service is deemed abnormal. Valid values: 400 and 500.
        # *   host: the host configuration.
        # *   path: the health check URL.
        # 
        # PING:
        # 
        # *   packetNum: the number of ping packets.
        # *   packetLossRate: the loss rate of ping packets.
        # *   failureRate: the failure rate.
        # 
        # TCP:
        # 
        # *   port: the port to check.
        # *   failureRate: the failure rate.
        # 
        # This parameter is required.
        self.monitor_extend_info = monitor_extend_info
        # The protocol used for the health check.
        # 
        # This parameter is required.
        self.protocol_type = protocol_type
        # The health check timeout period. Unit: milliseconds. Valid values: 2000, 3000, 5000, and 10000.
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

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.UpdateGtmMonitorRequestIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class UpdateGtmMonitorRequestIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        # The code of the city where the monitored node is deployed.
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

