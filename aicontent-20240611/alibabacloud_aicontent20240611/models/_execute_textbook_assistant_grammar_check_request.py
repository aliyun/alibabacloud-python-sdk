# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTextbookAssistantGrammarCheckRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user: str = None,
    ):
        # The authorization token for the API call. Obtain this token by calling the "Authorization token for the Textbook-style AI English Teacher" API.
        # 
        # This parameter is required.
        self.auth_token = auth_token
        # The ID of the current conversation.
        # 
        # This parameter is required.
        self.chat_id = chat_id
        # The use case. Valid values: `SYNC` for synchronous practice and `EXPAND` for expansion practice.
        # 
        # This parameter is required.
        self.scenario = scenario
        # The message ID of the user\\"s reply.
        # 
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.chat_id is not None:
            result['chatId'] = self.chat_id

        if self.scenario is not None:
            result['scenario'] = self.scenario

        if self.user is not None:
            result['user'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('scenario') is not None:
            self.scenario = m.get('scenario')

        if m.get('user') is not None:
            self.user = m.get('user')

        return self

