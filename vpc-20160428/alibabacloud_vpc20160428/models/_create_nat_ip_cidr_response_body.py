# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNatIpCidrResponseBody(DaraModel):
    def __init__(
        self,
        nat_ip_cidr_id: str = None,
        request_id: str = None,
    ):
        # The ID of the NAT CIDR block.
        self.nat_ip_cidr_id = nat_ip_cidr_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_ip_cidr_id is not None:
            result['NatIpCidrId'] = self.nat_ip_cidr_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatIpCidrId') is not None:
            self.nat_ip_cidr_id = m.get('NatIpCidrId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

