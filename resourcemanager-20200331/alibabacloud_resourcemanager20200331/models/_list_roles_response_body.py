# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class ListRolesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        roles: main_models.ListRolesResponseBodyRoles = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        self.roles = roles
        # The total number of roles.
        self.total_count = total_count

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.roles is not None:
            result['Roles'] = self.roles.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Roles') is not None:
            temp_model = main_models.ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m.get('Roles'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRolesResponseBodyRoles(DaraModel):
    def __init__(
        self,
        role: List[main_models.ListRolesResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for v1 in self.role:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Role'] = []
        if self.role is not None:
            for k1 in self.role:
                result['Role'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k1 in m.get('Role'):
                temp_model = main_models.ListRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k1))

        return self

class ListRolesResponseBodyRolesRole(DaraModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        is_service_linked_role: bool = None,
        latest_deletion_task: main_models.ListRolesResponseBodyRolesRoleLatestDeletionTask = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        role_principal_name: str = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.create_date = create_date
        self.description = description
        self.is_service_linked_role = is_service_linked_role
        self.latest_deletion_task = latest_deletion_task
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.role_principal_name = role_principal_name
        self.update_date = update_date

    def validate(self):
        if self.latest_deletion_task:
            self.latest_deletion_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.is_service_linked_role is not None:
            result['IsServiceLinkedRole'] = self.is_service_linked_role

        if self.latest_deletion_task is not None:
            result['LatestDeletionTask'] = self.latest_deletion_task.to_map()

        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.role_principal_name is not None:
            result['RolePrincipalName'] = self.role_principal_name

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsServiceLinkedRole') is not None:
            self.is_service_linked_role = m.get('IsServiceLinkedRole')

        if m.get('LatestDeletionTask') is not None:
            temp_model = main_models.ListRolesResponseBodyRolesRoleLatestDeletionTask()
            self.latest_deletion_task = temp_model.from_map(m.get('LatestDeletionTask'))

        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('RolePrincipalName') is not None:
            self.role_principal_name = m.get('RolePrincipalName')

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class ListRolesResponseBodyRolesRoleLatestDeletionTask(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        deletion_task_id: str = None,
    ):
        self.create_date = create_date
        self.deletion_task_id = deletion_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')

        return self

