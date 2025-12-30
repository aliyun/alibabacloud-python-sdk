# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateTenantMemberRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateTenantMemberRequestUpdateCommand = None,
    ):
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
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateTenantMemberRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateTenantMemberRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        member_list: List[main_models.UpdateTenantMemberRequestUpdateCommandMemberList] = None,
    ):
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.UpdateTenantMemberRequestUpdateCommandMemberList()
                self.member_list.append(temp_model.from_map(k1))

        return self

class UpdateTenantMemberRequestUpdateCommandMemberList(DaraModel):
    def __init__(
        self,
        ding_number: str = None,
        mail: str = None,
        mobile_phone: str = None,
        role_list: List[str] = None,
        user_id: str = None,
    ):
        self.ding_number = ding_number
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.role_list = role_list
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.role_list is not None:
            result['RoleList'] = self.role_list

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('RoleList') is not None:
            self.role_list = m.get('RoleList')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

