# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_internetbankopen20240612 import models as main_models
from darabonba.model import DaraModel

class ListProductReportsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListProductReportsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListProductReportsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProductReportsResponseBodyData(DaraModel):
    def __init__(
        self,
        reports: List[main_models.ListProductReportsResponseBodyDataReports] = None,
    ):
        self.reports = reports

    def validate(self):
        if self.reports:
            for v1 in self.reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.ListProductReportsResponseBodyDataReports()
                self.reports.append(temp_model.from_map(k1))

        return self

class ListProductReportsResponseBodyDataReports(DaraModel):
    def __init__(
        self,
        period_end: str = None,
        period_start: str = None,
        product_code: str = None,
        report_id: str = None,
    ):
        self.period_end = period_end
        self.period_start = period_start
        self.product_code = product_code
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_end is not None:
            result['PeriodEnd'] = self.period_end

        if self.period_start is not None:
            result['PeriodStart'] = self.period_start

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodEnd') is not None:
            self.period_end = m.get('PeriodEnd')

        if m.get('PeriodStart') is not None:
            self.period_start = m.get('PeriodStart')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

