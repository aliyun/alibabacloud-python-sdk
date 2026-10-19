# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnassociateNetworkCidrBlockRequest(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        network_id: str = None,
        secondary_cidr_block: str = None,
    ):
        # The secondary IPv6 CIDR block to delete.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The network ID.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The secondary IPv4 CIDR block to delete.
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        return self

