# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListProjectRolesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListProjectRolesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. Use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListProjectRolesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectRolesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        project_roles: List[main_models.ListProjectRolesResponseBodyPagingInfoProjectRoles] = None,
        total_count: str = None,
    ):
        # The returned page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # A list of workspace roles.
        self.project_roles = project_roles
        # The total number of matching entries.
        self.total_count = total_count

    def validate(self):
        if self.project_roles:
            for v1 in self.project_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProjectRoles'] = []
        if self.project_roles is not None:
            for k1 in self.project_roles:
                result['ProjectRoles'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.project_roles = []
        if m.get('ProjectRoles') is not None:
            for k1 in m.get('ProjectRoles'):
                temp_model = main_models.ListProjectRolesResponseBodyPagingInfoProjectRoles()
                self.project_roles.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProjectRolesResponseBodyPagingInfoProjectRoles(DaraModel):
    def __init__(
        self,
        code: str = None,
        module_permissions: List[main_models.ListProjectRolesResponseBodyPagingInfoProjectRolesModulePermissions] = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The code of the workspace role.
        self.code = code
        self.module_permissions = module_permissions
        # The name of the workspace role.
        self.name = name
        # The ID of the DataWorks workspace.
        # 
        # Note: For system-defined roles, this parameter returns -1.
        self.project_id = project_id
        # The type of the workspace role.
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
                temp_model = main_models.ListProjectRolesResponseBodyPagingInfoProjectRolesModulePermissions()
                self.module_permissions.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListProjectRolesResponseBodyPagingInfoProjectRolesModulePermissions(DaraModel):
    def __init__(
        self,
        module_id: int = None,
        module_name: str = None,
        permission_type: str = None,
    ):
        self.module_id = module_id
        self.module_name = module_name
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

