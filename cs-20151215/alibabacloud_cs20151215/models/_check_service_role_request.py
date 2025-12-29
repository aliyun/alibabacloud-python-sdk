# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CheckServiceRoleRequest(DaraModel):
    def __init__(
        self,
        roles: List[main_models.CheckServiceRoleRequestRoles] = None,
    ):
        # The list of service roles you want to check.
        # 
        # This parameter is required.
        self.roles = roles

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['roles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k1 in m.get('roles'):
                temp_model = main_models.CheckServiceRoleRequestRoles()
                self.roles.append(temp_model.from_map(k1))

        return self

class CheckServiceRoleRequestRoles(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The server role name. For more information about the service roles and their permissions in ACK, see [ACK roles](https://help.aliyun.com/document_detail/86483.html).
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

