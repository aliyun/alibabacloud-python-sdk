# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateKgRelationRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateKgRelationRequestUpdateCommand = None,
        workspace_id: str = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The update command.
        # 
        # This parameter is required.
        self.update_command = update_command
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateKgRelationRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateKgRelationRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        property_list: List[main_models.UpdateKgRelationRequestUpdateCommandPropertyList] = None,
        relation_id: str = None,
        relation_type: str = None,
    ):
        # The list of relationship record properties.
        self.property_list = property_list
        # The relationship record ID.
        # 
        # This parameter is required.
        self.relation_id = relation_id
        # The relationship type code.
        # 
        # This parameter is required.
        self.relation_type = relation_type

    def validate(self):
        if self.property_list:
            for v1 in self.property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PropertyList'] = []
        if self.property_list is not None:
            for k1 in self.property_list:
                result['PropertyList'].append(k1.to_map() if k1 else None)

        if self.relation_id is not None:
            result['RelationId'] = self.relation_id

        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k1 in m.get('PropertyList'):
                temp_model = main_models.UpdateKgRelationRequestUpdateCommandPropertyList()
                self.property_list.append(temp_model.from_map(k1))

        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')

        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        return self

class UpdateKgRelationRequestUpdateCommandPropertyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        # 
        # This parameter is required.
        self.code = code
        # The property value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

