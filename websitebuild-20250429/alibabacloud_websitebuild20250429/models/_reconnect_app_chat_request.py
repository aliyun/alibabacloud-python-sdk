# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReconnectAppChatRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        conversation_id: str = None,
        last_event_id: int = None,
    ):
        # The chat record ID.
        self.chat_id = chat_id
        # The session ID.
        self.conversation_id = conversation_id
        # The ID of the last event.
        self.last_event_id = last_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.last_event_id is not None:
            result['LastEventId'] = self.last_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('LastEventId') is not None:
            self.last_event_id = m.get('LastEventId')

        return self

