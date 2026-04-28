# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class BaseFileUserPermissionResponse(DaraModel):
    def __init__(
        self,
        can_access: bool = None,
        created_at: int = None,
        creator: str = None,
        disinherit_sub_group: bool = None,
        domain_id: str = None,
        drive_id: str = None,
        expire_time: int = None,
        file_full_path: str = None,
        file_id: str = None,
        identity: main_models.Identity = None,
        role_id: str = None,
    ):
        self.can_access = can_access
        self.created_at = created_at
        self.creator = creator
        self.disinherit_sub_group = disinherit_sub_group
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.expire_time = expire_time
        self.file_full_path = file_full_path
        self.file_id = file_id
        self.identity = identity
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_access is not None:
            result['can_access'] = self.can_access

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.file_full_path is not None:
            result['file_full_path'] = self.file_full_path

        if self.file_id is not None:
            result['file_id'] = self.file_id

        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_access') is not None:
            self.can_access = m.get('can_access')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('file_full_path') is not None:
            self.file_full_path = m.get('file_full_path')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

