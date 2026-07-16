# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetOperationRecordRunCodeRequest(DaraModel):
    def __init__(
        self,
        code_command: main_models.GetOperationRecordRunCodeRequestCodeCommand = None,
        op_tenant_id: int = None,
    ):
        # The query command.
        # 
        # This parameter is required.
        self.code_command = code_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.code_command:
            self.code_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_command is not None:
            result['CodeCommand'] = self.code_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeCommand') is not None:
            temp_model = main_models.GetOperationRecordRunCodeRequestCodeCommand()
            self.code_command = temp_model.from_map(m.get('CodeCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetOperationRecordRunCodeRequestCodeCommand(DaraModel):
    def __init__(
        self,
        operation_id: int = None,
        project_id: int = None,
    ):
        # The operation log ID.
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

