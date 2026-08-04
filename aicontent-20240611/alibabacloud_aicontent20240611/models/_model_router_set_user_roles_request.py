# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterSetUserRolesRequest(DaraModel):
    def __init__(
        self,
        department_roles: List[main_models.DepartmentRoleCmd] = None,
    ):
        # The department role list (required, full overwrite).
        self.department_roles = department_roles

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.department_roles = []
        if m.get('departmentRoles') is not None:
            for k1 in m.get('departmentRoles'):
                temp_model = main_models.DepartmentRoleCmd()
                self.department_roles.append(temp_model.from_map(k1))

        return self

