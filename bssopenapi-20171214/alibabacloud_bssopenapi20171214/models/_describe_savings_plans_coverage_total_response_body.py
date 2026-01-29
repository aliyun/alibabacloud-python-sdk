# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeSavingsPlansCoverageTotalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSavingsPlansCoverageTotalResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The return data.
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
            temp_model = main_models.DescribeSavingsPlansCoverageTotalResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSavingsPlansCoverageTotalResponseBodyData(DaraModel):
    def __init__(
        self,
        period_coverage: List[main_models.DescribeSavingsPlansCoverageTotalResponseBodyDataPeriodCoverage] = None,
        total_coverage: main_models.DescribeSavingsPlansCoverageTotalResponseBodyDataTotalCoverage = None,
    ):
        # The coverage in different periods.
        self.period_coverage = period_coverage
        # The coverage summary.
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
                temp_model = main_models.DescribeSavingsPlansCoverageTotalResponseBodyDataPeriodCoverage()
                self.period_coverage.append(temp_model.from_map(k1))

        if m.get('TotalCoverage') is not None:
            temp_model = main_models.DescribeSavingsPlansCoverageTotalResponseBodyDataTotalCoverage()
            self.total_coverage = temp_model.from_map(m.get('TotalCoverage'))

        return self

class DescribeSavingsPlansCoverageTotalResponseBodyDataTotalCoverage(DaraModel):
    def __init__(
        self,
        coverage_percentage: float = None,
        deduct_amount: float = None,
    ):
        # The total coverage.
        self.coverage_percentage = coverage_percentage
        # The total deducted amount.
        self.deduct_amount = deduct_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage_percentage is not None:
            result['CoveragePercentage'] = self.coverage_percentage

        if self.deduct_amount is not None:
            result['DeductAmount'] = self.deduct_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoveragePercentage') is not None:
            self.coverage_percentage = m.get('CoveragePercentage')

        if m.get('DeductAmount') is not None:
            self.deduct_amount = m.get('DeductAmount')

        return self

class DescribeSavingsPlansCoverageTotalResponseBodyDataPeriodCoverage(DaraModel):
    def __init__(
        self,
        percentage: float = None,
        period: str = None,
    ):
        # The coverage.
        self.percentage = percentage
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
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.period is not None:
            result['Period'] = self.period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        return self

