# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteSecurityClassifyCatalogRequest(DaraModel):
    def __init__(
        self,
        delete_command: main_models.DeleteSecurityClassifyCatalogRequestDeleteCommand = None,
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
            temp_model = main_models.DeleteSecurityClassifyCatalogRequestDeleteCommand()
            self.delete_command = temp_model.from_map(m.get('DeleteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteSecurityClassifyCatalogRequestDeleteCommand(DaraModel):
    def __init__(
        self,
        path: str = None,
        return_removed_details: bool = None,
    ):
        # This parameter is required.
        self.path = path
        self.return_removed_details = return_removed_details

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.return_removed_details is not None:
            result['ReturnRemovedDetails'] = self.return_removed_details

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ReturnRemovedDetails') is not None:
            self.return_removed_details = m.get('ReturnRemovedDetails')

        return self

