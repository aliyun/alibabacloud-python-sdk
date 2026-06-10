# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimQuestionRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
        title: str = None,
    ):
        # The business space key. If omitted, the default business space is used. You can find the key on the business management page of your main account.
        self.agent_key = agent_key
        # The knowledge ID.
        # 
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # The similar question title. Maximum length: 120 characters.
        # 
        # This parameter is required.
        self.title = title

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

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

