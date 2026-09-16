# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLumaChunksRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        document_id: str = None,
        enabled: bool = None,
        keyword: str = None,
        knowledge_base_name: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the agent. You can call ListLumaCatalogs to obtain this value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The ID of the document used to filter text chunks. If this parameter is not specified, text chunks of all documents in the knowledge base are returned.
        self.document_id = document_id
        # Specifies whether to return only enabled text chunks. If this parameter is not specified, text chunks are not filtered by enabled status.
        self.enabled = enabled
        # The keyword used to filter text chunks by content.
        self.keyword = keyword
        # The name of the knowledge base bound to the agent. You can call ListLumaKnowledgeBases to obtain this value.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The maximum number of records to return. Valid values: 1 to 100. If this parameter is not specified, the server uses a default value.
        self.max_results = max_results
        # The name of the namespace bound to the agent. You can call ListLumaNamespaces to obtain this value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The pagination token. Do not specify this parameter for the first request. For subsequent requests, use the NextToken value returned in the previous response. This value is an opaque string. Do not parse it.
        self.next_token = next_token

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

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

