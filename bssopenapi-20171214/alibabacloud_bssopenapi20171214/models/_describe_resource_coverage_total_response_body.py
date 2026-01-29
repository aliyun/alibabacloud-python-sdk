# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceCoverageTotalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResourceCoverageTotalResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful.
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
            temp_model = main_models.DescribeResourceCoverageTotalResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourceCoverageTotalResponseBodyData(DaraModel):
    def __init__(
        self,
        period_coverage: List[main_models.DescribeResourceCoverageTotalResponseBodyDataPeriodCoverage] = None,
        total_coverage: main_models.DescribeResourceCoverageTotalResponseBodyDataTotalCoverage = None,
    ):
        # The information about the coverage rate of deduction plans within a period.
        self.period_coverage = period_coverage
        # The information about the total coverage data of deduction plans.
        self.total_coverage = total_coverage

    def validate(self):
        if self.period_coverage:
            for v1 in self.period_coverage:
                 if v1:
                    v1.validate()
        if self.total_coverage:
            self.total_coverage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PeriodCoverage'] = []
        if self.period_coverage is not None:
            for k1 in self.period_coverage:
                result['PeriodCoverage'].append(k1.to_map() if k1 else None)

        if self.total_coverage is not None:
            result['TotalCoverage'] = self.total_coverage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.period_coverage = []
        if m.get('PeriodCoverage') is not None:
            for k1 in m.get('PeriodCoverage'):
                temp_model = main_models.DescribeResourceCoverageTotalResponseBodyDataPeriodCoverage()
                self.period_coverage.append(temp_model.from_map(k1))

        if m.get('TotalCoverage') is not None:
            temp_model = main_models.DescribeResourceCoverageTotalResponseBodyDataTotalCoverage()
            self.total_coverage = temp_model.from_map(m.get('TotalCoverage'))

        return self

class DescribeResourceCoverageTotalResponseBodyDataTotalCoverage(DaraModel):
    def __init__(
        self,
        capacity_unit: str = None,
        coverage_percentage: float = None,
        deduct_quantity: float = None,
        total_quantity: float = None,
    ):
        # The unit that is used to measure the resources deducted from deduction plans.
        self.capacity_unit = capacity_unit
        # The total coverage rate of deduction plans.
        self.coverage_percentage = coverage_percentage
        # The total amount of the resources deducted from deduction plans.
        self.deduct_quantity = deduct_quantity
        # The total amount of resources consumed.
        self.total_quantity = total_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit

        if self.coverage_percentage is not None:
            result['CoveragePercentage'] = self.coverage_percentage

        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity

        if self.total_quantity is not None:
            result['TotalQuantity'] = self.total_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')

        if m.get('CoveragePercentage') is not None:
            self.coverage_percentage = m.get('CoveragePercentage')

        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')

        if m.get('TotalQuantity') is not None:
            self.total_quantity = m.get('TotalQuantity')

        return self

class DescribeResourceCoverageTotalResponseBodyDataPeriodCoverage(DaraModel):
    def __init__(
        self,
        coverage_percentage: float = None,
        period: str = None,
    ):
        # The coverage rate of deduction plans within the specified period.
        self.coverage_percentage = coverage_percentage
        # The period.
        # 
        # The value is in the format of yyyyMMddHH.
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage_percentage is not None:
            result['CoveragePercentage'] = self.coverage_percentage

        if self.period is not None:
            result['Period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoveragePercentage') is not None:
            self.coverage_percentage = m.get('CoveragePercentage')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        return self

