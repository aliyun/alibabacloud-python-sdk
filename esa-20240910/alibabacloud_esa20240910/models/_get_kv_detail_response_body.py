# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKvDetailResponseBody(DaraModel):
    def __init__(
        self,
        expiration_ttl: str = None,
        request_id: str = None,
        value: str = None,
    ):
        # The expiration time of the key. Unit: seconds.
        self.expiration_ttl = expiration_ttl
        # The expiration time of the key. Unit: seconds.
        self.request_id = request_id
        # The value of the key. The value of the root node.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration_ttl is not None:
            result['ExpirationTtl'] = self.expiration_ttl

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpirationTtl') is not None:
            self.expiration_ttl = m.get('ExpirationTtl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

