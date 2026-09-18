# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumBillsByDateResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.SumBillsByDateResponseBodyData] = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The list of results.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.SumBillsByDateResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumBillsByDateResponseBodyData(DaraModel):
    def __init__(
        self,
        cost: str = None,
        currency: str = None,
        date_time: str = None,
        item_bills: List[main_models.SumBillsByDateResponseBodyDataItemBills] = None,
    ):
        # The total cost for the specified `dateTime`.
        self.cost = cost
        # The currency. This is a fixed value.
        self.currency = currency
        # The date of the statistics, in `yyyyMMdd` format.
        self.date_time = date_time
        # A list of billable items.
        self.item_bills = item_bills

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
        if self.cost is not None:
            result['cost'] = self.cost

        if self.currency is not None:
            result['currency'] = self.currency

        if self.date_time is not None:
            result['dateTime'] = self.date_time

        result['itemBills'] = []
        if self.item_bills is not None:
            for k1 in self.item_bills:
                result['itemBills'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('dateTime') is not None:
            self.date_time = m.get('dateTime')

        self.item_bills = []
        if m.get('itemBills') is not None:
            for k1 in m.get('itemBills'):
                temp_model = main_models.SumBillsByDateResponseBodyDataItemBills()
                self.item_bills.append(temp_model.from_map(k1))

        return self

class SumBillsByDateResponseBodyDataItemBills(DaraModel):
    def __init__(
        self,
        cost: str = None,
        currency: str = None,
        item_name: str = None,
        percentage: float = None,
    ):
        # The cost.
        self.cost = cost
        # The currency. This is a fixed value.
        self.currency = currency
        # The name of the item. The value of this parameter depends on the `statsType` parameter in the request. If `statsType` is `PROJECT`, this parameter indicates the instance name. If `statsType` is `FEE_ITEM`, this parameter can be a value such as `DRStorage`, `ComputationSql`, or `Storage`.
        self.item_name = item_name
        # The item\\"s cost as a percentage of the total daily cost. This value does not include a percent sign (%).
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

