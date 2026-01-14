# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class EpdInventoryConstituteItem(DaraModel):
    def __init__(
        self,
        carbon_emission: float = None,
        factor: str = None,
        factor_dataset: str = None,
        factor_id: str = None,
        factor_type: int = None,
        factor_unit: str = None,
        inventory_id: int = None,
        inventory_unit: str = None,
        inventory_value: float = None,
        inventory_value_per_product: float = None,
        inventory_value_per_product_unit: str = None,
        items: List[main_models.EpdInventoryConstituteItem] = None,
        name: str = None,
        num: int = None,
        percent: float = None,
        quantity: float = None,
        resource_type: str = None,
        state: int = None,
        unit: str = None,
    ):
        self.carbon_emission = carbon_emission
        self.factor = factor
        self.factor_dataset = factor_dataset
        self.factor_id = factor_id
        self.factor_type = factor_type
        self.factor_unit = factor_unit
        self.inventory_id = inventory_id
        self.inventory_unit = inventory_unit
        self.inventory_value = inventory_value
        self.inventory_value_per_product = inventory_value_per_product
        self.inventory_value_per_product_unit = inventory_value_per_product_unit
        self.items = items
        self.name = name
        self.num = num
        self.percent = percent
        self.quantity = quantity
        self.resource_type = resource_type
        self.state = state
        self.unit = unit

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        if self.factor is not None:
            result['factor'] = self.factor

        if self.factor_dataset is not None:
            result['factorDataset'] = self.factor_dataset

        if self.factor_id is not None:
            result['factorId'] = self.factor_id

        if self.factor_type is not None:
            result['factorType'] = self.factor_type

        if self.factor_unit is not None:
            result['factorUnit'] = self.factor_unit

        if self.inventory_id is not None:
            result['inventoryId'] = self.inventory_id

        if self.inventory_unit is not None:
            result['inventoryUnit'] = self.inventory_unit

        if self.inventory_value is not None:
            result['inventoryValue'] = self.inventory_value

        if self.inventory_value_per_product is not None:
            result['inventoryValuePerProduct'] = self.inventory_value_per_product

        if self.inventory_value_per_product_unit is not None:
            result['inventoryValuePerProductUnit'] = self.inventory_value_per_product_unit

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.num is not None:
            result['num'] = self.num

        if self.percent is not None:
            result['percent'] = self.percent

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.state is not None:
            result['state'] = self.state

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        if m.get('factor') is not None:
            self.factor = m.get('factor')

        if m.get('factorDataset') is not None:
            self.factor_dataset = m.get('factorDataset')

        if m.get('factorId') is not None:
            self.factor_id = m.get('factorId')

        if m.get('factorType') is not None:
            self.factor_type = m.get('factorType')

        if m.get('factorUnit') is not None:
            self.factor_unit = m.get('factorUnit')

        if m.get('inventoryId') is not None:
            self.inventory_id = m.get('inventoryId')

        if m.get('inventoryUnit') is not None:
            self.inventory_unit = m.get('inventoryUnit')

        if m.get('inventoryValue') is not None:
            self.inventory_value = m.get('inventoryValue')

        if m.get('inventoryValuePerProduct') is not None:
            self.inventory_value_per_product = m.get('inventoryValuePerProduct')

        if m.get('inventoryValuePerProductUnit') is not None:
            self.inventory_value_per_product_unit = m.get('inventoryValuePerProductUnit')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.EpdInventoryConstituteItem()
                self.items.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('num') is not None:
            self.num = m.get('num')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

