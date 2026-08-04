# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspacesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        workspace_name: str = None,
        workspace_name_list_shrink: str = None,
    ):
        # The number of entries per page.
        # Default value:
        # 	50
        # Maximum value:
        # 	50
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The region.
        self.region = region
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags_shrink = tags_shrink
        # The workspace name. Fuzzy match is used.
        self.workspace_name = workspace_name
        # The workspace name. Exact match is used.
        self.workspace_name_list_shrink = workspace_name_list_shrink

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

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        if self.workspace_name_list_shrink is not None:
            result['workspaceNameList'] = self.workspace_name_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('workspaceNameList') is not None:
            self.workspace_name_list_shrink = m.get('workspaceNameList')

        return self

