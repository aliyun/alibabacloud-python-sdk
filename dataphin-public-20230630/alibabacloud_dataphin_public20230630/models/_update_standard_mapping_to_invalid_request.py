# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateStandardMappingToInvalidRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateStandardMappingToInvalidRequestUpdateCommand = None,
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
            temp_model = main_models.UpdateStandardMappingToInvalidRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateStandardMappingToInvalidRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        belong_guid_list: List[str] = None,
        guid_list: List[str] = None,
        standard_id: int = None,
    ):
        self.belong_guid_list = belong_guid_list
        self.guid_list = guid_list
        # This parameter is required.
        self.standard_id = standard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belong_guid_list is not None:
            result['BelongGuidList'] = self.belong_guid_list

        if self.guid_list is not None:
            result['GuidList'] = self.guid_list

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongGuidList') is not None:
            self.belong_guid_list = m.get('BelongGuidList')

        if m.get('GuidList') is not None:
            self.guid_list = m.get('GuidList')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        return self

