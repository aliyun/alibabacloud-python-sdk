# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListEndpointGroupIpAddressCidrBlocksResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_group_region: str = None,
        ip_address_cidr_blocks: List[str] = None,
        request_id: str = None,
        resource_group_id: str = None,
        state: str = None,
    ):
        # The region ID of the endpoint group.
        self.endpoint_group_region = endpoint_group_region
        # The CIDR blocks.
        self.ip_address_cidr_blocks = ip_address_cidr_blocks
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the endpoint group belongs.
        self.resource_group_id = resource_group_id
        # The status of the endpoint group.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.ip_address_cidr_blocks is not None:
            result['IpAddressCidrBlocks'] = self.ip_address_cidr_blocks

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('IpAddressCidrBlocks') is not None:
            self.ip_address_cidr_blocks = m.get('IpAddressCidrBlocks')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

