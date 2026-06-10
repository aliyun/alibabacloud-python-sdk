# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppChatMessageRequest(DaraModel):
    def __init__(
        self,
        added_meta_data: str = None,
        content: str = None,
        conversation_id: str = None,
        message_id: str = None,
    ):
        # Appended message metadata (JSON format)
        self.added_meta_data = added_meta_data
        # Message content
        self.content = content
        # Session ID
        self.conversation_id = conversation_id
        # Message ID
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_meta_data is not None:
            result['AddedMetaData'] = self.added_meta_data

        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedMetaData') is not None:
            self.added_meta_data = m.get('AddedMetaData')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

