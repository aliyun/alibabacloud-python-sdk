# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRTCWhipStreamAddressResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        whip_address: str = None,
    ):
        self.request_id = request_id
        self.whip_address = whip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.whip_address is not None:
            result['WhipAddress'] = self.whip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WhipAddress') is not None:
            self.whip_address = m.get('WhipAddress')

        return self

