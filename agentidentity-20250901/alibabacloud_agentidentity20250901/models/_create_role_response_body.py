# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class CreateRoleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role: main_models.CreateRoleResponseBodyRole = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The role information.
        self.role = role

    def validate(self):
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role is not None:
            result['Role'] = self.role.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Role') is not None:
            temp_model = main_models.CreateRoleResponseBodyRole()
            self.role = temp_model.from_map(m.get('Role'))

        return self

class CreateRoleResponseBodyRole(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        role_id: str = None,
        role_name: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The time when the role was created. The time is displayed in ISO 8601 format (UTC).
        self.create_time = create_time
        # The description of the role.
        self.description = description
        # The ID of the role.
        self.role_id = role_id
        # The name of the role.
        self.role_name = role_name
        # The type of the role. Valid values:
        # - Default: the default role that is automatically provisioned when the user pool is created
        # - Manual: a custom role that is manually created by calling an API operation
        self.type = type
        # The time when the role was updated. The time is displayed in ISO 8601 format (UTC).
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

