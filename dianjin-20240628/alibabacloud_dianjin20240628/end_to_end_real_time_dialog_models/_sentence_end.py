# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SentenceEnd(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        data: List[int] = None,
    ):
        self.message_id = message_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.data is not None:
            result['data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('data') is not None:
            self.data = m.get('data')

        return self

