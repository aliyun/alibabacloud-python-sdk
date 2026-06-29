# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiKeysRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        description: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_by: str = None,
        workspace_id: str = None,
    ):
        # The API key ID for exact match.
        self.api_key_id = api_key_id
        # The keyword for fuzzy match against the description.
        self.description = description
        # The page size.
        self.max_results = max_results
        # The token used to retrieve more results. You do not need to provide this parameter for the first query. For subsequent queries, use the token obtained from the previous response.
        self.next_token = next_token
        # The sort order. Valid values:
        # 
        # - DESC (default)
        # 
        # - ASC.
        self.order = order
        # The field by which to sort results. Valid values:
        # 
        # - apiKeyId (default)
        # 
        # - gmtCreate.
        self.order_by = order_by
        # The workspace ID for exact match.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.description is not None:
            result['description'] = self.description

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order is not None:
            result['order'] = self.order

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

