# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetNetworkZoneResponseBody(DaraModel):
    def __init__(
        self,
        network_zone: main_models.GetNetworkZoneResponseBodyNetworkZone = None,
        request_id: str = None,
    ):
        self.network_zone = network_zone
        self.request_id = request_id

    def validate(self):
        if self.network_zone:
            self.network_zone.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_zone is not None:
            result['NetworkZone'] = self.network_zone.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkZone') is not None:
            temp_model = main_models.GetNetworkZoneResponseBodyNetworkZone()
            self.network_zone = temp_model.from_map(m.get('NetworkZone'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNetworkZoneResponseBodyNetworkZone(DaraModel):
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

