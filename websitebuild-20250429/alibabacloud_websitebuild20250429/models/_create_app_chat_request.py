# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppChatRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        chat_id: str = None,
        conversation_id: str = None,
        messages: str = None,
        site_id: str = None,
    ):
        self.bot_id = bot_id
        self.chat_id = chat_id
        self.conversation_id = conversation_id
        self.messages = messages
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.messages is not None:
            result['Messages'] = self.messages

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Messages') is not None:
            self.messages = m.get('Messages')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

