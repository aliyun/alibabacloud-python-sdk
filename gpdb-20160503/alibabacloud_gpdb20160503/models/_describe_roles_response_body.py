# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeRolesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        role_list: main_models.DescribeRolesResponseBodyRoleList = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The roles.
        self.role_list = role_list

    def validate(self):
        if self.role_list:
            self.role_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_list is not None:
            result['RoleList'] = self.role_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleList') is not None:
            temp_model = main_models.DescribeRolesResponseBodyRoleList()
            self.role_list = temp_model.from_map(m.get('RoleList'))

        return self

class DescribeRolesResponseBodyRoleList(DaraModel):
    def __init__(
        self,
        role: List[str] = None,
    ):
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

