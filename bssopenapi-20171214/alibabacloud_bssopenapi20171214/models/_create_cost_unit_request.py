# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class CreateCostUnitRequest(DaraModel):
    def __init__(
        self,
        unit_entity_list: List[main_models.CreateCostUnitRequestUnitEntityList] = None,
    ):
        # The list of cost centers.
        self.unit_entity_list = unit_entity_list

    def validate(self):
        if self.unit_entity_list:
            for v1 in self.unit_entity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k1 in self.unit_entity_list:
                result['UnitEntityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.unit_entity_list = []
        if m.get('UnitEntityList') is not None:
            for k1 in m.get('UnitEntityList'):
                temp_model = main_models.CreateCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k1))

        return self

class CreateCostUnitRequestUnitEntityList(DaraModel):
    def __init__(
        self,
        owner_uid: int = None,
        parent_unit_id: int = None,
        unit_name: str = None,
    ):
        # The user ID of the owner of the cost center.
        # 
        # This parameter is required.
        self.owner_uid = owner_uid
        # The ID of the parent cost center. A value of -1 indicates the root cost center.
        # 
        # This parameter is required.
        self.parent_unit_id = parent_unit_id
        # The name of the cost center.
        # 
        # This parameter is required.
        self.unit_name = unit_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id

        if self.unit_name is not None:
            result['UnitName'] = self.unit_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')

        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')

        return self

