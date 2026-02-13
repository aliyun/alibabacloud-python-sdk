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
        # Emissions are presented with 24 decimal places. It\\"s advisable to utilize the truncated version. These emissions encompass all tiers: At the first level, they reflect the product\\"s total emissions under the current environmental impact; at the second level, they show the process\\"s total emissions; and at the third level, they represent the inventory\\"s emissions within the same environmental impact context.
        self.carbon_emission = carbon_emission
        # The value of the factor. Only the third level is not empty. The factor in the inventory information indicates the factor value of the selected factor. The factor value is kept to four decimal places after the decimal point, and "1.0000" indicates that the factor value is 1. The factor value should be used in combination with factorUnit. If factorUnit is "kg CO2-Eq mg/kg", it means that the carbon emission per 1kg of the list is 1kg CO2-Eq.
        self.factor = factor
        # The database to which the factorDataset factor belongs. This field is used in conjunction with factorType. If factorType is 1, the data name of the factor is displayed. If factorType is 2,factorId indicates the ID of the referenced product. If factorType is null,factorId is meaningless. This field is a new field. Old data may not have data in this field and is displayed as "/".
        self.factor_dataset = factor_dataset
        # The id of the factor.
        self.factor_id = factor_id
        # The key of the factor type. Only the third level is not empty. The factorType in the inventory information indicates that the factor source type is selected; the optional values are 1, 2, or null:1: factor library, 2: product library. null indicates that the factor is not selected from the factor library or product library, and the factor is constructed by the user.
        self.factor_type = factor_type
        # Factor Unit
        self.factor_unit = factor_unit
        # manifest id
        self.inventory_id = inventory_id
        # Inventory Unit
        self.inventory_unit = inventory_unit
        # The quantity of the inventory. It is not empty only at the third level. The third level is the inventory details. This field indicates the id of the inventory. It should be used in conjunction with the InventoryUnit.
        self.inventory_value = inventory_value
        # Activity data per functional unit: only the third level is not empty; the value retains 24 decimal places, indicating the number of activities per functional unit; should be used in conjunction with the inventoryValuePerProductUnit.
        self.inventory_value_per_product = inventory_value_per_product
        # Unit of activity data per functional unit. Only the third level is not empty. in the inventory information indicates the unit of activity data per functional unit.
        self.inventory_value_per_product_unit = inventory_value_per_product_unit
        # List of children
        self.items = items
        # Returns the name of the current level. The names of different levels have different meanings. The first level returns the environmental impact type. The second level returns the current process name. The third level returns the current inventory name
        self.name = name
        # Category key, please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.num = num
        # The percentage. Four decimal places are retained and 31.4000 is returned to indicate the percentage 31.4%. The first level returns null; The second level returns the current process as a percentage of total emissions; the third level returns the current inventory as a percentage of total emissions.
        self.percent = percent
        # Raw activity data. Only the third level returns a quantity that is not null, indicating a manifest.
        self.quantity = quantity
        # The type of the inventory. Only the third level returns non-null, and the third level is the inventory details. This field indicates the resource type name of the inventory. You may refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.resource_type = resource_type
        # The data status. 1 indicates accurate calculation, 2 indicates default data, 3 indicates missing factor, and 0 value is used in other cases.
        self.state = state
        # The unit of environmental impact result value. This unit is the unit of the environmental impact result value of the corresponding environmental impact category. For example, the unit kg CO2-Eq represent the emission values shown here is kg CO2-Eq.
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

