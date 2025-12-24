# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateNatGatewayResponseBody(DaraModel):
    def __init__(
        self,
        forward_table_ids: List[str] = None,
        nat_gateway_id: str = None,
        request_id: str = None,
        snat_table_ids: List[str] = None,
    ):
        self.forward_table_ids = forward_table_ids
        self.nat_gateway_id = nat_gateway_id
        self.request_id = request_id
        self.snat_table_ids = snat_table_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_table_ids is not None:
            result['ForwardTableIds'] = self.forward_table_ids

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snat_table_ids is not None:
            result['SnatTableIds'] = self.snat_table_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardTableIds') is not None:
            self.forward_table_ids = m.get('ForwardTableIds')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnatTableIds') is not None:
            self.snat_table_ids = m.get('SnatTableIds')

        return self

