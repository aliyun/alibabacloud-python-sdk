# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterCreateUserRequest(DaraModel):
    def __init__(
        self,
        department_roles: List[main_models.DepartmentRoleCmd] = None,
        login_name: str = None,
        name: str = None,
        phone: str = None,
    ):
        # The department roles to assign to the user during creation. This parameter is optional.
        self.department_roles = department_roles
        # The logon name. This parameter is required. The logon name can be the same as the phone number.
        # 
        # This parameter is required.
        self.login_name = login_name
        # The name. This parameter is required. The value must be 2 to 20 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The phone number. This parameter is required.
        self.phone = phone

    def validate(self):
        if self.department_roles:
            for v1 in self.department_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['departmentRoles'] = []
        if self.department_roles is not None:
            for k1 in self.department_roles:
                result['departmentRoles'].append(k1.to_map() if k1 else None)

        if self.login_name is not None:
            result['loginName'] = self.login_name

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.department_roles = []
        if m.get('departmentRoles') is not None:
            for k1 in m.get('departmentRoles'):
                temp_model = main_models.DepartmentRoleCmd()
                self.department_roles.append(temp_model.from_map(k1))

        if m.get('loginName') is not None:
            self.login_name = m.get('loginName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        return self

