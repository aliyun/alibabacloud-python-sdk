# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateStandardWordRootRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateStandardWordRootRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateStandardWordRootRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateStandardWordRootRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        description: str = None,
        full_name: str = None,
        name: str = None,
        old_name: str = None,
    ):
        # This parameter is required.
        self.abbreviation = abbreviation
        self.description = description
        # This parameter is required.
        self.full_name = full_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.old_name = old_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        if self.description is not None:
            result['Description'] = self.description

        if self.full_name is not None:
            result['FullName'] = self.full_name

        if self.name is not None:
            result['Name'] = self.name

        if self.old_name is not None:
            result['OldName'] = self.old_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OldName') is not None:
            self.old_name = m.get('OldName')

        return self

