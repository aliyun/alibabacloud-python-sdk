# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddDataServiceProjectMemberRequest(DaraModel):
    def __init__(
        self,
        add_command: main_models.AddDataServiceProjectMemberRequestAddCommand = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.add_command = add_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddCommand') is not None:
            temp_model = main_models.AddDataServiceProjectMemberRequestAddCommand()
            self.add_command = temp_model.from_map(m.get('AddCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class AddDataServiceProjectMemberRequestAddCommand(DaraModel):
    def __init__(
        self,
        project_member_list: List[main_models.AddDataServiceProjectMemberRequestAddCommandProjectMemberList] = None,
    ):
        # This parameter is required.
        self.project_member_list = project_member_list

    def validate(self):
        if self.project_member_list:
            for v1 in self.project_member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProjectMemberList'] = []
        if self.project_member_list is not None:
            for k1 in self.project_member_list:
                result['ProjectMemberList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.project_member_list = []
        if m.get('ProjectMemberList') is not None:
            for k1 in m.get('ProjectMemberList'):
                temp_model = main_models.AddDataServiceProjectMemberRequestAddCommandProjectMemberList()
                self.project_member_list.append(temp_model.from_map(k1))

        return self



class AddDataServiceProjectMemberRequestAddCommandProjectMemberList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        display_name: str = None,
        role: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.role is not None:
            result['Role'] = self.role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

