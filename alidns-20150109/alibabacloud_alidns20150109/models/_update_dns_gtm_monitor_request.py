# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateDnsGtmMonitorRequest(DaraModel):
    def __init__(
        self,
        evaluation_count: int = None,
        interval: int = None,
        isp_city_node: List[main_models.UpdateDnsGtmMonitorRequestIspCityNode] = None,
        lang: str = None,
        monitor_config_id: str = None,
        monitor_extend_info: str = None,
        protocol_type: str = None,
        timeout: int = None,
    ):
        # The number of consecutive health checks.
        self.evaluation_count = evaluation_count
        # The health check interval. Unit: seconds.
        self.interval = interval
        # The list of city nodes for health checks.
        # 
        # This parameter is required.
        self.isp_city_node = isp_city_node
        # The language of the response. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The ID of the health check configuration. You can call the [DescribeDnsGtmInstanceAddressPool](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describednsgtminstanceaddresspool) operation to obtain the ID.
        # 
        # This parameter is required.
        self.monitor_config_id = monitor_config_id
        # The extended information. The required parameters vary based on the health check protocol.
        # 
        # - HTTP(S):
        # 
        #   - port: The port for the health check.
        # 
        #   - host: The Host header.
        # 
        #   - path: The URL path.
        # 
        #   - code: The health check is considered abnormal if the returned status code is greater than the specified value. For example, if you set this parameter to 400, a returned status code of 404 is considered abnormal.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - sni: Specifies whether to enable Server Name Indication (SNI). This parameter is available only for the HTTPS protocol.
        # 
        #     - true: Enable SNI.
        # 
        #     - false: Disable SNI.
        # 
        #   - nodeType: The type of the node for health checks when the address pool type is DOMAIN.
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
        #   - nodeType: The type of the node for health checks when the address pool type is DOMAIN.
        # 
        #     - IPV4
        # 
        #     - IPV6
        # 
        # - TCP:
        # 
        #   - port: The port for the health check.
        # 
        #   - failureRate: The failure rate.
        # 
        #   - nodeType: The type of the node for health checks when the address pool type is DOMAIN.
        # 
        #     - IPV4
        # 
        #     - IPV6
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
        # The timeout period for a health check. Unit: milliseconds.
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
                temp_model = main_models.UpdateDnsGtmMonitorRequestIspCityNode()
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

class UpdateDnsGtmMonitorRequestIspCityNode(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        isp_code: str = None,
    ):
        # The city code of the health check node.
        self.city_code = city_code
        # The carrier code of the health check node.
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

