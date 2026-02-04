# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutDcdnKvResponseBody(DaraModel):
    def __init__(
        self,
        length: int = None,
        request_id: str = None,
        value: str = None,
    ):
        # The length of the key.
        self.length = length
        # The ID of the request.
        self.request_id = request_id
        # The value of the key. If the value exceeds 256 characters in length, the first 100 characters and the last 100 characters are retained and other characters are not displayed.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.length is not None:
            result['Length'] = self.length

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

