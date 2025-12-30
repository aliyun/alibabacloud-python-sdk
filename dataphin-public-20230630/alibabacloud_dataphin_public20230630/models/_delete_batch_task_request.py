# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteBatchTaskRequest(DaraModel):
    def __init__(
        self,
        delete_command: main_models.DeleteBatchTaskRequestDeleteCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_command = delete_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.delete_command:
            self.delete_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_command is not None:
            result['DeleteCommand'] = self.delete_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteCommand') is not None:
            temp_model = main_models.DeleteBatchTaskRequestDeleteCommand()
            self.delete_command = temp_model.from_map(m.get('DeleteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteBatchTaskRequestDeleteCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        file_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

