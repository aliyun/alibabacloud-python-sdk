# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetGwpBenchmarkSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGwpBenchmarkSummaryResponseBodyData = None,
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
            temp_model = main_models.GetGwpBenchmarkSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGwpBenchmarkSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetGwpBenchmarkSummaryResponseBodyDataItems] = None,
        quantity: int = None,
        unit: str = None,
    ):
        # Carbon Reduction Contribution Top4 Details.
        self.items = items
        # Emission amount is presented with four decimal places. Normally, modeling doesn\\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
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

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGwpBenchmarkSummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class GetGwpBenchmarkSummaryResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        name: str = None,
        percent: str = None,
        quantity: int = None,
        unit: str = None,
    ):
        # Name of carbon reduction details.
        self.name = name
        # Percentage of emissions. The value is of the string type. Two decimal places are reserved for numbers. For example, "99.01" indicates the 99.01% of this type of emissions to the total emissions. Note that the returned string itself does not contain a percent sign.
        self.percent = percent
        # Emission amount is presented with four decimal places. Normally, modeling doesn\\"t result in negative values, but users can represent carbon reductions as negatives. The amount, paired with the unit, defines the emissions. Both are dynamically adjusted. If emissions exceed `1000 kgCO₂e/productUnit`, they convert to `tCO₂e/productUnit`. If they fall below `1 kgCO₂e/productUnit`, they convert to `gCO₂e/productUnit`. Otherwise, they stay in `kgCO₂e/productUnit`.
        self.quantity = quantity
        # Unit of emissions. The default value is `kgCO₂e/productUnit.` `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.percent is not None:
            result['percent'] = self.percent

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

