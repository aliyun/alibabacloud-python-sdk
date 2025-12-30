# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class OnlineBizEntityRequest(DaraModel):
    def __init__(
        self,
        online_command: main_models.OnlineBizEntityRequestOnlineCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.online_command = online_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.online_command:
            self.online_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.online_command is not None:
            result['OnlineCommand'] = self.online_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCommand') is not None:
            temp_model = main_models.OnlineBizEntityRequestOnlineCommand()
            self.online_command = temp_model.from_map(m.get('OnlineCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class OnlineBizEntityRequestOnlineCommand(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        comment: str = None,
        id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.biz_unit_id = biz_unit_id
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

