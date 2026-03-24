# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSimQuestionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.knowledge_id = knowledge_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        return self

