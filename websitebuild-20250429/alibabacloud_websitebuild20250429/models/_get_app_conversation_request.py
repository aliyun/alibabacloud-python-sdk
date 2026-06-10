# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppConversationRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        conversation_id: str = None,
    ):
        # Bot ID
        self.bot_id = bot_id
        # Session ID
        self.conversation_id = conversation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        return self

