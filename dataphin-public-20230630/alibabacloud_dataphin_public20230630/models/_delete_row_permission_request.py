# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteRowPermissionRequest(DaraModel):
    def __init__(
        self,
        delete_row_permission_command: main_models.DeleteRowPermissionRequestDeleteRowPermissionCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_row_permission_command = delete_row_permission_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.delete_row_permission_command:
            self.delete_row_permission_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_row_permission_command is not None:
            result['DeleteRowPermissionCommand'] = self.delete_row_permission_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteRowPermissionCommand') is not None:
            temp_model = main_models.DeleteRowPermissionRequestDeleteRowPermissionCommand()
            self.delete_row_permission_command = temp_model.from_map(m.get('DeleteRowPermissionCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteRowPermissionRequestDeleteRowPermissionCommand(DaraModel):
    def __init__(
        self,
        row_permission_id: int = None,
    ):
        # This parameter is required.
        self.row_permission_id = row_permission_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row_permission_id is not None:
            result['RowPermissionId'] = self.row_permission_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RowPermissionId') is not None:
            self.row_permission_id = m.get('RowPermissionId')

        return self

