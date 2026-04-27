# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspacesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        return self

