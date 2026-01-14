# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GwpInventoryConstitute(DaraModel):
    def __init__(
        self,
        by_resource_type: List[main_models.GwpResourceConstitute] = None,
        carbon_emission: float = None,
        items: List[main_models.GwpInventoryConstitute] = None,
        name: str = None,
        percent: float = None,
        resource_type: int = None,
        unit: str = None,
    ):
        self.by_resource_type = by_resource_type
        self.carbon_emission = carbon_emission
        self.items = items
        self.name = name
        self.percent = percent
        self.resource_type = resource_type
        self.unit = unit

    def validate(self):
        if self.by_resource_type:
            for v1 in self.by_resource_type:
                 if v1:
                    v1.validate()
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['byResourceType'] = []
        if self.by_resource_type is not None:
            for k1 in self.by_resource_type:
                result['byResourceType'].append(k1.to_map() if k1 else None)

        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.percent is not None:
            result['percent'] = self.percent

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k1 in m.get('byResourceType'):
                temp_model = main_models.GwpResourceConstitute()
                self.by_resource_type.append(temp_model.from_map(k1))

        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GwpInventoryConstitute()
                self.items.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

