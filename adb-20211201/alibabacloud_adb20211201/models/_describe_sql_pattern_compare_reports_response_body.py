# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlPatternCompareReportsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSqlPatternCompareReportsResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of reports on the current page. An empty array is returned if no reports match the conditions.
        self.items = items
        # The number of rows per page used in this query.
        self.max_results = max_results
        # The token for the next page. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # The page number used in this query. Pages start from 1.
        self.page_number = page_number
        # The number of rows per page used in this query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of reports that match the conditions.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSqlPatternCompareReportsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSqlPatternCompareReportsResponseBodyItems(DaraModel):
    def __init__(
        self,
        cancel_available: bool = None,
        compare_end_time: str = None,
        compare_start_time: str = None,
        created_at: str = None,
        detail_enabled: bool = None,
        end_time: str = None,
        report_id: int = None,
        report_type: str = None,
        report_type_name: str = None,
        row_number: int = None,
        start_time: str = None,
        status: str = None,
    ):
        # Indicates whether the report can be canceled. The value is true when the report is in the PENDING or RUNNING state.
        self.cancel_available = cancel_available
        # The end time of time range 2. The time is in the yyyy-MM-ddTHH:mmZ UTC format.
        self.compare_end_time = compare_end_time
        # The start time of time range 2. The time is in the yyyy-MM-ddTHH:mmZ UTC format.
        self.compare_start_time = compare_start_time
        # The time when the report was created. The time is in the yyyy-MM-ddTHH:mmZ UTC format.
        self.created_at = created_at
        # Indicates whether report details can be queried. The value is true when the report is in the SUCCESS state.
        self.detail_enabled = detail_enabled
        # The end time of time range 1. The time is in the yyyy-MM-ddTHH:mmZ UTC format.
        self.end_time = end_time
        # The ID of the SQL Pattern comparison report.
        self.report_id = report_id
        # The report type. Valid values:
        # 
        # - `NEW`: new patterns.
        # - `CHANGED`: patterns with increased metrics.
        self.report_type = report_type
        # The name of the report type.
        self.report_type_name = report_type_name
        # The sequence number in the current sorted result. The value starts from 1.
        self.row_number = row_number
        # The start time of time range 1. The time is in the yyyy-MM-ddTHH:mmZ UTC format.
        self.start_time = start_time
        # The report status. Valid values:
        # 
        # - `PENDING`: waiting to be generated.
        # - `RUNNING`: being generated.
        # - `SUCCESS`: generated.
        # - `FAILED`: failed to be generated.
        # - `CANCELED`: canceled.
        # - `EXPIRED`: expired.
        # 
        # > The current list returns only reports in the `PENDING`, `RUNNING`, or `SUCCESS` state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_available is not None:
            result['CancelAvailable'] = self.cancel_available

        if self.compare_end_time is not None:
            result['CompareEndTime'] = self.compare_end_time

        if self.compare_start_time is not None:
            result['CompareStartTime'] = self.compare_start_time

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.detail_enabled is not None:
            result['DetailEnabled'] = self.detail_enabled

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.report_type_name is not None:
            result['ReportTypeName'] = self.report_type_name

        if self.row_number is not None:
            result['RowNumber'] = self.row_number

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelAvailable') is not None:
            self.cancel_available = m.get('CancelAvailable')

        if m.get('CompareEndTime') is not None:
            self.compare_end_time = m.get('CompareEndTime')

        if m.get('CompareStartTime') is not None:
            self.compare_start_time = m.get('CompareStartTime')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DetailEnabled') is not None:
            self.detail_enabled = m.get('DetailEnabled')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('ReportTypeName') is not None:
            self.report_type_name = m.get('ReportTypeName')

        if m.get('RowNumber') is not None:
            self.row_number = m.get('RowNumber')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

