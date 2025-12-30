# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddUserGroupMemberRequest(DaraModel):
    def __init__(
        self,
        add_command: main_models.AddUserGroupMemberRequestAddCommand = None,
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
            temp_model = main_models.AddUserGroupMemberRequestAddCommand()
            self.add_command = temp_model.from_map(m.get('AddCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AddUserGroupMemberRequestAddCommand(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.user_group_id = user_group_id
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

