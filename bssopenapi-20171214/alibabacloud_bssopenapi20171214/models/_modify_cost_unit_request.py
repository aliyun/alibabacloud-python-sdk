# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class ModifyCostUnitRequest(DaraModel):
    def __init__(
        self,
        unit_entity_list: List[main_models.ModifyCostUnitRequestUnitEntityList] = None,
    ):
        # The cost centers to be modified.
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
                temp_model = main_models.ModifyCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k1))

        return self

class ModifyCostUnitRequestUnitEntityList(DaraModel):
    def __init__(
        self,
        new_unit_name: str = None,
        owner_uid: int = None,
        unit_id: int = None,
    ):
        # The new name of the cost center.
        # 
        # This parameter is required.
        self.new_unit_name = new_unit_name
        # The user ID of the cost center owner.
        # 
        # This parameter is required.
        self.owner_uid = owner_uid
        # The ID of the cost center.
        # 
        # This parameter is required.
        self.unit_id = unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_unit_name is not None:
            result['NewUnitName'] = self.new_unit_name

        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid

        if self.unit_id is not None:
            result['UnitId'] = self.unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewUnitName') is not None:
            self.new_unit_name = m.get('NewUnitName')

        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')

        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')

        return self

