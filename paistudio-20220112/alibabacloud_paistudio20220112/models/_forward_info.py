# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ForwardInfo(DaraModel):
    def __init__(
        self,
        eip_allocation_id: str = None,
        nat_gateway_id: str = None,
    ):
        self.eip_allocation_id = eip_allocation_id
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        return self

