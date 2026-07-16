# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class GetWorkspaceRoleResponseBody(DaraModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        module_permissions: List[main_models.GetWorkspaceRoleResponseBodyModulePermissions] = None,
        request_id: str = None,
        role_id: str = None,
        role_name: str = None,
        status: str = None,
    ):
        # The Alibaba Cloud account UID of the creator.
        self.creator = creator
        # The time when the role was created. It is specified in UTC and formatted in ISO 8601.
        self.gmt_create_time = gmt_create_time
        # The time when the role was last modified. It is specified in UTC and formatted in ISO 8601.
        self.gmt_modified_time = gmt_modified_time
        # The permission configuration of the role.
        self.module_permissions = module_permissions
        # The request ID.
        self.request_id = request_id
        # The role ID.
        self.role_id = role_id
        # The role name.
        self.role_name = role_name
        # The task status. Valid values:
        # 
        # - `Creating`: The role is being created.
        # 
        # - `Updating`: The role is being updated.
        # 
        # - `Deleting`: The role is being deleted.
        # 
        # - `Succeeded`: The task succeeded.
        # 
        # - `Failed`: The task failed.
        self.status = status

    def validate(self):
        if self.module_permissions:
            for v1 in self.module_permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['ModulePermissions'] = []
        if self.module_permissions is not None:
            for k1 in self.module_permissions:
                result['ModulePermissions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.module_permissions = []
        if m.get('ModulePermissions') is not None:
            for k1 in m.get('ModulePermissions'):
                temp_model = main_models.GetWorkspaceRoleResponseBodyModulePermissions()
                self.module_permissions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWorkspaceRoleResponseBodyModulePermissions(DaraModel):
    def __init__(
        self,
        module_name: str = None,
        permission_type: str = None,
        permissions: List[main_models.GetWorkspaceRoleResponseBodyModulePermissionsPermissions] = None,
    ):
        # The module name. Valid values are:
        # 
        # - PaiDesigner: PAI-Designer
        # 
        # - Paiflow: workflow
        # 
        # - DSW: PAI-DSW
        # 
        # - DLC: PAI-DLC
        # 
        # - Dataset: dataset
        # 
        # - Model: model
        # 
        # - Image: image
        # 
        # - CodeSource: code source
        # 
        # - PaiWorkspace@@Workspace: Basic workspace information
        # 
        # - PaiWorkspace@@MemberRole: workspace member management
        # 
        # - PaiWorkspace@@Resource: workspace computing resource management
        # 
        # - PaiWorkspace@@Config: workspace configuration center
        # 
        # - ArtLab: ArtLab
        self.module_name = module_name
        # The permission type. Valid values are:
        # 
        # - ReadOnly: read-only access.
        # 
        # - ReadWrite: Allows users to edit and run.
        # 
        # - FullAccess: full control.
        # 
        # - NoPrivilege: no permissions.
        # 
        # - CustomPermissions: custom permissions.
        self.permission_type = permission_type
        # The permissions. This parameter is required and applies only when `PermissionType` is set to `CustomPermissions`.
        self.permissions = permissions

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.GetWorkspaceRoleResponseBodyModulePermissionsPermissions()
                self.permissions.append(temp_model.from_map(k1))

        return self

class GetWorkspaceRoleResponseBodyModulePermissionsPermissions(DaraModel):
    def __init__(
        self,
        permission_codes: List[str] = None,
        permission_rules: List[main_models.GetWorkspaceRoleResponseBodyModulePermissionsPermissionsPermissionRules] = None,
    ):
        # A list of permissions.
        self.permission_codes = permission_codes
        # A list of permission rules.
        self.permission_rules = permission_rules

    def validate(self):
        if self.permission_rules:
            for v1 in self.permission_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_codes is not None:
            result['PermissionCodes'] = self.permission_codes

        result['PermissionRules'] = []
        if self.permission_rules is not None:
            for k1 in self.permission_rules:
                result['PermissionRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionCodes') is not None:
            self.permission_codes = m.get('PermissionCodes')

        self.permission_rules = []
        if m.get('PermissionRules') is not None:
            for k1 in m.get('PermissionRules'):
                temp_model = main_models.GetWorkspaceRoleResponseBodyModulePermissionsPermissionsPermissionRules()
                self.permission_rules.append(temp_model.from_map(k1))

        return self

class GetWorkspaceRoleResponseBodyModulePermissionsPermissionsPermissionRules(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        entity_access_type: str = None,
    ):
        # The access type. Valid values are:
        # 
        # - PUBLIC: All members in the current workspace can perform this action.
        # 
        # - PRIVATE: Only the creator can perform this action.
        # 
        # - ANY: Both the creator and non-creators can perform this action.
        self.accessibility = accessibility
        # The entity access type. This parameter is ignored if `Accessibility` is set to `PUBLIC`. If `Accessibility` is set to `PRIVATE`, the value of this parameter determines the permissions. Valid values are:
        # 
        # - CREATOR: Only the creator can perform this action.
        # 
        # - ANY: Both the creator and non-creators can perform this action.
        self.entity_access_type = entity_access_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.entity_access_type is not None:
            result['EntityAccessType'] = self.entity_access_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('EntityAccessType') is not None:
            self.entity_access_type = m.get('EntityAccessType')

        return self

