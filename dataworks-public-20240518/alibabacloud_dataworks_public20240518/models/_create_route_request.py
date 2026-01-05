# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRouteRequest(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        network_id: int = None,
        resource_group_id: str = None,
    ):
        # The CIDR blocks of the destination-based route.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The network ID.
        # 
        # This parameter is required.
        self.network_id = network_id
        # Unique identifier of the serverless resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

