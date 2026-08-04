# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListWorkspacesRequestTags] = None,
        workspace_name: str = None,
        workspace_name_list: List[str] = None,
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
        self.tags = tags
        # The workspace name. Fuzzy match is used.
        self.workspace_name = workspace_name
        # The workspace name. Exact match is used.
        self.workspace_name_list = workspace_name_list

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

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

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListWorkspacesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        if m.get('workspaceNameList') is not None:
            self.workspace_name_list = m.get('workspaceNameList')

        return self

class ListWorkspacesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

