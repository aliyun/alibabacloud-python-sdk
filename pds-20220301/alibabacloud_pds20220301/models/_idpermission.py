# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class IDPermission(DaraModel):
    def __init__(
        self,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        permission: main_models.Permission = None,
        roles: List[str] = None,
    ):
        self.disinherit_sub_group = disinherit_sub_group
        self.expire_time = expire_time
        self.permission = permission
        self.roles = roles

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.permission is not None:
            result['permission'] = self.permission.to_map()

        if self.roles is not None:
            result['roles'] = self.roles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('permission') is not None:
            temp_model = main_models.Permission()
            self.permission = temp_model.from_map(m.get('permission'))

        if m.get('roles') is not None:
            self.roles = m.get('roles')

        return self

