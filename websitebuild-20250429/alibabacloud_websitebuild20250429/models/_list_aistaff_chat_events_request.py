# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAIStaffChatEventsRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        chat_id: str = None,
        conversation_id: str = None,
        last_event_id: int = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The chat ID. This parameter is optional. If not specified, the latest chat ID is used.
        self.chat_id = chat_id
        # The conversation ID.
        self.conversation_id = conversation_id
        # The ID of the last event, used for incremental retrieval.
        self.last_event_id = last_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.last_event_id is not None:
            result['LastEventId'] = self.last_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('LastEventId') is not None:
            self.last_event_id = m.get('LastEventId')

        return self

