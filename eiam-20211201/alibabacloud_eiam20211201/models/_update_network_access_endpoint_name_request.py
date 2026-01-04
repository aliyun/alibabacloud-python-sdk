# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNetworkAccessEndpointNameRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_access_endpoint_id: str = None,
        network_access_endpoint_name: str = None,
    ):
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 专属网络端点ID。
        # 
        # This parameter is required.
        self.network_access_endpoint_id = network_access_endpoint_id
        # 专属网络端点名称。
        # 
        # This parameter is required.
        self.network_access_endpoint_name = network_access_endpoint_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_access_endpoint_id is not None:
            result['NetworkAccessEndpointId'] = self.network_access_endpoint_id

        if self.network_access_endpoint_name is not None:
            result['NetworkAccessEndpointName'] = self.network_access_endpoint_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkAccessEndpointId') is not None:
            self.network_access_endpoint_id = m.get('NetworkAccessEndpointId')

        if m.get('NetworkAccessEndpointName') is not None:
            self.network_access_endpoint_name = m.get('NetworkAccessEndpointName')

        return self

