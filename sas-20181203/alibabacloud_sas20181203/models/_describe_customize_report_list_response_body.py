# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomizeReportListResponseBody(DaraModel):
    def __init__(
        self,
        report_list: List[main_models.DescribeCustomizeReportListResponseBodyReportList] = None,
        request_id: str = None,
    ):
        # The reports.
        self.report_list = report_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.report_list:
            for v1 in self.report_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReportList'] = []
        if self.report_list is not None:
            for k1 in self.report_list:
                result['ReportList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report_list = []
        if m.get('ReportList') is not None:
            for k1 in m.get('ReportList'):
                temp_model = main_models.DescribeCustomizeReportListResponseBodyReportList()
                self.report_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomizeReportListResponseBodyReportList(DaraModel):
    def __init__(
        self,
        is_default: str = None,
        pinned_time: int = None,
        report_days: int = None,
        report_end_date: int = None,
        report_id: int = None,
        report_start_date: int = None,
        report_status: str = None,
        report_type: int = None,
        report_version: str = None,
        title: str = None,
    ):
        # Indicates whether the report is the default report. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.is_default = is_default
        # The timestamp when the report is pinned. Unit: milliseconds.
        self.pinned_time = pinned_time
        # The most recent days for report statistics.
        self.report_days = report_days
        # The end date on which the report is sent. The value is a UNIX timestamp. Unit: milliseconds.
        self.report_end_date = report_end_date
        # The ID of the report.
        self.report_id = report_id
        # The start date on which the report is sent. The value is a UNIX timestamp. Unit: milliseconds.
        self.report_start_date = report_start_date
        # The state of the report. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.report_status = report_status
        # The type of the report. Valid values:
        # 
        # *   **0**: daily report
        # *   **1**: weekly report
        # *   **2**: monthly report
        # *   **3**: report whose statistics are collected in a custom time range
        self.report_type = report_type
        # The report version.
        self.report_version = report_version
        # The name of the report.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.pinned_time is not None:
            result['PinnedTime'] = self.pinned_time

        if self.report_days is not None:
            result['ReportDays'] = self.report_days

        if self.report_end_date is not None:
            result['ReportEndDate'] = self.report_end_date

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_start_date is not None:
            result['ReportStartDate'] = self.report_start_date

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_version is not None:
            result['ReportVersion'] = self.report_version

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('PinnedTime') is not None:
            self.pinned_time = m.get('PinnedTime')

        if m.get('ReportDays') is not None:
            self.report_days = m.get('ReportDays')

        if m.get('ReportEndDate') is not None:
            self.report_end_date = m.get('ReportEndDate')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportStartDate') is not None:
            self.report_start_date = m.get('ReportStartDate')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportVersion') is not None:
            self.report_version = m.get('ReportVersion')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

