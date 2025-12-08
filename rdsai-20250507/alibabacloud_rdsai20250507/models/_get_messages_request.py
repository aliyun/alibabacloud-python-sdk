# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMessagesRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        first_id: str = None,
        limit: int = None,
    ):
        self.conversation_id = conversation_id
        self.first_id = first_id
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.first_id is not None:
            result['FirstId'] = self.first_id

        if self.limit is not None:
            result['Limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('FirstId') is not None:
            self.first_id = m.get('FirstId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        return self

