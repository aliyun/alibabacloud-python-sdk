# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListWorkspacesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_limits: Dict[str, Any] = None,
        total_count: int = None,
        workspaces: List[main_models.ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The resource types and quantity limits that a user can activate within a workspace. This list is returned when Option is set to GetResourceLimits.
        # Currently supported resource types include:
        # * MaxCompute_share: MaxCompute pay-as-you-go.
        # * MaxCompute_isolate: MaxCompute subscription.
        # * DLC_share: DLC pay-as-you-go.
        # * PAI_isolate: PAI subscription.
        # * PAI_share: PAI pay-as-you-go.
        # * DataWorks_isolate: DataWorks subscription.
        # * DataWorks_share: DataWorks pay-as-you-go.
        self.resource_limits = resource_limits
        # The total number of workspaces that match the query conditions.
        self.total_count = total_count
        # The list of workspace details. This list is returned when Option is set to GetWorkspaces.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_limits is not None:
            result['ResourceLimits'] = self.resource_limits

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Workspaces'] = []
        if self.workspaces is not None:
            for k1 in self.workspaces:
                result['Workspaces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceLimits') is not None:
            self.resource_limits = m.get('ResourceLimits')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workspaces = []
        if m.get('Workspaces') is not None:
            for k1 in m.get('Workspaces'):
                temp_model = main_models.ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k1))

        return self

class ListWorkspacesResponseBodyWorkspaces(DaraModel):
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
        status: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        resource_group_id: str = None,
    ):
        # The list of administrator account names.
        self.admin_names = admin_names
        # The user ID of the creator.
        self.creator = creator
        # The workspace description.
        self.description = description
        self.display_name = display_name
        # The list of environments in the workspace.
        self.env_types = env_types
        # The extended information. Currently, this includes TenantId, which represents the tenant ID.
        self.extra_infos = extra_infos
        # The time when the workspace was created. The time follows the ISO 8601 standard in UTC+0. Format: yyyy-MM-ddTHH:mm:ss.SSSZ.
        self.gmt_create_time = gmt_create_time
        # The time when the workspace was last modified. The time follows the ISO 8601 standard in UTC+0. Format: yyyy-MM-ddTHH:mmZ.
        self.gmt_modified_time = gmt_modified_time
        # Indicates whether the workspace is the default workspace.
        self.is_default = is_default
        # The workspace status.
        self.status = status
        # The workspace ID.
        self.workspace_id = workspace_id
        # The workspace name.
        self.workspace_name = workspace_name
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

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

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        return self

