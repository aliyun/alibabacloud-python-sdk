# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateProjectMemberRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        op_tenant_id: int = None,
        update_command: main_models.UpdateProjectMemberRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateProjectMemberRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateProjectMemberRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        env: str = None,
        user_list: List[main_models.UpdateProjectMemberRequestUpdateCommandUserList] = None,
    ):
        # This parameter is required.
        self.env = env
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
        if self.env is not None:
            result['Env'] = self.env

        result['UserList'] = []
        if self.user_list is not None:
            for k1 in self.user_list:
                result['UserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        self.user_list = []
        if m.get('UserList') is not None:
            for k1 in m.get('UserList'):
                temp_model = main_models.UpdateProjectMemberRequestUpdateCommandUserList()
                self.user_list.append(temp_model.from_map(k1))

        return self

class UpdateProjectMemberRequestUpdateCommandUserList(DaraModel):
    def __init__(
        self,
        role_list: List[int] = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.role_list = role_list
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_list is not None:
            result['RoleList'] = self.role_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

