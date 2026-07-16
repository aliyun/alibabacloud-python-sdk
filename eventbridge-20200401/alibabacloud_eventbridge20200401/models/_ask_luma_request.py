# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AskLumaRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        conversation_id: str = None,
        max_rows: int = None,
        question: str = None,
    ):
        # This parameter is required.
        self.agent_name = agent_name
        self.conversation_id = conversation_id
        self.max_rows = max_rows
        # This parameter is required.
        self.question = question

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.max_rows is not None:
            result['MaxRows'] = self.max_rows

        if self.question is not None:
            result['Question'] = self.question

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('MaxRows') is not None:
            self.max_rows = m.get('MaxRows')

        if m.get('Question') is not None:
            self.question = m.get('Question')

        return self

