# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateProjectRoleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        module_permissions: List[main_models.UpdateProjectRoleRequestModulePermissions] = None,
        project_id: int = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.module_permissions = module_permissions
        # This parameter is required.
        self.project_id = project_id

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.code is not None:
            result['Code'] = self.code

        result['ModulePermissions'] = []
        if self.module_permissions is not None:
            for k1 in self.module_permissions:
                result['ModulePermissions'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.module_permissions = []
        if m.get('ModulePermissions') is not None:
            for k1 in m.get('ModulePermissions'):
                temp_model = main_models.UpdateProjectRoleRequestModulePermissions()
                self.module_permissions.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class UpdateProjectRoleRequestModulePermissions(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        permission_type: str = None,
    ):
        self.module_id = module_id
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

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        return self

