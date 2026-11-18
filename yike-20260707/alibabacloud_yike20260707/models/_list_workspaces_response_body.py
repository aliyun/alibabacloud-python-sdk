# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        workspace_list: List[main_models.ListWorkspacesResponseBodyWorkspaceList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of workspaces that meet the query conditions.
        self.total_count = total_count
        # The list of workspaces on the current page.
        self.workspace_list = workspace_list

    def validate(self):
        if self.workspace_list:
            for v1 in self.workspace_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WorkspaceList'] = []
        if self.workspace_list is not None:
            for k1 in self.workspace_list:
                result['WorkspaceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workspace_list = []
        if m.get('WorkspaceList') is not None:
            for k1 in m.get('WorkspaceList'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspaceList()
                self.workspace_list.append(temp_model.from_map(k1))

        return self

class ListWorkspacesResponseBodyWorkspaceList(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        default_project_id: str = None,
        status: str = None,
        title: str = None,
        user_count: str = None,
        workspace_id: str = None,
    ):
        # The workspace code.
        self.code = code
        # The creation time. The time follows the ISO 8601 standard and is displayed in UTC.
        self.create_time = create_time
        # The ID of the default project for the workspace.
        self.default_project_id = default_project_id
        # The workspace status. Valid values: Online: enabled. Offline: disabled.
        self.status = status
        # The workspace name.
        self.title = title
        # The current number of users in the workspace, returned as a string.
        self.user_count = user_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_project_id is not None:
            result['DefaultProjectId'] = self.default_project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultProjectId') is not None:
            self.default_project_id = m.get('DefaultProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

