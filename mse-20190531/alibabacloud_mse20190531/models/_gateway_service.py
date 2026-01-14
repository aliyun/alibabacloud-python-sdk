# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GatewayService(DaraModel):
    def __init__(
        self,
        gateway_traffic_policy: main_models.TrafficPolicy = None,
        gateway_unique_id: str = None,
        group_name: str = None,
        id: int = None,
        meta_info: str = None,
        name: str = None,
        namespace: str = None,
        source_type: str = None,
    ):
        self.gateway_traffic_policy = gateway_traffic_policy
        self.gateway_unique_id = gateway_unique_id
        self.group_name = group_name
        self.id = id
        self.meta_info = meta_info
        self.name = name
        self.namespace = namespace
        self.source_type = source_type

    def validate(self):
        if self.gateway_traffic_policy:
            self.gateway_traffic_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_traffic_policy is not None:
            result['GatewayTrafficPolicy'] = self.gateway_traffic_policy.to_map()

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayTrafficPolicy') is not None:
            temp_model = main_models.TrafficPolicy()
            self.gateway_traffic_policy = temp_model.from_map(m.get('GatewayTrafficPolicy'))

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

