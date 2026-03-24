# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelChatRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        answer: str = None,
        chat_id: str = None,
        instance_id: str = None,
        session_id: str = None,
        type: str = None,
    ):
        self.agent_key = agent_key
        self.answer = answer
        self.chat_id = chat_id
        self.instance_id = instance_id
        self.session_id = session_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.answer is not None:
            result['Answer'] = self.answer

        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

