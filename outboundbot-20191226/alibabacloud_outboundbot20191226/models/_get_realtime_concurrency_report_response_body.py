# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeConcurrencyReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_date: int = None,
        reports: main_models.GetRealtimeConcurrencyReportResponseBodyReports = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.report_date = report_date
        self.reports = reports
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.reports:
            self.reports.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        if self.reports is not None:
            result['Reports'] = self.reports.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        if m.get('Reports') is not None:
            temp_model = main_models.GetRealtimeConcurrencyReportResponseBodyReports()
            self.reports = temp_model.from_map(m.get('Reports'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRealtimeConcurrencyReportResponseBodyReports(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetRealtimeConcurrencyReportResponseBodyReportsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetRealtimeConcurrencyReportResponseBodyReportsList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetRealtimeConcurrencyReportResponseBodyReportsList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        max_concurrency_limit: int = None,
        min_concurrency_limit: int = None,
        occupied_concurrency_count: int = None,
        report_date: int = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.job_group_id = job_group_id
        self.job_group_name = job_group_name
        self.max_concurrency_limit = max_concurrency_limit
        self.min_concurrency_limit = min_concurrency_limit
        self.occupied_concurrency_count = occupied_concurrency_count
        self.report_date = report_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.max_concurrency_limit is not None:
            result['MaxConcurrencyLimit'] = self.max_concurrency_limit

        if self.min_concurrency_limit is not None:
            result['MinConcurrencyLimit'] = self.min_concurrency_limit

        if self.occupied_concurrency_count is not None:
            result['OccupiedConcurrencyCount'] = self.occupied_concurrency_count

        if self.report_date is not None:
            result['ReportDate'] = self.report_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('MaxConcurrencyLimit') is not None:
            self.max_concurrency_limit = m.get('MaxConcurrencyLimit')

        if m.get('MinConcurrencyLimit') is not None:
            self.min_concurrency_limit = m.get('MinConcurrencyLimit')

        if m.get('OccupiedConcurrencyCount') is not None:
            self.occupied_concurrency_count = m.get('OccupiedConcurrencyCount')

        if m.get('ReportDate') is not None:
            self.report_date = m.get('ReportDate')

        return self

