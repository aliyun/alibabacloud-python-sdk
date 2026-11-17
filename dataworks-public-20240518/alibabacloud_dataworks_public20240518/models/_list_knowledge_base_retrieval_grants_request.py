# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBaseRetrievalGrantsRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        max_results: int = None,
        next_token: str = None,
        principal_type: str = None,
    ):
        # The knowledge base ID.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The number of entries per page. This parameter is optional. Default value: 20. Valid values: 1 to 100.
        self.max_results = max_results
        # The cursor returned from the previous page. Do not specify this parameter for the first request.
        self.next_token = next_token
        # The type of the principal that receives the share. This parameter is optional. Default value: USER. Only USER is supported in the initial release.
        self.principal_type = principal_type

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

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

