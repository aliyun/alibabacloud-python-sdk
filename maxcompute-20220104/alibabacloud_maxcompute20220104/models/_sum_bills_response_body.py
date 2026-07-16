# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumBillsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SumBillsResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.http_code = http_code
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

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.SumBillsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumBillsResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        item_bills: List[main_models.SumBillsResponseBodyDataItemBills] = None,
        total_cost: str = None,
    ):
        self.currency = currency
        self.item_bills = item_bills
        self.total_cost = total_cost

    def validate(self):
        if self.item_bills:
            for v1 in self.item_bills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['currency'] = self.currency

        result['itemBills'] = []
        if self.item_bills is not None:
            for k1 in self.item_bills:
                result['itemBills'].append(k1.to_map() if k1 else None)

        if self.total_cost is not None:
            result['totalCost'] = self.total_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')

        self.item_bills = []
        if m.get('itemBills') is not None:
            for k1 in m.get('itemBills'):
                temp_model = main_models.SumBillsResponseBodyDataItemBills()
                self.item_bills.append(temp_model.from_map(k1))

        if m.get('totalCost') is not None:
            self.total_cost = m.get('totalCost')

        return self

class SumBillsResponseBodyDataItemBills(DaraModel):
    def __init__(
        self,
        cost: str = None,
        currency: str = None,
        item_name: str = None,
        percentage: float = None,
    ):
        self.cost = cost
        self.currency = currency
        self.item_name = item_name
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.currency is not None:
            result['currency'] = self.currency

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.percentage is not None:
            result['percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        return self

