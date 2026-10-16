# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderSyncScopeResponseBody(DaraModel):
    def __init__(
        self,
        estimate_status: str = None,
        estimated_user_count: int = None,
        expanded_department_count: int = None,
        request_id: str = None,
        selected_departments: List[main_models.GetIdentityProviderSyncScopeResponseBodySelectedDepartments] = None,
        sync_scope: main_models.GetIdentityProviderSyncScopeResponseBodySyncScope = None,
    ):
        self.estimate_status = estimate_status
        self.estimated_user_count = estimated_user_count
        self.expanded_department_count = expanded_department_count
        self.request_id = request_id
        self.selected_departments = selected_departments
        self.sync_scope = sync_scope

    def validate(self):
        if self.selected_departments:
            for v1 in self.selected_departments:
                 if v1:
                    v1.validate()
        if self.sync_scope:
            self.sync_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.estimate_status is not None:
            result['EstimateStatus'] = self.estimate_status

        if self.estimated_user_count is not None:
            result['EstimatedUserCount'] = self.estimated_user_count

        if self.expanded_department_count is not None:
            result['ExpandedDepartmentCount'] = self.expanded_department_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SelectedDepartments'] = []
        if self.selected_departments is not None:
            for k1 in self.selected_departments:
                result['SelectedDepartments'].append(k1.to_map() if k1 else None)

        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimateStatus') is not None:
            self.estimate_status = m.get('EstimateStatus')

        if m.get('EstimatedUserCount') is not None:
            self.estimated_user_count = m.get('EstimatedUserCount')

        if m.get('ExpandedDepartmentCount') is not None:
            self.expanded_department_count = m.get('ExpandedDepartmentCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.selected_departments = []
        if m.get('SelectedDepartments') is not None:
            for k1 in m.get('SelectedDepartments'):
                temp_model = main_models.GetIdentityProviderSyncScopeResponseBodySelectedDepartments()
                self.selected_departments.append(temp_model.from_map(k1))

        if m.get('SyncScope') is not None:
            temp_model = main_models.GetIdentityProviderSyncScopeResponseBodySyncScope()
            self.sync_scope = temp_model.from_map(m.get('SyncScope'))

        return self

class GetIdentityProviderSyncScopeResponseBodySyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        self.department_ids = department_ids
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_ids is not None:
            result['DepartmentIds'] = self.department_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentIds') is not None:
            self.department_ids = m.get('DepartmentIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class GetIdentityProviderSyncScopeResponseBodySelectedDepartments(DaraModel):
    def __init__(
        self,
        exists: bool = None,
        id: str = None,
        name: str = None,
    ):
        self.exists = exists
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exists is not None:
            result['Exists'] = self.exists

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

