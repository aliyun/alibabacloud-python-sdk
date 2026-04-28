# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CancelAssignRoleRequest(DaraModel):
    def __init__(
        self,
        identity: main_models.Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
    ):
        # The unique identifier. You can cancel only the role assigned to a user.
        # 
        # This parameter is required.
        self.identity = identity
        # The ID of the resource that the role manages. Set the value to a group ID.
        # 
        # This parameter is required.
        self.manage_resource_id = manage_resource_id
        # The type of the resource that the role manages. Set the value to RT_Group, which specifies group.
        # 
        # This parameter is required.
        self.manage_resource_type = manage_resource_type
        # The ID of the role to be canceled. Set the value to SystemGroupAdmin, which is the ID of the group administrator role.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id

        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')

        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

