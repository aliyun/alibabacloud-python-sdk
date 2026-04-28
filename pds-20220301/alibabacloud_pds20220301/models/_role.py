# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class Role(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        manage_resource_type: str = None,
        name: str = None,
        permissions: List[main_models.Permission] = None,
        role_id: str = None,
        status: str = None,
        updated_at: int = None,
    ):
        # The time when the role was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The ID of the user who created the role.
        self.creator = creator
        # The description of the role.
        self.description = description
        # The type of the resource on which the role has permissions. Valid value: RT_File.
        self.manage_resource_type = manage_resource_type
        # The name of the role.
        self.name = name
        # The permissions.
        self.permissions = permissions
        # The ID of the role.
        self.role_id = role_id
        # The status of the role.
        self.status = status
        # The time when the role was modified. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_at = updated_at

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type

        if self.name is not None:
            result['name'] = self.name

        result['permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['permissions'].append(k1.to_map() if k1 else None)

        if self.role_id is not None:
            result['role_id'] = self.role_id

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updated_at'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.permissions = []
        if m.get('permissions') is not None:
            for k1 in m.get('permissions'):
                temp_model = main_models.Permission()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

