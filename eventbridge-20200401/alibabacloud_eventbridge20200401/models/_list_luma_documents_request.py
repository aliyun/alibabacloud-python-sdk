# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLumaDocumentsRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        file_name_prefix: str = None,
        knowledge_base_name: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
        status: str = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the agent. You can call ListLumaCatalogs to obtain the catalog name.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The file name prefix used to filter documents.
        self.file_name_prefix = file_name_prefix
        # The name of the knowledge base bound to the agent. You can call ListLumaKnowledgeBases to obtain the knowledge base name.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The maximum number of records to return. Valid values: 1 to 100. If this parameter is not specified, the server uses a default value.
        self.max_results = max_results
        # The name of the namespace bound to the agent. You can call ListLumaNamespaces to obtain the namespace name.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The pagination token. Do not specify this parameter for the first request. For subsequent requests, use the NextToken value returned in the previous response. This value is an opaque string. Do not parse it.
        self.next_token = next_token
        # The processing status used to filter documents. Valid values: Pending, Processing, Ready, and Failed.
        self.status = status

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

        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

