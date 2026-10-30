# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChunksRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        document_id: str = None,
        enabled: bool = None,
        keyword: str = None,
        knowledge_base_name: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
    ):
        # The data catalog to which the knowledge base belongs. This parameter is used together with Namespace and KnowledgeBaseName to locate the knowledge base. You can obtain the value by calling the ListCatalogs operation.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. If you specify this parameter, only the chunks of the specified document are listed, sorted in ascending order of ChunkSeq within the document. If you do not specify this parameter, the chunks of all documents in the knowledge base are listed, sorted in ascending lexicographical order of DocumentId and then in ascending order of ChunkSeq within the same document, with chunks arranged consecutively. In full-base mode, Keyword filtering is not supported. Use SearchKnowledgeBase instead. In addition, TotalCount is not returned in full-base mode. Pagination ends when NextToken is empty.
        self.document_id = document_id
        # Optional. If you set this parameter to true, only enabled chunks are returned. If you set it to false, only disabled chunks are returned. If you do not specify this parameter, all chunks are returned.
        self.enabled = enabled
        # Optional. This parameter is active only when DocumentId is specified. It filters chunks by keywords in the chunk content. Only chunks that contain the specified keyword are returned. If you specify this parameter in full-base pattern (when DocumentId is not specified), an error is reported. To retrieve full-text content, use SearchKnowledgeBase (set Mode to KEYWORD for full-text index).
        self.keyword = keyword
        # The name of the knowledge base. The name must be unique within the namespace. It is specified upon creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The maximum number of results to return per page. If you do not specify this parameter or set it to 0, the default value 20 is used. The maximum value is 100.
        self.max_results = max_results
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. This parameter is used together with Catalog and KnowledgeBaseName to locate the knowledge base. You can obtain the value by calling the ListNamespaces operation.
        # 
        # This parameter is required.
        self.namespace = namespace
        # You do not need to specify this parameter for the first query. For subsequent queries, use the NextToken value returned in the previous response. An empty value indicates that no more pages are available.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

