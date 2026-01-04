# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNatGatewayRequest(DaraModel):
    def __init__(
        self,
        force_delete: bool = None,
        nat_gateway_id: str = None,
    ):
        # Specifies whether to forcefully delete the NAT instance.
        self.force_delete = force_delete
        # The ID of the NAT gateway that you want to delete.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        return self

