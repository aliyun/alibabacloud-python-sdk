# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class RemoveDataServiceAppMemberRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command: main_models.RemoveDataServiceAppMemberRequestRemoveCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.remove_command = remove_command

    def validate(self):
        if self.remove_command:
            self.remove_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.remove_command is not None:
            result['RemoveCommand'] = self.remove_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RemoveCommand') is not None:
            temp_model = main_models.RemoveDataServiceAppMemberRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m.get('RemoveCommand'))

        return self

class RemoveDataServiceAppMemberRequestRemoveCommand(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        member_ids: List[str] = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.member_ids = member_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.member_ids is not None:
            result['MemberIds'] = self.member_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('MemberIds') is not None:
            self.member_ids = m.get('MemberIds')

        return self

