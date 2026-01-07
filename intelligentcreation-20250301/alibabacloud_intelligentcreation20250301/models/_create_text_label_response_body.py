# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTextLabelResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        tokens: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tokens is not None:
            result['Tokens'] = self.tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')

        return self

