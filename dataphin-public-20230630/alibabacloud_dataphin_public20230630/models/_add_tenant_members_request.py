# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddTenantMembersRequest(DaraModel):
    def __init__(
        self,
        add_command: main_models.AddTenantMembersRequestAddCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.add_command = add_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.add_command:
            self.add_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_command is not None:
            result['AddCommand'] = self.add_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            temp_model = main_models.AddTenantMembersRequestAddCommand()
            self.add_command = temp_model.from_map(m.get('AddCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AddTenantMembersRequestAddCommand(DaraModel):
    def __init__(
        self,
        user_list: List[main_models.AddTenantMembersRequestAddCommandUserList] = None,
    ):
        # This parameter is required.
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for v1 in self.user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.AddTenantMembersRequestAddCommandUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class AddTenantMembersRequestAddCommandUserList(DaraModel):
    def __init__(
        self,
        id: str = None,
        role_list: List[str] = None,
    ):
        self.id = id
        self.role_list = role_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.role_list is not None:
            result['RoleList'] = self.role_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')

        return self

