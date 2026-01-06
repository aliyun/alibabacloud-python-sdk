# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        admin_names: List[str] = None,
        creator: str = None,
        description: str = None,
        display_name: str = None,
        env_types: List[str] = None,
        extra_infos: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        is_default: bool = None,
        owner: main_models.GetWorkspaceResponseBodyOwner = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The names of the administrator accounts.
        self.admin_names = admin_names
        # The ID of the user who creates the workspace.
        self.creator = creator
        # The description of the workspace.
        self.description = description
        # The display name of the workspace.
        self.display_name = display_name
        # The environment information of the workspace.
        # 
        # *   Workspaces in basic mode can run only in the production environment.
        # *   Workspaces in standard mode can run in both the development and production environments.
        self.env_types = env_types
        # The additional information, which only contains the TenantId field.
        self.extra_infos = extra_infos
        # The time when the workspace is created, in UTC. The time follows the ISO 8601 standard.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace is modified, in UTC. The time follows the ISO 8601 standard.
        self.gmt_modified_time = gmt_modified_time
        # Indicates whether the workspace is the default workspace. Valid values:
        # 
        # *   false
        # *   true
        self.is_default = is_default
        # The information about the workspace owner. This parameter is valid only when Verbose is set to true.
        self.owner = owner
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The workspace state. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE:
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_names is not None:
            result['AdminNames'] = self.admin_names

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.env_types is not None:
            result['EnvTypes'] = self.env_types

        if self.extra_infos is not None:
            result['ExtraInfos'] = self.extra_infos

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminNames') is not None:
            self.admin_names = m.get('AdminNames')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EnvTypes') is not None:
            self.env_types = m.get('EnvTypes')

        if m.get('ExtraInfos') is not None:
            self.extra_infos = m.get('ExtraInfos')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Owner') is not None:
            temp_model = main_models.GetWorkspaceResponseBodyOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class GetWorkspaceResponseBodyOwner(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        user_id: str = None,
        user_kp: str = None,
        user_name: str = None,
    ):
        # The display name.
        self.display_name = display_name
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
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_kp is not None:
            result['UserKp'] = self.user_kp

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserKp') is not None:
            self.user_kp = m.get('UserKp')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

