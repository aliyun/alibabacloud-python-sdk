# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordDetailRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        record_detail_command: main_models.GetOperationRecordDetailRequestRecordDetailCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The query command.
        # 
        # This parameter is required.
        self.record_detail_command = record_detail_command

    def validate(self):
        if self.record_detail_command:
            self.record_detail_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.record_detail_command is not None:
            result['RecordDetailCommand'] = self.record_detail_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('RecordDetailCommand') is not None:
            temp_model = main_models.GetOperationRecordDetailRequestRecordDetailCommand()
            self.record_detail_command = temp_model.from_map(m.get('RecordDetailCommand'))

        return self

class GetOperationRecordDetailRequestRecordDetailCommand(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        project_id: int = None,
    ):
        # The operation record ID.
        # 
        # This parameter is required.
        self.operation_id = operation_id
        # The project ID.
        # 
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

