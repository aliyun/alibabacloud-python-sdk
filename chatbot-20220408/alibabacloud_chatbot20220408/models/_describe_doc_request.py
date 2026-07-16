# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDocRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        knowledge_id: int = None,
        show_detail: bool = None,
    ):
        # The key that identifies the workspace. If this parameter is omitted, the default workspace is used. You can find this key on the workspace management page of your root account.
        self.agent_key = agent_key
        # The knowledge ID.
        # 
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # Specifies whether to return detailed information for paragraphs. true: Detailed information is returned. false: Detailed information is not returned (default).
        self.show_detail = show_detail

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

        if self.show_detail is not None:
            result['ShowDetail'] = self.show_detail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('ShowDetail') is not None:
            self.show_detail = m.get('ShowDetail')

        return self

