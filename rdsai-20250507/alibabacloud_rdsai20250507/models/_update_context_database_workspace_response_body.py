# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateContextDatabaseWorkspaceResponseBody(DaraModel):
    def __init__(
        self,
        capabilities: main_models.UpdateContextDatabaseWorkspaceResponseBodyCapabilities = None,
        cluster_id: str = None,
        console_permission_mode: str = None,
        created_at: str = None,
        permission_mode: str = None,
        request_id: str = None,
        status: str = None,
        type: str = None,
        viewer: main_models.UpdateContextDatabaseWorkspaceResponseBodyViewer = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The account-level capability information of the current request. It only indicates the operations that the account compatibility adapter can perform and does not represent resource-level authorization. This field is optional and is not returned if no account-level executable operations are provided.
        self.capabilities = capabilities
        # The ID of the cluster to which the workspace belongs. For shared clusters, `default` is returned. For dedicated clusters, the corresponding cluster ID is returned.
        self.cluster_id = cluster_id
        # The permission mode used by the server to parse the identity of the current request. Valid values:
        # - `personal_compatibility`: compatibility mode.
        # - `advanced`: advanced permission mode.
        # 
        # This field describes the identity context of the current request. For the actual permission mode of the workspace, refer to PermissionMode.
        self.console_permission_mode = console_permission_mode
        # The creation time in ISO 8601 format.
        self.created_at = created_at
        # The permission mode of the workspace. Valid values:
        # - `personal_compatibility`: compatibility mode.
        # - `advanced`: advanced permission mode.
        self.permission_mode = permission_mode
        # The request ID.
        self.request_id = request_id
        # The workspace status.
        self.status = status
        # The workspace type.
        self.type = type
        # The viewer identity information of the current request, including the identity resolution mode, caller account type, and member information. Member-related fields are optional.
        self.viewer = viewer
        # The workspace ID.
        self.workspace_id = workspace_id
        # The updated name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()
        if self.viewer:
            self.viewer.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.console_permission_mode is not None:
            result['ConsolePermissionMode'] = self.console_permission_mode

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.permission_mode is not None:
            result['PermissionMode'] = self.permission_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.viewer is not None:
            result['Viewer'] = self.viewer.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capabilities') is not None:
            temp_model = main_models.UpdateContextDatabaseWorkspaceResponseBodyCapabilities()
            self.capabilities = temp_model.from_map(m.get('Capabilities'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConsolePermissionMode') is not None:
            self.console_permission_mode = m.get('ConsolePermissionMode')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('PermissionMode') is not None:
            self.permission_mode = m.get('PermissionMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Viewer') is not None:
            temp_model = main_models.UpdateContextDatabaseWorkspaceResponseBodyViewer()
            self.viewer = temp_model.from_map(m.get('Viewer'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class UpdateContextDatabaseWorkspaceResponseBodyViewer(DaraModel):
    def __init__(
        self,
        bound_member_id: str = None,
        bound_member_role: str = None,
        bound_member_status: str = None,
        caller_type: str = None,
        identity_mode: str = None,
        selected_member_id: str = None,
    ):
        # The ID of the bound workspace member in the identity information of the current request. Optional. This field is empty if no bound member information is provided.
        self.bound_member_id = bound_member_id
        # The role of the bound member in the workspace, such as `Owner`. Optional. This field is empty if no bound member role information is provided.
        self.bound_member_role = bound_member_role
        # The status of the bound member, such as `active`. Optional. This field is empty if no bound member status information is provided.
        self.bound_member_status = bound_member_status
        # The account type of the caller for the current request, such as `customer`. This field describes the caller account and does not indicate the role of a workspace member.
        self.caller_type = caller_type
        # The identity resolution mode of the current request. Valid values:
        # - `account_compatibility`: account compatibility identity mode.
        # - `bound_member`: bound member identity mode.
        # 
        # The identity resolution mode and the workspace permission mode are different concepts. You cannot infer whether advanced permissions are enabled for the workspace based on this field.
        self.identity_mode = identity_mode
        # The ID of the selected workspace member in the account compatibility identity mode. Optional. This field is empty if no member is selected for the current request. This field and the bound member ID represent the member selection result and the binding relationship, respectively.
        self.selected_member_id = selected_member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_member_id is not None:
            result['BoundMemberId'] = self.bound_member_id

        if self.bound_member_role is not None:
            result['BoundMemberRole'] = self.bound_member_role

        if self.bound_member_status is not None:
            result['BoundMemberStatus'] = self.bound_member_status

        if self.caller_type is not None:
            result['CallerType'] = self.caller_type

        if self.identity_mode is not None:
            result['IdentityMode'] = self.identity_mode

        if self.selected_member_id is not None:
            result['SelectedMemberId'] = self.selected_member_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundMemberId') is not None:
            self.bound_member_id = m.get('BoundMemberId')

        if m.get('BoundMemberRole') is not None:
            self.bound_member_role = m.get('BoundMemberRole')

        if m.get('BoundMemberStatus') is not None:
            self.bound_member_status = m.get('BoundMemberStatus')

        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')

        if m.get('IdentityMode') is not None:
            self.identity_mode = m.get('IdentityMode')

        if m.get('SelectedMemberId') is not None:
            self.selected_member_id = m.get('SelectedMemberId')

        return self

class UpdateContextDatabaseWorkspaceResponseBodyCapabilities(DaraModel):
    def __init__(
        self,
        executable_actions: List[str] = None,
    ):
        # The list of operation names that the account compatibility adapter can perform. The list content does not represent read/write, member group, or access control authorization for specific resources.
        self.executable_actions = executable_actions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executable_actions is not None:
            result['ExecutableActions'] = self.executable_actions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutableActions') is not None:
            self.executable_actions = m.get('ExecutableActions')

        return self

