# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomRoutingEndpointGroupDestinationsRequest(DaraModel):
    def __init__(
        self,
        destination_id: str = None,
        endpoint_group_id: str = None,
        region_id: str = None,
    ):
        # The ID of the endpoint group mapping configuration.
        # 
        # This parameter is required.
        self.destination_id = destination_id
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
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
        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

