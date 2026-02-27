# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddDataServiceAppMemberRequest(DaraModel):
    def __init__(
        self,
        add_command: main_models.AddDataServiceAppMemberRequestAddCommand = None,
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
            temp_model = main_models.AddDataServiceAppMemberRequestAddCommand()
            self.add_command = temp_model.from_map(m.get('AddCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AddDataServiceAppMemberRequestAddCommand(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        member_list: List[main_models.AddDataServiceAppMemberRequestAddCommandMemberList] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.AddDataServiceAppMemberRequestAddCommandMemberList()
                self.member_list.append(temp_model.from_map(k1))

        return self



class AddDataServiceAppMemberRequestAddCommandMemberList(DaraModel):
    def __init__(
        self,
        effective_end: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.effective_end = effective_end
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_end is not None:
            result['EffectiveEnd'] = self.effective_end

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveEnd') is not None:
            self.effective_end = m.get('EffectiveEnd')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

