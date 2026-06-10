# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppCodeRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        conversation_id: str = None,
    ):
        # Edit operation Content (JSON)
        self.content = content
        # session ID
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        return self

