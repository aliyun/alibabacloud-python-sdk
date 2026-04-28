# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseGroupResponse(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        is_sync: bool = None,
        permission: Dict[str, main_models.IDPermission] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.group_id = group_id
        self.group_name = group_name
        self.is_sync = is_sync
        self.permission = permission
        self.updated_at = updated_at

    def validate(self):
        if self.permission:
            for v1 in self.permission.values():
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

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.group_name is not None:
            result['group_name'] = self.group_name

        if self.is_sync is not None:
            result['is_sync'] = self.is_sync

        result['permission'] = {}
        if self.permission is not None:
            for k1, v1 in self.permission.items():
                result['permission'][k1] = v1.to_map() if v1 else None

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

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        if m.get('is_sync') is not None:
            self.is_sync = m.get('is_sync')

        self.permission = {}
        if m.get('permission') is not None:
            for k1, v1 in m.get('permission').items():
                temp_model = main_models.IDPermission()
                self.permission[k1] = temp_model.from_map(v1)

        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')

        return self

