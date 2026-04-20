# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIpamPoolCidrResponseBody(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        request_id: str = None,
    ):
        # The successfully provisioned CIDR block.
        self.cidr = cidr
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

