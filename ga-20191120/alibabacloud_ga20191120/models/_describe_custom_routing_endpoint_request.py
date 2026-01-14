# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomRoutingEndpointRequest(DaraModel):
    def __init__(
        self,
        endpoint_group: str = None,
        endpoint_id: str = None,
        region_id: str = None,
    ):
        # The ID of the endpoint group.
        self.endpoint_group = endpoint_group
        # The ID of the endpoint.
        # 
        # This parameter is required.
        self.endpoint_id = endpoint_id
        # The ID of the region where the Global Accelerator (GA) instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_group is not None:
            result['EndpointGroup'] = self.endpoint_group

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroup') is not None:
            self.endpoint_group = m.get('EndpointGroup')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

