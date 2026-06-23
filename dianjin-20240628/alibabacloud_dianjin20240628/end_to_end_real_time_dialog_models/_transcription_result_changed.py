# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TranscriptionResultChanged(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        content: str = None,
    ):
        self.message_id = message_id
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.content is not None:
            result['content'] = self.content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('content') is not None:
            self.content = m.get('content')

        return self

