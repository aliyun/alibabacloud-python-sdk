# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetProjectRoleResponseBody(DaraModel):
    def __init__(
        self,
        project_role: main_models.GetProjectRoleResponseBodyProjectRole = None,
        request_id: str = None,
    ):
        # The details of the workspace role.
        self.project_role = project_role
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project_role:
            self.project_role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_role is not None:
            result['ProjectRole'] = self.project_role.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectRole') is not None:
            temp_model = main_models.GetProjectRoleResponseBodyProjectRole()
            self.project_role = temp_model.from_map(m.get('ProjectRole'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProjectRoleResponseBodyProjectRole(DaraModel):
    def __init__(
        self,
        code: str = None,
        module_permissions: List[main_models.GetProjectRoleResponseBodyProjectRoleModulePermissions] = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The code of the workspace role.
        self.code = code
        # The permissions for the modules in the workspace.
        self.module_permissions = module_permissions
        # The name of the workspace role.
        self.name = name
        # The ID of the DataWorks workspace.
        # 
        # Note: A fixed value of -1 is returned for a system role.
        self.project_id = project_id
        # The type of the workspace role. Valid values:
        # 
        # - UserCustom: a custom role
        # 
        # - System: a system role
        self.type = type

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
        if self.code is not None:
            result['Code'] = self.code

        result['ModulePermissions'] = []
        if self.module_permissions is not None:
            for k1 in self.module_permissions:
                result['ModulePermissions'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.module_permissions = []
        if m.get('ModulePermissions') is not None:
            for k1 in m.get('ModulePermissions'):
                temp_model = main_models.GetProjectRoleResponseBodyProjectRoleModulePermissions()
                self.module_permissions.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetProjectRoleResponseBodyProjectRoleModulePermissions(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        module_name: str = None,
        permission_type: str = None,
    ):
        # The module ID.
        self.module_id = module_id
        # The module name.
        self.module_name = module_name
        # The permission type.
        self.permission_type = permission_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_id is not None:
            result['ModuleId'] = self.module_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        return self

