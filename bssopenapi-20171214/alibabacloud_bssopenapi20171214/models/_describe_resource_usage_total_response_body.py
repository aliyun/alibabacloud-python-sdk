# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceUsageTotalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResourceUsageTotalResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The queried data.
        self.data = data
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeResourceUsageTotalResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourceUsageTotalResponseBodyData(DaraModel):
    def __init__(
        self,
        period_coverage: List[main_models.DescribeResourceUsageTotalResponseBodyDataPeriodCoverage] = None,
        total_usage: main_models.DescribeResourceUsageTotalResponseBodyDataTotalUsage = None,
    ):
        # The usage of resource plans in the specified period.
        self.period_coverage = period_coverage
        # The total usage of resource plans.
        self.total_usage = total_usage

    def validate(self):
        if self.period_coverage:
            for v1 in self.period_coverage:
                 if v1:
                    v1.validate()
        if self.total_usage:
            self.total_usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PeriodCoverage'] = []
        if self.period_coverage is not None:
            for k1 in self.period_coverage:
                result['PeriodCoverage'].append(k1.to_map() if k1 else None)

        if self.total_usage is not None:
            result['TotalUsage'] = self.total_usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.period_coverage = []
        if m.get('PeriodCoverage') is not None:
            for k1 in m.get('PeriodCoverage'):
                temp_model = main_models.DescribeResourceUsageTotalResponseBodyDataPeriodCoverage()
                self.period_coverage.append(temp_model.from_map(k1))

        if m.get('TotalUsage') is not None:
            temp_model = main_models.DescribeResourceUsageTotalResponseBodyDataTotalUsage()
            self.total_usage = temp_model.from_map(m.get('TotalUsage'))

        return self

class DescribeResourceUsageTotalResponseBodyDataTotalUsage(DaraModel):
    def __init__(
        self,
        postpaid_cost: float = None,
        potential_saved_cost: float = None,
        reservation_cost: float = None,
        saved_cost: float = None,
        usage_percentage: float = None,
    ):
        # The total costs of pay-as-you-go instances.
        self.postpaid_cost = postpaid_cost
        # The total potential savings.
        self.potential_saved_cost = potential_saved_cost
        # The fee of purchased resource plans.
        self.reservation_cost = reservation_cost
        # The total savings.
        self.saved_cost = saved_cost
        # The total usage of resource plans.
        self.usage_percentage = usage_percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.postpaid_cost is not None:
            result['PostpaidCost'] = self.postpaid_cost

        if self.potential_saved_cost is not None:
            result['PotentialSavedCost'] = self.potential_saved_cost

        if self.reservation_cost is not None:
            result['ReservationCost'] = self.reservation_cost

        if self.saved_cost is not None:
            result['SavedCost'] = self.saved_cost

        if self.usage_percentage is not None:
            result['UsagePercentage'] = self.usage_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostpaidCost') is not None:
            self.postpaid_cost = m.get('PostpaidCost')

        if m.get('PotentialSavedCost') is not None:
            self.potential_saved_cost = m.get('PotentialSavedCost')

        if m.get('ReservationCost') is not None:
            self.reservation_cost = m.get('ReservationCost')

        if m.get('SavedCost') is not None:
            self.saved_cost = m.get('SavedCost')

        if m.get('UsagePercentage') is not None:
            self.usage_percentage = m.get('UsagePercentage')

        return self

class DescribeResourceUsageTotalResponseBodyDataPeriodCoverage(DaraModel):
    def __init__(
        self,
        period: str = None,
        usage_percentage: float = None,
    ):
        # The period.
        self.period = period
        # The usage of resource plans.
        self.usage_percentage = usage_percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period is not None:
            result['Period'] = self.period

        if self.usage_percentage is not None:
            result['UsagePercentage'] = self.usage_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('UsagePercentage') is not None:
            self.usage_percentage = m.get('UsagePercentage')

        return self

