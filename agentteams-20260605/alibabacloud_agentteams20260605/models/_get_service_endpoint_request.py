# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceEndpointRequest(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

