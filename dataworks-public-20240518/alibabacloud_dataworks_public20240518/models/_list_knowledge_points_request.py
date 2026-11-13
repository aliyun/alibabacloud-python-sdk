# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgePointsRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # The stable ID of the target knowledge base. You can obtain the ID by calling the ListKnowledgeBases operation.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The maximum number of knowledge points to return per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination cursor. Do not specify this parameter for the first page. For subsequent pages, pass the NextToken value returned in the previous response as is, and keep the knowledge base, type, and page size unchanged. An empty cursor indicates that no more data is available. If the current page is empty but the cursor is not empty, continue querying.
        self.next_token = next_token
        # The type of the knowledge point. Valid values:
        # - GRAPH: local graph entry.
        # - WIKI: Wiki page.
        # - KNOWLEDGE_CONTENT: knowledge content.
        # If you do not specify this parameter, knowledge points of all types are listed.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

