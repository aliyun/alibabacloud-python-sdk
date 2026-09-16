# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLumaKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        knowledge_base_name: str = None,
        namespace: str = None,
    ):
        # The name of the Agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the Agent. You can call ListLumaCatalogs to obtain this value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The name of the knowledge base bound to the Agent. You can call ListLumaKnowledgeBases to obtain this value.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The name of the namespace bound to the Agent. You can call ListLumaNamespaces to obtain this value.
        # 
        # This parameter is required.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

