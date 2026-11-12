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
        # The query result of the periodic report list, which contains the Reports array. The array is empty if no available reports exist.
        self.data = data
        # The unique identity of the request, which is used for Tracing Analysis and troubleshooting. Provide this ID when troubleshooting exceptions.
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
        # The available report records sorted by period from newest to oldest. By default, up to ten records are returned. If LatestOnly is set to true, at most one record is returned. The array is empty if no reports exist. A single natural week may have multiple report records. Use ReportId to distinguish them. The list does not contain download URLs. The actual download status is subject to the result of GetAiReport.
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
        # The end time of the natural week to which the report belongs, exclusive. The natural week ends at 00:00:00 on the following Monday in UTC+8 (Asia/Shanghai). This field is transformed to UTC RFC 3339 format and ends with Z. The example corresponds to 00:00:00 on Monday, November 9, 2026, UTC+8.
        self.period_end = period_end
        # The start time of the natural week to which the report belongs, inclusive. The natural week is calculated based on UTC+8 (Asia/Shanghai) and starts at 00:00:00 on Monday. This field is transformed to UTC RFC 3339 format and ends with Z. The example corresponds to 00:00:00 on Monday, November 2, 2026, UTC+8.
        self.period_start = period_start
        # The product code of the data product to which the report belongs. This is consistent with the ProductCode of the current request.
        self.product_code = product_code
        # The unique ID of the periodic report. Pass this value as the reportId parameter to GetAiReport to query the current status of the report and obtain the download URL when it is available.
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

