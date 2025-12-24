# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateEipAddressResponseBody(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eip_address: str = None,
        request_id: str = None,
    ):
        self.allocation_id = allocation_id
        self.eip_address = eip_address
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

