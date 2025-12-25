# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListWorkspacesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        workspace_name: str = None,
        workspace_name_list: List[str] = None,
    ):
        # Page size
        # Default value:
        # 	50
        # Maximum value:
        # 	50
        self.max_results = max_results
        # Pagination Token
        self.next_token = next_token
        # Region
        self.region = region
        # Workspace name, fuzzy search
        self.workspace_name = workspace_name
        # Workspace name, exact match
        self.workspace_name_list = workspace_name_list

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

        if self.region is not None:
            result['region'] = self.region

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.workspace_name_list is not None:
            result['workspaceNameList'] = self.workspace_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('workspaceNameList') is not None:
            self.workspace_name_list = m.get('workspaceNameList')

        return self

