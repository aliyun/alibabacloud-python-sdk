# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
        workspaces: List[main_models.ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # The number of entries per page.
        # Default value:
        # 	50
        # Maximum value:
        # 	50
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total
        # The list of workspaces.
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for v1 in self.workspaces:
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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        result['workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        self.workspaces = []
        if m.get('workspaces') is not None:
            for k1 in m.get('workspaces'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k1))

        return self

class ListWorkspacesResponseBodyWorkspaces(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        last_modify_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sls_project: str = None,
        tags: List[main_models.ListWorkspacesResponseBodyWorkspacesTags] = None,
        workspace_name: str = None,
    ):
        # The time when the workspace was created.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the workspace.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The time when the workspace was last modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.last_modify_time = last_modify_time
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The Simple Log Service project name.
        self.sls_project = sls_project
        # The tags.
        self.tags = tags
        # The workspace name.
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.sls_project is not None:
            result['slsProject'] = self.sls_project

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspacesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        return self

class ListWorkspacesResponseBodyWorkspacesTags(DaraModel):
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

