# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class RemoveTenantMemberRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        remove_command: main_models.RemoveTenantMemberRequestRemoveCommand = None,
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
            temp_model = main_models.RemoveTenantMemberRequestRemoveCommand()
            self.remove_command = temp_model.from_map(m.get('RemoveCommand'))

        return self

class RemoveTenantMemberRequestRemoveCommand(DaraModel):
    def __init__(
        self,
        source_id: str = None,
    ):
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

