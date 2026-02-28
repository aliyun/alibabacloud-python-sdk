# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVccRouteEntryRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # Destination CIDR block
        self.destination_cidr_block = destination_cidr_block
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        return self

