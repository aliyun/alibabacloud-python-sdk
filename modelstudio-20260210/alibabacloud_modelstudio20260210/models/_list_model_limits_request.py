# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelLimitsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        model: str = None,
        name: str = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        # The maximum number of results to return. Valid values: 0 to 200.
        self.max_results = max_results
        # The model for exact match.
        self.model = model
        # The model name for fuzzy match.
        self.name = name
        # The pagination token.
        self.next_token = next_token
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

