# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordByIdRequest(DaraModel):
    def __init__(
        self,
        detail_command: main_models.GetOperationRecordByIdRequestDetailCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.detail_command = detail_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.detail_command:
            self.detail_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail_command is not None:
            result['DetailCommand'] = self.detail_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailCommand') is not None:
            temp_model = main_models.GetOperationRecordByIdRequestDetailCommand()
            self.detail_command = temp_model.from_map(m.get('DetailCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetOperationRecordByIdRequestDetailCommand(DaraModel):
    def __init__(
        self,
        operation_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.operation_id = operation_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

