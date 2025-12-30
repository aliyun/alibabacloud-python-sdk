# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmMonitorConfigResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        evaluation_count: int = None,
        interval: int = None,
        isp_city_nodes: main_models.DescribeGtmMonitorConfigResponseBodyIspCityNodes = None,
        monitor_config_id: str = None,
        monitor_extend_info: str = None,
        protocol_type: str = None,
        request_id: str = None,
        timeout: int = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the health check configuration was created.
        self.create_time = create_time
        # The timestamp that indicates the time when the health check configuration was created.
        self.create_timestamp = create_timestamp
        # The maximum number of consecutive exceptions detected. If the number of consecutive exceptions detected reaches the maximum number, the application service is deemed abnormal.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds. The value is 60.
        self.interval = interval
        # The monitored nodes.
        self.isp_city_nodes = isp_city_nodes
        # The ID of the health check configuration.
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
        self.monitor_extend_info = monitor_extend_info
        # The protocol used for the health check.
        self.protocol_type = protocol_type
        # The ID of the request.
        self.request_id = request_id
        # The health check timeout period. Unit: milliseconds. Valid values: 2000, 3000, 5000, and 10000.
        self.timeout = timeout
        # The time when the health check configuration was last updated.
        self.update_time = update_time
        # The timestamp that indicates the time when the health check configuration was last updated.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.isp_city_nodes:
            self.isp_city_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.evaluation_count is not None:
            result['EvaluationCount'] = self.evaluation_count

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.isp_city_nodes is not None:
            result['IspCityNodes'] = self.isp_city_nodes.to_map()

        if self.monitor_config_id is not None:
            result['MonitorConfigId'] = self.monitor_config_id

        if self.monitor_extend_info is not None:
            result['MonitorExtendInfo'] = self.monitor_extend_info

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('EvaluationCount') is not None:
            self.evaluation_count = m.get('EvaluationCount')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IspCityNodes') is not None:
            temp_model = main_models.DescribeGtmMonitorConfigResponseBodyIspCityNodes()
            self.isp_city_nodes = temp_model.from_map(m.get('IspCityNodes'))

        if m.get('MonitorConfigId') is not None:
            self.monitor_config_id = m.get('MonitorConfigId')

        if m.get('MonitorExtendInfo') is not None:
            self.monitor_extend_info = m.get('MonitorExtendInfo')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeGtmMonitorConfigResponseBodyIspCityNodes(DaraModel):
    def __init__(
        self,
        isp_city_node: List[main_models.DescribeGtmMonitorConfigResponseBodyIspCityNodesIspCityNode] = None,
    ):
        self.isp_city_node = isp_city_node

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
        result['IspCityNode'] = []
        if self.isp_city_node is not None:
            for k1 in self.isp_city_node:
                result['IspCityNode'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city_node = []
        if m.get('IspCityNode') is not None:
            for k1 in m.get('IspCityNode'):
                temp_model = main_models.DescribeGtmMonitorConfigResponseBodyIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeGtmMonitorConfigResponseBodyIspCityNodesIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        # The code of the city where the monitored node is deployed.
        self.city_code = city_code
        # The display name of the city where the monitored node is deployed.
        self.city_name = city_name
        # The code of the country where the monitored node is deployed.
        self.country_code = country_code
        # The display name of the country where the monitored node is deployed.
        self.country_name = country_name
        # The code of the Internet service provider (ISP) to which the monitored node belongs.
        self.isp_code = isp_code
        # The display name of the ISP to which the monitored node belongs.
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['CityCode'] = self.city_code

        if self.city_name is not None:
            result['CityName'] = self.city_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.isp_code is not None:
            result['IspCode'] = self.isp_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')

        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('IspCode') is not None:
            self.isp_code = m.get('IspCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

