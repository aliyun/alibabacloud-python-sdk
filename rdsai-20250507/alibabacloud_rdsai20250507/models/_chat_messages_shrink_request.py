# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatMessagesShrinkRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        inputs_shrink: str = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        self.conversation_id = conversation_id
        self.inputs_shrink = inputs_shrink
        self.parent_message_id = parent_message_id
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink

        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')

        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

