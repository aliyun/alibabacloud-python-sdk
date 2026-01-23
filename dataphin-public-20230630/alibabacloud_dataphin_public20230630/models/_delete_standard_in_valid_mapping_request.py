# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteStandardInValidMappingRequest(DaraModel):
    def __init__(
        self,
        delete_command: main_models.DeleteStandardInValidMappingRequestDeleteCommand = None,
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
            temp_model = main_models.DeleteStandardInValidMappingRequestDeleteCommand()
            self.delete_command = temp_model.from_map(m.get('DeleteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteStandardInValidMappingRequestDeleteCommand(DaraModel):
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

