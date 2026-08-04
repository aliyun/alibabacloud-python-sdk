# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class UserListItemDTO(DaraModel):
    def __init__(
        self,
        departments: List[main_models.UserDepartmentDTO] = None,
        gmt_create: str = None,
        id: int = None,
        login_name: str = None,
        name: str = None,
        phone: str = None,
    ):
        self.departments = departments
        self.gmt_create = gmt_create
        self.id = id
        self.login_name = login_name
        self.name = name
        self.phone = phone

    def validate(self):
        if self.departments:
            for v1 in self.departments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['departments'] = []
        if self.departments is not None:
            for k1 in self.departments:
                result['departments'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.login_name is not None:
            result['loginName'] = self.login_name

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.departments = []
        if m.get('departments') is not None:
            for k1 in m.get('departments'):
                temp_model = main_models.UserDepartmentDTO()
                self.departments.append(temp_model.from_map(k1))

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

