# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppChatMessagesRequest(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        conversation_id: str = None,
        max_results: int = None,
        next_token: str = None,
        section_id: str = None,
    ):
        self.chat_id = chat_id
        self.conversation_id = conversation_id
        self.max_results = max_results
        self.next_token = next_token
        self.section_id = section_id

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        return self

