# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDataDomainRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateDataDomainRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateDataDomainRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDataDomainRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        abbreviation: str = None,
        biz_unit_id: int = None,
        data_domain_id: int = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
        parent_id: int = None,
    ):
        # This parameter is required.
        self.abbreviation = abbreviation
        # This parameter is required.
        self.biz_unit_id = biz_unit_id
        # This parameter is required.
        self.data_domain_id = data_domain_id
        self.description = description
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abbreviation is not None:
            result['Abbreviation'] = self.abbreviation

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.data_domain_id is not None:
            result['DataDomainId'] = self.data_domain_id

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Abbreviation') is not None:
            self.abbreviation = m.get('Abbreviation')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('DataDomainId') is not None:
            self.data_domain_id = m.get('DataDomainId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

