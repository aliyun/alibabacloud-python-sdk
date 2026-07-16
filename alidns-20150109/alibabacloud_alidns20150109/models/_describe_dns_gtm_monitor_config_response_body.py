# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmMonitorConfigResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        evaluation_count: int = None,
        interval: int = None,
        isp_city_nodes: main_models.DescribeDnsGtmMonitorConfigResponseBodyIspCityNodes = None,
        monitor_config_id: str = None,
        monitor_extend_info: str = None,
        protocol_type: str = None,
        request_id: str = None,
        timeout: int = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the configuration was created.
        self.create_time = create_time
        # The timestamp that indicates when the configuration was created.
        self.create_timestamp = create_timestamp
        # The number of consecutive failures.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds.
        self.interval = interval
        self.isp_city_nodes = isp_city_nodes
        # The ID of the health check configuration.
        self.monitor_config_id = monitor_config_id
        # The extended information. The parameters vary by protocol.
        # 
        # - For HTTP and HTTPS:
        # 
        #   - port: The health check port.
        # 
        #   - host: The Host header.
        # 
        #   - path: The URL path.
        # 
        #   - code: The expected HTTP status code.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - sni: Specifies whether to enable Server Name Indication (SNI). This parameter is valid only when the protocol is set to HTTPS.
        # 
        #     - true: enables SNI.
        # 
        #     - false: disables SNI.
        # 
        #   - nodeType: The type of the monitoring node for the health check when the address pool type is DOMAIN.
        # 
        #     - IPV4
        # 
        #     - IPV6
        # 
        # - For PING:
        # 
        #   - failureRate: The failure rate.
        # 
        #   - packetNum: The number of ping packets.
        # 
        #   - packetLossRate: The packet loss rate.
        # 
        #   - nodeType: The type of the monitoring node for the health check when the address pool type is DOMAIN.
        # 
        #     - IPV4
        # 
        #     - IPV6
        # 
        # - For TCP:
        # 
        #   - port: The health check port.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - nodeType: The type of the monitoring node for the health check when the address pool type is DOMAIN.
        # 
        #     - IPV4
        # 
        #     - IPV6
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
        self.protocol_type = protocol_type
        # The unique request ID.
        self.request_id = request_id
        # The timeout period. Unit: milliseconds.
        self.timeout = timeout
        # The time when the configuration was last updated.
        self.update_time = update_time
        # The timestamp that indicates when the configuration was last updated.
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
            temp_model = main_models.DescribeDnsGtmMonitorConfigResponseBodyIspCityNodes()
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

class DescribeDnsGtmMonitorConfigResponseBodyIspCityNodes(DaraModel):
    def __init__(
        self,
        isp_city_node: List[main_models.DescribeDnsGtmMonitorConfigResponseBodyIspCityNodesIspCityNode] = None,
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
                temp_model = main_models.DescribeDnsGtmMonitorConfigResponseBodyIspCityNodesIspCityNode()
                self.isp_city_node.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmMonitorConfigResponseBodyIspCityNodesIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        country_code: str = None,
        country_name: str = None,
        isp_code: str = None,
        isp_name: str = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.country_code = country_code
        self.country_name = country_name
        self.isp_code = isp_code
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

