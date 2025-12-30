# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ApplyDataServiceAppRequest(DaraModel):
    def __init__(
        self,
        apply_command: main_models.ApplyDataServiceAppRequestApplyCommand = None,
        op_tenant_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.apply_command = apply_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.apply_command:
            self.apply_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_command is not None:
            result['ApplyCommand'] = self.apply_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyCommand') is not None:
            temp_model = main_models.ApplyDataServiceAppRequestApplyCommand()
            self.apply_command = temp_model.from_map(m.get('ApplyCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class ApplyDataServiceAppRequestApplyCommand(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        expire_date: str = None,
        reason: str = None,
    ):
        # appId
        # 
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.expire_date = expire_date
        # This parameter is required.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

