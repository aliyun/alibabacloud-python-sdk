# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateProjectRoleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        module_permissions: List[main_models.CreateProjectRoleRequestModulePermissions] = None,
        name: str = None,
        project_id: int = None,
    ):
        # The client token.
        self.client_token = client_token
        # The list of DataWorks module permissions.
        self.module_permissions = module_permissions
        # The role name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace on which the API operation is performed.
        # 
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

        result['ModulePermissions'] = []
        if self.module_permissions is not None:
            for k1 in self.module_permissions:
                result['ModulePermissions'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.module_permissions = []
        if m.get('ModulePermissions') is not None:
            for k1 in m.get('ModulePermissions'):
                temp_model = main_models.CreateProjectRoleRequestModulePermissions()
                self.module_permissions.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreateProjectRoleRequestModulePermissions(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        permission_type: str = None,
    ):
        # The DataWorks module ID. Valid values:
        # 
        # - 2: HoloStudio
        # 
        # - 3: StreamStudio
        # 
        # - 4: Deployment management
        # 
        # - 6: Data Security Guard
        # 
        # - 7: Data Map
        # 
        # - 8: Data Service
        # 
        # - 9: Data Integration
        # 
        # - 10: Data Modeling (DataBlau DDM)
        # 
        # - 11: Data Studio
        # 
        # - 12: Data Quality
        # 
        # - 13: Data Governance
        # 
        # - 14: Operation Center
        # 
        # - 15: Resource optimization
        # 
        # - 16: Migration Assistant
        # 
        # - 17: Data Analysis
        # 
        # - 18: Approval center
        # 
        # - 19: Security Center
        # 
        # - 20: Intelligent Data Modeling
        self.module_id = module_id
        # The permission type. Valid values:
        # 
        # - Write: Read-only
        # 
        # - Read: Edit
        # 
        # - NotSet: Not controlled
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

