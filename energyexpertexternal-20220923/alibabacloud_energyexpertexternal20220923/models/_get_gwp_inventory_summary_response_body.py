# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetGwpInventorySummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGwpInventorySummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned results.
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
            temp_model = main_models.GetGwpInventorySummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGwpInventorySummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetGwpInventorySummaryResponseBodyDataItems] = None,
        quantity: float = None,
        result_generate_time: int = None,
        unit: str = None,
    ):
        # Top 4 types of carbon footprint contribution.
        self.items = items
        # The emission quantity.
        self.quantity = quantity
        # The time when the result was generated, in the millisecond timestamp format.
        self.result_generate_time = result_generate_time
        # Emission Unit.
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

        if self.result_generate_time is not None:
            result['resultGenerateTime'] = self.result_generate_time

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGwpInventorySummaryResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('resultGenerateTime') is not None:
            self.result_generate_time = m.get('resultGenerateTime')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class GetGwpInventorySummaryResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        name: str = None,
        percent: str = None,
        quantity: float = None,
        unit: str = None,
    ):
        # Inventory resource type name.
        self.name = name
        # Percentage.
        self.percent = percent
        # Quantity.
        self.quantity = quantity
        # The unit.
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

