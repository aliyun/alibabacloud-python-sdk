# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchLumaKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        knowledge_base_name: str = None,
        metadata_filter: str = None,
        mode: str = None,
        namespace: str = None,
        query: str = None,
        rerank: bool = None,
        top_k: int = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the agent. You can call ListLumaCatalogs to obtain this value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The name of the knowledge base bound to the agent. You can call ListLumaKnowledgeBases to obtain this value.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The metadata filter conditions. The value is a JSON string used to filter the recall scope based on document metadata. For available fields, see the MetadataSchema of the knowledge base.
        self.metadata_filter = metadata_filter
        # The retrieve mode. Valid values: vector (AISearch), keyword (keyword retrieve), and hybrid (hybrid retrieve). If you do not specify this parameter, the retrieve configuration of the knowledge base is used.
        self.mode = mode
        # The name of the namespace bound to the agent. You can call ListLumaNamespaces to obtain this value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The search query in natural language.
        # 
        # This parameter is required.
        self.query = query
        # Specifies whether to enable reranking. If enabled, the recalled results are reranked to improve precision at the cost of longer execution duration. If you do not specify this parameter, the search configuration of the knowledge base is used.
        self.rerank = rerank
        # The number of text chunks to return. Valid values: 1 to 100. If you do not specify this parameter, the search configuration of the knowledge base is used.
        self.top_k = top_k

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

        if self.metadata_filter is not None:
            result['MetadataFilter'] = self.metadata_filter

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.query is not None:
            result['Query'] = self.query

        if self.rerank is not None:
            result['Rerank'] = self.rerank

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MetadataFilter') is not None:
            self.metadata_filter = m.get('MetadataFilter')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Rerank') is not None:
            self.rerank = m.get('Rerank')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

