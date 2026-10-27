# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderSyncScopeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderSyncScopeResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code of the API request. SUCCESS indicates that the request is successful, but does not indicate that the asynchronous synchronization task is completed.
        self.code = code
        # The business data returned by the request.
        self.data = data
        # The HTTP status code of the API request. It does not indicate the execution result of the asynchronous task.
        self.http_status_code = http_status_code
        # The response message of the API request.
        self.message = message
        # The unique identifier of the request. Provide this value when troubleshooting issues.
        self.request_id = request_id
        # Indicates whether the API request is successful. To check whether the asynchronous task is completed, query the task status.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetIdentityProviderSyncScopeResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetIdentityProviderSyncScopeResponseBodyData(DaraModel):
    def __init__(
        self,
        estimate_status: str = None,
        estimated_user_count: int = None,
        expanded_department_count: int = None,
        selected_departments: List[main_models.GetIdentityProviderSyncScopeResponseBodyDataSelectedDepartments] = None,
        sync_scope: main_models.GetIdentityProviderSyncScopeResponseBodyDataSyncScope = None,
    ):
        # The estimation status of the user count for the synchronization scope. The count is available only when the status is Ready. A missing count in other states cannot be considered as 0.
        self.estimate_status = estimate_status
        # The estimated number of users in the saved synchronization scope. This parameter is returned only when estimateStatus is Ready and the downstream system provides the value. It does not represent the number of users that have been synchronized.
        self.estimated_user_count = estimated_user_count
        # The estimated number of departments including sub-departments. This parameter is returned only when estimateStatus is Ready and the downstream system provides the value.
        self.expanded_department_count = expanded_department_count
        # The names and validity of the saved selected departments. This parameter can be an empty array when the mode is AllAuthorized. An empty array does not indicate that the organization has no departments.
        self.selected_departments = selected_departments
        # The saved synchronization scope downstream. AllAuthorized indicates the address book scope authorized for the application.
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
            result['estimateStatus'] = self.estimate_status

        if self.estimated_user_count is not None:
            result['estimatedUserCount'] = self.estimated_user_count

        if self.expanded_department_count is not None:
            result['expandedDepartmentCount'] = self.expanded_department_count

        result['selectedDepartments'] = []
        if self.selected_departments is not None:
            for k1 in self.selected_departments:
                result['selectedDepartments'].append(k1.to_map() if k1 else None)

        if self.sync_scope is not None:
            result['syncScope'] = self.sync_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('estimateStatus') is not None:
            self.estimate_status = m.get('estimateStatus')

        if m.get('estimatedUserCount') is not None:
            self.estimated_user_count = m.get('estimatedUserCount')

        if m.get('expandedDepartmentCount') is not None:
            self.expanded_department_count = m.get('expandedDepartmentCount')

        self.selected_departments = []
        if m.get('selectedDepartments') is not None:
            for k1 in m.get('selectedDepartments'):
                temp_model = main_models.GetIdentityProviderSyncScopeResponseBodyDataSelectedDepartments()
                self.selected_departments.append(temp_model.from_map(k1))

        if m.get('syncScope') is not None:
            temp_model = main_models.GetIdentityProviderSyncScopeResponseBodyDataSyncScope()
            self.sync_scope = temp_model.from_map(m.get('syncScope'))

        return self

class GetIdentityProviderSyncScopeResponseBodyDataSyncScope(DaraModel):
    def __init__(
        self,
        department_ids: List[str] = None,
        mode: str = None,
    ):
        # When the mode is SelectedDepartments, this parameter contains at least one non-empty department ID, which should be obtained from ListIdentityProviderDepartments. When the mode is AllAuthorized, pass an empty array or omit this parameter.
        self.department_ids = department_ids
        # The scope mode. Valid values: AllAuthorized (the entire authorized scope, limited by the application\\"s address book authorization) and SelectedDepartments (the selected departments and all their sub-departments). When explicitly submitting syncScope, a valid mode must be provided and verified by the backend.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_ids is not None:
            result['departmentIds'] = self.department_ids

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('departmentIds') is not None:
            self.department_ids = m.get('departmentIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

class GetIdentityProviderSyncScopeResponseBodyDataSelectedDepartments(DaraModel):
    def __init__(
        self,
        exists: bool = None,
        id: str = None,
        name: str = None,
    ):
        # Indicates whether the selected department still exists. A value of false indicates that the selection is invalid and the synchronization scope must be reconfirmed.
        self.exists = exists
        # The unique identifier of the department returned by the identity provider. When querying the sub-departments of this node, use this value as parentDepartmentId.
        self.id = id
        # The name of the department returned by the identity provider.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exists is not None:
            result['exists'] = self.exists

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exists') is not None:
            self.exists = m.get('exists')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

