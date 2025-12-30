# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddTenantMembersBySourceUserRequest(DaraModel):
    def __init__(
        self,
        add_command: main_models.AddTenantMembersBySourceUserRequestAddCommand = None,
        op_tenant_id: int = None,
    ):
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
            temp_model = main_models.AddTenantMembersBySourceUserRequestAddCommand()
            self.add_command = temp_model.from_map(m.get('AddCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AddTenantMembersBySourceUserRequestAddCommand(DaraModel):
    def __init__(
        self,
        source_user_list: List[main_models.AddTenantMembersBySourceUserRequestAddCommandSourceUserList] = None,
    ):
        self.source_user_list = source_user_list

    def validate(self):
        if self.source_user_list:
            for v1 in self.source_user_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SourceUserList'] = []
        if self.source_user_list is not None:
            for k1 in self.source_user_list:
                result['SourceUserList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_user_list = []
        if m.get('SourceUserList') is not None:
            for k1 in m.get('SourceUserList'):
                temp_model = main_models.AddTenantMembersBySourceUserRequestAddCommandSourceUserList()
                self.source_user_list.append(temp_model.from_map(k1))

        return self

class AddTenantMembersBySourceUserRequestAddCommandSourceUserList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        ding_number: str = None,
        display_name: str = None,
        mail: str = None,
        mobile_phone: str = None,
        source_id: str = None,
    ):
        self.account_name = account_name
        self.ding_number = ding_number
        self.display_name = display_name
        self.mail = mail
        self.mobile_phone = mobile_phone
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.ding_number is not None:
            result['DingNumber'] = self.ding_number

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.mail is not None:
            result['Mail'] = self.mail

        if self.mobile_phone is not None:
            result['MobilePhone'] = self.mobile_phone

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DingNumber') is not None:
            self.ding_number = m.get('DingNumber')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Mail') is not None:
            self.mail = m.get('Mail')

        if m.get('MobilePhone') is not None:
            self.mobile_phone = m.get('MobilePhone')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

