# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateVpcIpv6CidrResponseBody(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        request_id: str = None,
    ):
        # The IPv6 CIDR block that is reserved.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

