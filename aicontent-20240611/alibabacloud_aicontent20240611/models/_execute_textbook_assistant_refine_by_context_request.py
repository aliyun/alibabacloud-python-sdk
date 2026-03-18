# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteTextbookAssistantRefineByContextRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        chat_id: str = None,
        scenario: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.chat_id = chat_id
        # This parameter is required.
        self.scenario = scenario
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

