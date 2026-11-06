# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeInspectionReportListResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        report_items: List[main_models.DescribeInspectionReportListResponseBodyReportItems] = None,
        request_id: str = None,
        score: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The list of inspection reports.
        self.report_items = report_items
        # The request ID.
        self.request_id = request_id
        # The score returned by the inspection task.
        self.score = score
        # The total number of reports that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.report_items:
            for v1 in self.report_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ReportItems'] = []
        if self.report_items is not None:
            for k1 in self.report_items:
                result['ReportItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.score is not None:
            result['Score'] = self.score

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.report_items = []
        if m.get('ReportItems') is not None:
            for k1 in m.get('ReportItems'):
                temp_model = main_models.DescribeInspectionReportListResponseBodyReportItems()
                self.report_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInspectionReportListResponseBodyReportItems(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        latest: str = None,
        region_id: str = None,
        report_description: str = None,
        report_id: str = None,
        report_score: int = None,
        report_status: str = None,
        report_summary: str = None,
        report_time: str = None,
        sub_items: List[main_models.DescribeInspectionReportListResponseBodyReportItemsSubItems] = None,
        task_id: str = None,
    ):
        # The ID of the inspected PolarDB cluster.
        self.dbcluster_id = dbcluster_id
        # Indicates whether the inspection report is the latest report. The value is returned as a string.
        self.latest = latest
        # The region ID of the inspected cluster.
        self.region_id = region_id
        # The detailed description of the inspection report.
        self.report_description = report_description
        # The ID of the inspection report.
        self.report_id = report_id
        # The score of the inspection report.
        self.report_score = report_score
        # The status of the inspection report.
        self.report_status = report_status
        # The summary of the inspection report.
        self.report_summary = report_summary
        # The time when the inspection report was generated. The time is in the yyyy-MM-dd HH:mm:ss format and is in the UTC+8 time zone.
        self.report_time = report_time
        # The number of check items categorized by inspection result level.
        self.sub_items = sub_items
        # The ID of the inspection task.
        self.task_id = task_id

    def validate(self):
        if self.sub_items:
            for v1 in self.sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.latest is not None:
            result['Latest'] = self.latest

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_description is not None:
            result['ReportDescription'] = self.report_description

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_score is not None:
            result['ReportScore'] = self.report_score

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.report_summary is not None:
            result['ReportSummary'] = self.report_summary

        if self.report_time is not None:
            result['ReportTime'] = self.report_time

        result['SubItems'] = []
        if self.sub_items is not None:
            for k1 in self.sub_items:
                result['SubItems'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Latest') is not None:
            self.latest = m.get('Latest')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportDescription') is not None:
            self.report_description = m.get('ReportDescription')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportScore') is not None:
            self.report_score = m.get('ReportScore')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('ReportSummary') is not None:
            self.report_summary = m.get('ReportSummary')

        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')

        self.sub_items = []
        if m.get('SubItems') is not None:
            for k1 in m.get('SubItems'):
                temp_model = main_models.DescribeInspectionReportListResponseBodyReportItemsSubItems()
                self.sub_items.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeInspectionReportListResponseBodyReportItemsSubItems(DaraModel):
    def __init__(
        self,
        critical: int = None,
        info: int = None,
        normal: int = None,
        warning: int = None,
    ):
        # The number of check items at the critical level.
        self.critical = critical
        # The number of check items at the info level.
        self.info = info
        # The number of normal check items.
        self.normal = normal
        # The number of check items at the warning level.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.info is not None:
            result['Info'] = self.info

        if self.normal is not None:
            result['Normal'] = self.normal

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('Normal') is not None:
            self.normal = m.get('Normal')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

