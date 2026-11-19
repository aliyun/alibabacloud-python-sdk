# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountRolesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        roles: main_models.DescribeAccountRolesResponseBodyRoles = None,
    ):
        # The request ID.
        self.request_id = request_id
        self.roles = roles

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.roles is not None:
            result['Roles'] = self.roles.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Roles') is not None:
            temp_model = main_models.DescribeAccountRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m.get('Roles'))

        return self

class DescribeAccountRolesResponseBodyRoles(DaraModel):
    def __init__(
        self,
        role: List[main_models.DescribeAccountRolesResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for v1 in self.role:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Role'] = []
        if self.role is not None:
            for k1 in self.role:
                result['Role'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k1 in m.get('Role'):
                temp_model = main_models.DescribeAccountRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k1))

        return self

class DescribeAccountRolesResponseBodyRolesRole(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        role: str = None,
    ):
        self.dbname = dbname
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

