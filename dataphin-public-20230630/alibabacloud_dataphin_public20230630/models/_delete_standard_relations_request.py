# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteStandardRelationsRequest(DaraModel):
    def __init__(
        self,
        delete_command: main_models.DeleteStandardRelationsRequestDeleteCommand = None,
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
            temp_model = main_models.DeleteStandardRelationsRequestDeleteCommand()
            self.delete_command = temp_model.from_map(m.get('DeleteCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteStandardRelationsRequestDeleteCommand(DaraModel):
    def __init__(
        self,
        relation_type: str = None,
        standard_id: int = None,
        standard_ref_list: List[main_models.DeleteStandardRelationsRequestDeleteCommandStandardRefList] = None,
    ):
        # This parameter is required.
        self.relation_type = relation_type
        # This parameter is required.
        self.standard_id = standard_id
        # This parameter is required.
        self.standard_ref_list = standard_ref_list

    def validate(self):
        if self.standard_ref_list:
            for v1 in self.standard_ref_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        result['StandardRefList'] = []
        if self.standard_ref_list is not None:
            for k1 in self.standard_ref_list:
                result['StandardRefList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        self.standard_ref_list = []
        if m.get('StandardRefList') is not None:
            for k1 in m.get('StandardRefList'):
                temp_model = main_models.DeleteStandardRelationsRequestDeleteCommandStandardRefList()
                self.standard_ref_list.append(temp_model.from_map(k1))

        return self

class DeleteStandardRelationsRequestDeleteCommandStandardRefList(DaraModel):
    def __init__(
        self,
        standard_id: int = None,
    ):
        # This parameter is required.
        self.standard_id = standard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        return self

