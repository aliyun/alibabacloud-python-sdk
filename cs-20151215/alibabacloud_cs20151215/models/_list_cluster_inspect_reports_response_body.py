# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListClusterInspectReportsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        reports: List[main_models.ListClusterInspectReportsResponseBodyReports] = None,
        request_id: str = None,
    ):
        # The pagination token.
        self.next_token = next_token
        # The list of inspection reports.
        self.reports = reports
        # The request ID.
        self.request_id = request_id

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
        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.reports = []
        if m.get('reports') is not None:
            for k1 in m.get('reports'):
                temp_model = main_models.ListClusterInspectReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListClusterInspectReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        report_id: str = None,
        start_time: str = None,
        status: str = None,
        summary: main_models.ListClusterInspectReportsResponseBodyReportsSummary = None,
    ):
        # The report completion time.
        self.end_time = end_time
        # An inspection report ID.
        self.report_id = report_id
        # The report start time.
        self.start_time = start_time
        # The inspection report status.
        self.status = status
        # The inspection summary.
        self.summary = summary

    def validate(self):
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.report_id is not None:
            result['reportId'] = self.report_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            temp_model = main_models.ListClusterInspectReportsResponseBodyReportsSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        return self

class ListClusterInspectReportsResponseBodyReportsSummary(DaraModel):
    def __init__(
        self,
        advice_count: int = None,
        code: str = None,
        error_count: int = None,
        normal_count: int = None,
        warn_count: int = None,
    ):
        # The number of items whose result is advice.
        self.advice_count = advice_count
        # Aggregated inspection task result code.
        self.code = code
        # The number of items whose result is error.
        self.error_count = error_count
        # The number of items whose result is normal.
        self.normal_count = normal_count
        # The number of items whose result is warning.
        self.warn_count = warn_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advice_count is not None:
            result['adviceCount'] = self.advice_count

        if self.code is not None:
            result['code'] = self.code

        if self.error_count is not None:
            result['errorCount'] = self.error_count

        if self.normal_count is not None:
            result['normalCount'] = self.normal_count

        if self.warn_count is not None:
            result['warnCount'] = self.warn_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adviceCount') is not None:
            self.advice_count = m.get('adviceCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('errorCount') is not None:
            self.error_count = m.get('errorCount')

        if m.get('normalCount') is not None:
            self.normal_count = m.get('normalCount')

        if m.get('warnCount') is not None:
            self.warn_count = m.get('warnCount')

        return self

