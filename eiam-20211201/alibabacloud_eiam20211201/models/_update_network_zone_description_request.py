# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkZoneDescriptionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        network_zone_id: str = None,
    ):
        self.client_token = client_token
        # 网络区域描述
        # 
        # This parameter is required.
        self.description = description
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # IDaaS的网络区域主键id
        # 
        # This parameter is required.
        self.network_zone_id = network_zone_id

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

        if self.network_zone_id is not None:
            result['NetworkZoneId'] = self.network_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkZoneId') is not None:
            self.network_zone_id = m.get('NetworkZoneId')

        return self

