# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetDefaultWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.GetDefaultWorkspaceResponseBodyConditions] = None,
        creator: str = None,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        owner: main_models.GetDefaultWorkspaceResponseBodyOwner = None,
        request_id: str = None,
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The conditions of the default workspace in the creation process.
        self.conditions = conditions
        # The UID of the Alibaba Cloud account.
        self.creator = creator
        # The workspace description.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The environments of the workspace. Valid values:
        # 
        # *   Workspaces in basic mode can run only in the production environment.
        # *   Workspaces in standard mode can run in both the development and production environments.
        self.env_types = env_types
        # The time when the workspace was created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace was modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # The UID of the Alibaba Cloud account.
        self.owner = owner
        # The request ID.
        self.request_id = request_id
        # The workspace status. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name, which is unique in a region.
        self.workspace_name = workspace_name

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.owner:
            self.owner.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env_types is not None:
            result['EnvTypes'] = self.env_types

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.GetDefaultWorkspaceResponseBodyConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Owner') is not None:
            temp_model = main_models.GetDefaultWorkspaceResponseBodyOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class GetDefaultWorkspaceResponseBodyOwner(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_kp: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The user ID.
        self.user_kp = user_kp
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_kp is not None:
            result['UserKp'] = self.user_kp

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetDefaultWorkspaceResponseBodyConditions(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        type: str = None,
    ):
        # The returned status code. HTTP status code 200 indicates that the request was successful. Other HTTP status codes indicate that the request failed.
        self.code = code
        # The error message. If the returned status code is 200, this parameter is empty.
        self.message = message
        # The task type. Valid values:
        # 
        # *   CREATING: The workspace is being created.
        # *   WORKSPACE_CREATED: The workspace is created.
        # *   MEMBERS_ADDED: The member is added.
        # *   ENABLED: The workspace is created and the member is added.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

