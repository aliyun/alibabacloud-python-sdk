# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLimitationResponseBody(DaraModel):
    def __init__(
        self,
        limitation: str = None,
        request_id: str = None,
        value: str = None,
    ):
        self.limitation = limitation
        self.request_id = request_id
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limitation is not None:
            result['Limitation'] = self.limitation

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limitation') is not None:
            self.limitation = m.get('Limitation')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

