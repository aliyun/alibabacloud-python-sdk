# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetKgAuthorizedWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetKgAuthorizedWorkspacesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The request result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetKgAuthorizedWorkspacesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKgAuthorizedWorkspacesResponseBodyData(DaraModel):
    def __init__(
        self,
        total_count: int = None,
        workspace_list: List[main_models.GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceList] = None,
    ):
        # The total number of knowledge graph workspaces that the user has permissions on.
        self.total_count = total_count
        # The list of knowledge graph workspaces that the user has permissions on.
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WorkspaceList'] = []
        if self.workspace_list is not None:
            for k1 in self.workspace_list:
                result['WorkspaceList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workspace_list = []
        if m.get('WorkspaceList') is not None:
            for k1 in m.get('WorkspaceList'):
                temp_model = main_models.GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceList()
                self.workspace_list.append(temp_model.from_map(k1))

        return self

class GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceList(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: str = None,
        last_publish_time: str = None,
        last_publish_version: int = None,
        name: str = None,
        role_list: List[main_models.GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceListRoleList] = None,
        workspace_id: str = None,
    ):
        # The description of the knowledge graph workspace.
        self.description = description
        # The creation time of the knowledge graph workspace.
        self.gmt_create = gmt_create
        # The latest publish time of the knowledge graph workspace. This value is empty if the workspace has never been published successfully.
        self.last_publish_time = last_publish_time
        # The latest publish version number of the knowledge graph workspace. This value is empty if the workspace has never been published successfully.
        self.last_publish_version = last_publish_version
        # The name of the knowledge graph workspace.
        self.name = name
        # The list of roles assigned to the specified user in the workspace. This is an empty list if the user is not a member of the workspace.
        self.role_list = role_list
        # The ID of the knowledge graph workspace.
        self.workspace_id = workspace_id

    def validate(self):
        if self.role_list:
            for v1 in self.role_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.last_publish_time is not None:
            result['LastPublishTime'] = self.last_publish_time

        if self.last_publish_version is not None:
            result['LastPublishVersion'] = self.last_publish_version

        if self.name is not None:
            result['Name'] = self.name

        result['RoleList'] = []
        if self.role_list is not None:
            for k1 in self.role_list:
                result['RoleList'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('LastPublishTime') is not None:
            self.last_publish_time = m.get('LastPublishTime')

        if m.get('LastPublishVersion') is not None:
            self.last_publish_version = m.get('LastPublishVersion')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.role_list = []
        if m.get('RoleList') is not None:
            for k1 in m.get('RoleList'):
                temp_model = main_models.GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceListRoleList()
                self.role_list.append(temp_model.from_map(k1))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class GetKgAuthorizedWorkspacesResponseBodyDataWorkspaceListRoleList(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # The code of the workspace role.
        self.code = code
        # The name of the workspace role.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

