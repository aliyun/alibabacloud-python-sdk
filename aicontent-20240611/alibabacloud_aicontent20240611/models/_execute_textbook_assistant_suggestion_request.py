# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTextbookAssistantSuggestionRequest(DaraModel):
    def __init__(
        self,
        assistant: str = None,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
    ):
        # The unique identifier for the AI teacher\\"s message.
        # 
        # This parameter is required.
        self.assistant = assistant
        # The authorization token for the API call. To obtain this token, call the operation that generates authorization tokens for the AI teacher feature.
        # 
        # This parameter is required.
        self.auth_token = auth_token
        # The unique identifier for the current chat.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The practice scenario. Valid values are `SYNC` for synchronous practice and `EXPAND` for extended practice.
        # 
        # This parameter is required.
        self.scenario = scenario

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant is not None:
            result['assistant'] = self.assistant

        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.scenario is not None:
            result['scenario'] = self.scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assistant') is not None:
            self.assistant = m.get('assistant')

        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')

        return self

