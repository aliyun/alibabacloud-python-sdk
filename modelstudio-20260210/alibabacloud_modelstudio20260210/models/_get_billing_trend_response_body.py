# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetBillingTrendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBillingTrendResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The request result code.
        self.code = code
        # The response data.
        self.data = data
        # The request result description.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetBillingTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetBillingTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        cost_totals: main_models.GetBillingTrendResponseBodyDataCostTotals = None,
        group_by_total: List[main_models.GetBillingTrendResponseBodyDataGroupByTotal] = None,
        result_by_time: List[main_models.GetBillingTrendResponseBodyDataResultByTime] = None,
    ):
        # The total cost for the entire query time range, including the top N groups and "Others".
        self.cost_totals = cost_totals
        # The total cost of the top N groups and the optional "Others" group within the period.
        self.group_by_total = group_by_total
        # The cost trend list sorted by time in ascending order.
        self.result_by_time = result_by_time

    def validate(self):
        if self.cost_totals:
            self.cost_totals.validate()
        if self.group_by_total:
            for v1 in self.group_by_total:
                 if v1:
                    v1.validate()
        if self.result_by_time:
            for v1 in self.result_by_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_totals is not None:
            result['costTotals'] = self.cost_totals.to_map()

        result['groupByTotal'] = []
        if self.group_by_total is not None:
            for k1 in self.group_by_total:
                result['groupByTotal'].append(k1.to_map() if k1 else None)

        result['resultByTime'] = []
        if self.result_by_time is not None:
            for k1 in self.result_by_time:
                result['resultByTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('costTotals') is not None:
            temp_model = main_models.GetBillingTrendResponseBodyDataCostTotals()
            self.cost_totals = temp_model.from_map(m.get('costTotals'))

        self.group_by_total = []
        if m.get('groupByTotal') is not None:
            for k1 in m.get('groupByTotal'):
                temp_model = main_models.GetBillingTrendResponseBodyDataGroupByTotal()
                self.group_by_total.append(temp_model.from_map(k1))

        self.result_by_time = []
        if m.get('resultByTime') is not None:
            for k1 in m.get('resultByTime'):
                temp_model = main_models.GetBillingTrendResponseBodyDataResultByTime()
                self.result_by_time.append(temp_model.from_map(k1))

        return self

class GetBillingTrendResponseBodyDataResultByTime(DaraModel):
    def __init__(
        self,
        period: str = None,
        period_details: List[main_models.GetBillingTrendResponseBodyDataResultByTimePeriodDetails] = None,
        total: main_models.GetBillingTrendResponseBodyDataResultByTimeTotal = None,
    ):
        # The statistical period. DAY returns yyyyMMdd. MONTH returns yyyyMM.
        self.period = period
        # The cost groups that actually exist in the current period.
        self.period_details = period_details
        # The total cost for the current period.
        self.total = total

    def validate(self):
        if self.period_details:
            for v1 in self.period_details:
                 if v1:
                    v1.validate()
        if self.total:
            self.total.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['period'] = self.period

        result['periodDetails'] = []
        if self.period_details is not None:
            for k1 in self.period_details:
                result['periodDetails'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('period') is not None:
            self.period = m.get('period')

        self.period_details = []
        if m.get('periodDetails') is not None:
            for k1 in m.get('periodDetails'):
                temp_model = main_models.GetBillingTrendResponseBodyDataResultByTimePeriodDetails()
                self.period_details.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            temp_model = main_models.GetBillingTrendResponseBodyDataResultByTimeTotal()
            self.total = temp_model.from_map(m.get('total'))

        return self

class GetBillingTrendResponseBodyDataResultByTimeTotal(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        pretax_amount: str = None,
        tax_amount: str = None,
    ):
        # The total amount for the current period.
        self.amount = amount
        # The currency of the amount for the current period.
        self.currency = currency
        # The pretax amount for the current period.
        self.pretax_amount = pretax_amount
        # The tax amount for the current period.
        self.tax_amount = tax_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.currency is not None:
            result['currency'] = self.currency

        if self.pretax_amount is not None:
            result['pretaxAmount'] = self.pretax_amount

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('pretaxAmount') is not None:
            self.pretax_amount = m.get('pretaxAmount')

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        return self

class GetBillingTrendResponseBodyDataResultByTimePeriodDetails(DaraModel):
    def __init__(
        self,
        amount: str = None,
        key: str = None,
        name: str = None,
        percentage: str = None,
        pretax_amount: str = None,
        tax_amount: str = None,
    ):
        # The amount of the group within the current period.
        self.amount = amount
        # The grouping dimension value. Data beyond the top N uses DIMENSION_GROUP_OTHERS_VALUE.
        self.key = key
        # The display name of the group. This value is affected by the locale parameter.
        self.name = name
        # The ratio of the current group amount to the total amount of the current period.
        self.percentage = percentage
        # The pretax amount of the group within the current period.
        self.pretax_amount = pretax_amount
        # The tax amount of the group within the current period.
        self.tax_amount = tax_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.percentage is not None:
            result['percentage'] = self.percentage

        if self.pretax_amount is not None:
            result['pretaxAmount'] = self.pretax_amount

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percentage') is not None:
            self.percentage = m.get('percentage')

        if m.get('pretaxAmount') is not None:
            self.pretax_amount = m.get('pretaxAmount')

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        return self

class GetBillingTrendResponseBodyDataGroupByTotal(DaraModel):
    def __init__(
        self,
        amount: str = None,
        key: str = None,
        name: str = None,
        pretax_amount: str = None,
        tax_amount: str = None,
    ):
        # The total amount of the current group.
        self.amount = amount
        # The grouping dimension value.
        self.key = key
        # The display name of the group. This value is affected by the locale parameter.
        self.name = name
        # The pretax amount of the current group.
        self.pretax_amount = pretax_amount
        # The tax amount of the current group.
        self.tax_amount = tax_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.pretax_amount is not None:
            result['pretaxAmount'] = self.pretax_amount

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pretaxAmount') is not None:
            self.pretax_amount = m.get('pretaxAmount')

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        return self

class GetBillingTrendResponseBodyDataCostTotals(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        pretax_amount: str = None,
        tax_amount: str = None,
    ):
        # The total amount.
        self.amount = amount
        # The currency of the amount.
        self.currency = currency
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The tax amount.
        self.tax_amount = tax_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.currency is not None:
            result['currency'] = self.currency

        if self.pretax_amount is not None:
            result['pretaxAmount'] = self.pretax_amount

        if self.tax_amount is not None:
            result['taxAmount'] = self.tax_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('pretaxAmount') is not None:
            self.pretax_amount = m.get('pretaxAmount')

        if m.get('taxAmount') is not None:
            self.tax_amount = m.get('taxAmount')

        return self

