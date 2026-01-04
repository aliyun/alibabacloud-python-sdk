# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNetworkZoneRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        ipv_4cidrs: List[str] = None,
        ipv_6cidrs: List[str] = None,
        network_zone_name: str = None,
        network_zone_type: str = None,
        vpc_id: str = None,
    ):
        # 保证请求幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符，且不能超过64个字符。
        self.client_token = client_token
        # 网络区域描述
        self.description = description
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 网络区域ipv4Cidr
        self.ipv_4cidrs = ipv_4cidrs
        # 网络区域ipv6Cidr
        self.ipv_6cidrs = ipv_6cidrs
        # 网络区域名称
        # 
        # This parameter is required.
        self.network_zone_name = network_zone_name
        # 网络区域类型
        # 
        # This parameter is required.
        self.network_zone_type = network_zone_type
        # 专有网络VpcId
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs

        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs

        if self.network_zone_name is not None:
            result['NetworkZoneName'] = self.network_zone_name

        if self.network_zone_type is not None:
            result['NetworkZoneType'] = self.network_zone_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')

        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')

        if m.get('NetworkZoneName') is not None:
            self.network_zone_name = m.get('NetworkZoneName')

        if m.get('NetworkZoneType') is not None:
            self.network_zone_type = m.get('NetworkZoneType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

