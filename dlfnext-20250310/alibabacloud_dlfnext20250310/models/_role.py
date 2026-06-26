# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Role(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        description: str = None,
        display_name: str = None,
        is_predefined: str = None,
        role_name: str = None,
        role_principal: str = None,
        updated_at: int = None,
        updated_by: str = None,
        users: List[main_models.User] = None,
    ):
        # The time when the role was created. This is a Unix timestamp in milliseconds.
        self.created_at = created_at
        # The name of the user who created the role.
        self.created_by = created_by
        # The role description.
        self.description = description
        # The display name of the role.
        self.display_name = display_name
        # Indicates whether the role is a system role.
        self.is_predefined = is_predefined
        # The name of the role.
        self.role_name = role_name
        # The resource descriptor of the role.
        self.role_principal = role_principal
        # The time when the role was last updated. This is a Unix timestamp in milliseconds.
        self.updated_at = updated_at
        # The name of the user who last updated the role.
        self.updated_by = updated_by
        # The users for the role.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_predefined is not None:
            result['isPredefined'] = self.is_predefined

        if self.role_name is not None:
            result['roleName'] = self.role_name

        if self.role_principal is not None:
            result['rolePrincipal'] = self.role_principal

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        result['users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isPredefined') is not None:
            self.is_predefined = m.get('isPredefined')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        if m.get('rolePrincipal') is not None:
            self.role_principal = m.get('rolePrincipal')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        self.users = []
        if m.get('users') is not None:
            for k1 in m.get('users'):
                temp_model = main_models.User()
                self.users.append(temp_model.from_map(k1))

        return self

