# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDataServiceAppMemberRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateDataServiceAppMemberRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateDataServiceAppMemberRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDataServiceAppMemberRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        member_list: List[main_models.UpdateDataServiceAppMemberRequestUpdateCommandMemberList] = None,
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
                temp_model = main_models.UpdateDataServiceAppMemberRequestUpdateCommandMemberList()
                self.member_list.append(temp_model.from_map(k1))

        return self

class UpdateDataServiceAppMemberRequestUpdateCommandMemberList(DaraModel):
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

