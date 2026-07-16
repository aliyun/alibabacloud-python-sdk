# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class SumDailyBillsByItemResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SumDailyBillsByItemResponseBodyData = None,
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
            temp_model = main_models.SumDailyBillsByItemResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class SumDailyBillsByItemResponseBodyData(DaraModel):
    def __init__(
        self,
        item_summary_bills: List[main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBills] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.item_summary_bills = item_summary_bills
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.item_summary_bills:
            for v1 in self.item_summary_bills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['itemSummaryBills'] = []
        if self.item_summary_bills is not None:
            for k1 in self.item_summary_bills:
                result['itemSummaryBills'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_summary_bills = []
        if m.get('itemSummaryBills') is not None:
            for k1 in m.get('itemSummaryBills'):
                temp_model = main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBills()
                self.item_summary_bills.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class SumDailyBillsByItemResponseBodyDataItemSummaryBills(DaraModel):
    def __init__(
        self,
        currency: str = None,
        daily_sum_bills: List[main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBills] = None,
        item_name: str = None,
        percentage: float = None,
        spec_code: str = None,
        total_cost: str = None,
    ):
        self.currency = currency
        self.daily_sum_bills = daily_sum_bills
        self.item_name = item_name
        self.percentage = percentage
        self.spec_code = spec_code
        self.total_cost = total_cost

    def validate(self):
        if self.daily_sum_bills:
            for v1 in self.daily_sum_bills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['currency'] = self.currency

        result['dailySumBills'] = []
        if self.daily_sum_bills is not None:
            for k1 in self.daily_sum_bills:
                result['dailySumBills'].append(k1.to_map() if k1 else None)

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.percentage is not None:
            result['percentage'] = self.percentage

        if self.spec_code is not None:
            result['specCode'] = self.spec_code

        if self.total_cost is not None:
            result['totalCost'] = self.total_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currency') is not None:
            self.currency = m.get('currency')

        self.daily_sum_bills = []
        if m.get('dailySumBills') is not None:
            for k1 in m.get('dailySumBills'):
                temp_model = main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBills()
                self.daily_sum_bills.append(temp_model.from_map(k1))

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')

        if m.get('totalCost') is not None:
            self.total_cost = m.get('totalCost')

        return self

class SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBills(DaraModel):
    def __init__(
        self,
        cost: str = None,
        currency: str = None,
        date_time: str = None,
        item_bills: List[main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBillsItemBills] = None,
    ):
        self.cost = cost
        self.currency = currency
        self.date_time = date_time
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
                temp_model = main_models.SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBillsItemBills()
                self.item_bills.append(temp_model.from_map(k1))

        return self

class SumDailyBillsByItemResponseBodyDataItemSummaryBillsDailySumBillsItemBills(DaraModel):
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

