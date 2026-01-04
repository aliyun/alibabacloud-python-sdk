# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListNetworkZonesResponseBody(DaraModel):
    def __init__(
        self,
        network_zones: List[main_models.ListNetworkZonesResponseBodyNetworkZones] = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.network_zones = network_zones
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.previous_token = previous_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_zones:
            for v1 in self.network_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkZones'] = []
        if self.network_zones is not None:
            for k1 in self.network_zones:
                result['NetworkZones'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_zones = []
        if m.get('NetworkZones') is not None:
            for k1 in m.get('NetworkZones'):
                temp_model = main_models.ListNetworkZonesResponseBodyNetworkZones()
                self.network_zones.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNetworkZonesResponseBodyNetworkZones(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        ipv_4cidrs: List[str] = None,
        ipv_6cidrs: List[str] = None,
        network_zone_id: str = None,
        network_zone_name: str = None,
        network_zone_type: str = None,
        vpc_id: str = None,
    ):
        # IDaaS EIAM 网络区域描述
        self.description = description
        # 实例ID。
        self.instance_id = instance_id
        self.ipv_4cidrs = ipv_4cidrs
        self.ipv_6cidrs = ipv_6cidrs
        # IDaaS EIAM 网络区域Id
        self.network_zone_id = network_zone_id
        # IDaaS EIAM 网络区域名称
        self.network_zone_name = network_zone_name
        # IDaaS EIAM 网络区域类型
        self.network_zone_type = network_zone_type
        # IDaaS EIAM 专有网络VpcId
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs

        if self.network_zone_id is not None:
            result['NetworkZoneId'] = self.network_zone_id

        if self.network_zone_name is not None:
            result['NetworkZoneName'] = self.network_zone_name

        if self.network_zone_type is not None:
            result['NetworkZoneType'] = self.network_zone_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')

        if m.get('NetworkZoneId') is not None:
            self.network_zone_id = m.get('NetworkZoneId')

        if m.get('NetworkZoneName') is not None:
            self.network_zone_name = m.get('NetworkZoneName')

        if m.get('NetworkZoneType') is not None:
            self.network_zone_type = m.get('NetworkZoneType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

