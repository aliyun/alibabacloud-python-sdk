# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SinkAgentCoreKnowledgeBaseParameters(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        role_name: str = None,
        workspace_id: str = None,
    ):
        # The AgentCore knowledge base ID.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The AgentCore knowledge base role name.
        # 
        # This parameter is required.
        self.role_name = role_name
        # The AgentCore workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

