# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetInventoryListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetInventoryListResponseBodyData = None,
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
            temp_model = main_models.GetInventoryListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetInventoryListResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetInventoryListResponseBodyDataItems] = None,
        product_unit: str = None,
        unit: str = None,
    ):
        # Inventory detail.
        self.items = items
        # Unit of product.
        self.product_unit = product_unit
        # Emission Unit: The default value is kgCO₂ /productUnit. productUnit is the unit selected for the product. The unit value is changed to tCO₂ e/productUnit or gCO₂ e/productUnit based on the emission quantity. For more information, see the quantity column.
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
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.product_unit is not None:
            result['productUnit'] = self.product_unit

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetInventoryListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('productUnit') is not None:
            self.product_unit = m.get('productUnit')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class GetInventoryListResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
        process_name: str = None,
    ):
        # Emission quantity: may be positive, negative, or 0. To ensure the calculation accuracy, 24 decimal places are reserved for the calculation process. We recommend that you intercept data based on your business requirements.
        self.carbon_emission = carbon_emission
        # Name 
        # 
        # > The name is related to the request parameters group. Request parameters: resource, return name parameter meaning: list name; request parameters: process, return name parameter meaning: process name; request parameters: resourceType, return name parameter meaning: inventory resource type name; request parameters: processType, return name parameter meaning: flow name.
        self.name = name
        # Percentage
        self.percent = percent
        # Process Name: It is only meaningful when the request parameters group is resource.
        self.process_name = process_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        if self.name is not None:
            result['name'] = self.name

        if self.percent is not None:
            result['percent'] = self.percent

        if self.process_name is not None:
            result['processName'] = self.process_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('processName') is not None:
            self.process_name = m.get('processName')

        return self

