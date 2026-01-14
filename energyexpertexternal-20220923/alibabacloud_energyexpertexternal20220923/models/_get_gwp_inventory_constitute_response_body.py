# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetGwpInventoryConstituteResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGwpInventoryConstituteResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetGwpInventoryConstituteResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGwpInventoryConstituteResponseBodyData(DaraModel):
    def __init__(
        self,
        by_resource_type: List[main_models.GwpInventoryConstitute] = None,
        carbon_emission: float = None,
        items: List[main_models.GwpInventoryConstitute] = None,
        name: str = None,
        unit: str = None,
    ):
        # Aggregated by resource type of an inventory.
        self.by_resource_type = by_resource_type
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission
        # Organized by hierarchy from high to low, according to the flow-> process-> inventory hierarchy.
        self.items = items
        # The name.
        self.name = name
        # Emission Unit.
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

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.by_resource_type = []
        if m.get('byResourceType') is not None:
            for k1 in m.get('byResourceType'):
                temp_model = main_models.GwpInventoryConstitute()
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

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

