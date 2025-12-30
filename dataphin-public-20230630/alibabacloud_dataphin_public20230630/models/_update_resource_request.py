# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateResourceRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateResourceRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateResourceRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        compute_engine_type: str = None,
        description: str = None,
        id: int = None,
        name: str = None,
        project_id: int = None,
        storage_address: str = None,
    ):
        # This parameter is required.
        self.comment = comment
        # This parameter is required.
        self.compute_engine_type = compute_engine_type
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.storage_address = storage_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.compute_engine_type is not None:
            result['ComputeEngineType'] = self.compute_engine_type

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.storage_address is not None:
            result['StorageAddress'] = self.storage_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ComputeEngineType') is not None:
            self.compute_engine_type = m.get('ComputeEngineType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('StorageAddress') is not None:
            self.storage_address = m.get('StorageAddress')

        return self

