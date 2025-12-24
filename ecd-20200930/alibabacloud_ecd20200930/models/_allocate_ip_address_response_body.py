# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateIpAddressResponseBody(DaraModel):
    def __init__(
        self,
        eip_address: str = None,
        eip_id: str = None,
        request_id: str = None,
    ):
        self.eip_address = eip_address
        self.eip_id = eip_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_address is not None:
            result['EipAddress'] = self.eip_address

        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddress') is not None:
            self.eip_address = m.get('EipAddress')

        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

