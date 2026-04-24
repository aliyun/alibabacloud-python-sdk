# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetScheduledReportsResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        reports: List[main_models.GetScheduledReportsResponseBodyReports] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response message.
        self.message = message
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of reports returned on each page.
        self.page_size = page_size
        # The details of the report.
        self.reports = reports
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of returned reports.
        self.total_count = total_count

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
        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.GetScheduledReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetScheduledReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        end_time: str = None,
        inspection_items: str = None,
        region_id: str = None,
        report_language: str = None,
        report_type: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        # The creation time of the task.
        self.created_time = created_time
        # The end time of the inspection task. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.end_time = end_time
        self.inspection_items = inspection_items
        self.region_id = region_id
        self.report_language = report_language
        self.report_type = report_type
        # The start time of the inspection task. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.start_time = start_time
        # The status of the task.
        self.status = status
        # The ID of the report.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.inspection_items is not None:
            result['InspectionItems'] = self.inspection_items

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_language is not None:
            result['ReportLanguage'] = self.report_language

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InspectionItems') is not None:
            self.inspection_items = m.get('InspectionItems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportLanguage') is not None:
            self.report_language = m.get('ReportLanguage')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

