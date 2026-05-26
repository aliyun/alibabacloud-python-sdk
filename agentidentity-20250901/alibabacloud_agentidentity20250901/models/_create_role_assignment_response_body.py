# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class CreateRoleAssignmentResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role_assignment: main_models.CreateRoleAssignmentResponseBodyRoleAssignment = None,
    ):
        self.request_id = request_id
        self.role_assignment = role_assignment

    def validate(self):
        if self.role_assignment:
            self.role_assignment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_assignment is not None:
            result['RoleAssignment'] = self.role_assignment.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleAssignment') is not None:
            temp_model = main_models.CreateRoleAssignmentResponseBodyRoleAssignment()
            self.role_assignment = temp_model.from_map(m.get('RoleAssignment'))

        return self

class CreateRoleAssignmentResponseBodyRoleAssignment(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        principal_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
        role_id: str = None,
        role_name: str = None,
        user_pool_id: str = None,
    ):
        self.create_time = create_time
        self.principal_id = principal_id
        self.principal_name = principal_name
        self.principal_type = principal_type
        self.role_id = role_id
        self.role_name = role_name
        self.user_pool_id = user_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        return self

