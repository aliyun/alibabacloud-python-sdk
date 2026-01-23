# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateStandardMappingRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateStandardMappingRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_command = create_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateStandardMappingRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateStandardMappingRequestCreateCommand(DaraModel):
    def __init__(
        self,
        asset_guid_list: List[str] = None,
        invalid_mapping_relation_operation_type: str = None,
        relation_type: str = None,
        standard_id: int = None,
    ):
        # This parameter is required.
        self.asset_guid_list = asset_guid_list
        self.invalid_mapping_relation_operation_type = invalid_mapping_relation_operation_type
        self.relation_type = relation_type
        # This parameter is required.
        self.standard_id = standard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_guid_list is not None:
            result['AssetGuidList'] = self.asset_guid_list

        if self.invalid_mapping_relation_operation_type is not None:
            result['InvalidMappingRelationOperationType'] = self.invalid_mapping_relation_operation_type

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetGuidList') is not None:
            self.asset_guid_list = m.get('AssetGuidList')

        if m.get('InvalidMappingRelationOperationType') is not None:
            self.invalid_mapping_relation_operation_type = m.get('InvalidMappingRelationOperationType')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        return self

