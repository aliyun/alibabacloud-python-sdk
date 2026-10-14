# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlPatternCompareReportResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeSqlPatternCompareReportResponseBodyItems] = None,
        metric_type: str = None,
        page_number: int = None,
        page_size: int = None,
        report_id: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The Pattern details on the current page. An empty array is returned if no results match the conditions.
        self.items = items
        # The analysis metric. Valid values:
        # 
        # - `QUERY_COUNT`: the number of query executions.
        # - `CPU_COST`: the CPU consumption.
        # - `SHUFFLE_SIZE`: the amount of shuffle data.
        # - `PEAK_MEMORY`: the peak memory consumption.
        # - `SCAN_SIZE`: the amount of scanned data.
        self.metric_type = metric_type
        # The page number of the returned page, starting from 1.
        self.page_number = page_number
        # The maximum number of entries returned per page for this query.
        self.page_size = page_size
        # The ID of the SQL Pattern comparison report.
        self.report_id = report_id
        # The request ID.
        self.request_id = request_id
        # The total number of Patterns that match the current report, analysis dimension, and change rate filter conditions. This is not the number of entries on the current page.
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

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.report_id is not None:
            result['ReportId'] = self.report_id

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
                temp_model = main_models.DescribeSqlPatternCompareReportResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSqlPatternCompareReportResponseBodyItems(DaraModel):
    def __init__(
        self,
        avg_execution_time: str = None,
        avg_planning_time: str = None,
        avg_rt: str = None,
        max_execution_time: str = None,
        max_planning_time: str = None,
        max_rt: str = None,
        metric_values: Dict[str, main_models.ItemsMetricValuesValue] = None,
        pattern: str = None,
        query_count: int = None,
        query_count_display_value: str = None,
        rank: int = None,
        risk_level: str = None,
        sql_pattern_hash: str = None,
        total_query_time: str = None,
        total_scan_cost: str = None,
    ):
        # The display string of the average execution duration for Time 2, in seconds. This field is returned only for the CPU_COST dimension.
        self.avg_execution_time = avg_execution_time
        # The display string of the average planning duration for Time 2, in seconds. This field is returned only for the CPU_COST dimension.
        self.avg_planning_time = avg_planning_time
        # The display string of the average query response time for Time 2, in seconds. This field is returned for all analysis dimensions.
        self.avg_rt = avg_rt
        # The display string of the maximum execution duration for Time 2, in seconds. This field is returned only for the CPU_COST dimension.
        self.max_execution_time = max_execution_time
        # The display string of the maximum planning duration for Time 2, in seconds. This field is returned only for the CPU_COST dimension.
        self.max_planning_time = max_planning_time
        # The display string of the maximum query response time for Time 2, in seconds. This field is returned for all analysis dimensions.
        self.max_rt = max_rt
        # The primary metric mapping for the current analysis dimension. Valid keys:
        # 
        # - `QUERY_COUNT`: the number of query executions.
        # - `CPU_COST`: the CPU consumption.
        # - `SHUFFLE_SIZE`: the shuffle data volume.
        # - `PEAK_MEMORY`: the peak memory consumption.
        # - `SCAN_SIZE`: the scan data volume.
        # 
        # > Each result contains only one key that matches the `MetricType` request parameter.
        self.metric_values = metric_values
        # The parameterized SQL Pattern text. This field is empty or not returned when IncludePattern is set to false. When the text is unavailable, a prompt containing a hash identifier may be returned.
        self.pattern = pattern
        # The number of query executions for Time 2, in count. This field is returned for the CPU_COST, SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE dimensions.
        self.query_count = query_count
        # The display string of the number of query executions for Time 2. The applicable scope is the same as QueryCount.
        self.query_count_display_value = query_count_display_value
        # The global sequence number in the current filtered and sorted results, starting from 1 and numbered continuously across pages.
        self.rank = rank
        # The change level for the current analysis dimension. Valid values:
        # 
        # - `NEW`: A new Pattern. Returned only for NEW reports.
        # - `SLIGHT`: A slight change. The average change rate is in the range of (0%, 20%].
        # - `MODERATE`: A moderate change. The average change rate is in the range of (20%, 50%].
        # - `HIGH`: A high change. The average change rate is in the range of (50%, 100%].
        # - `SEVERE`: A severe change. The average change rate is greater than 100%, or the change represents zero-baseline growth.
        # 
        # > The change level only indicates the magnitude of metric growth and cannot be used alone to determine the cause of a fault.
        self.risk_level = risk_level
        # The hash identifier of the SQL Pattern, returned as a string. Store and pass this value as a string to avoid precision loss caused by numeric conversion.
        self.sql_pattern_hash = sql_pattern_hash
        # The display string of the total query duration for Time 2, in seconds. This field is returned only for the QUERY_COUNT dimension.
        self.total_query_time = total_query_time
        # The display string of the total scan duration for Time 2, in seconds. This field is returned only for the SCAN_SIZE dimension.
        self.total_scan_cost = total_scan_cost

    def validate(self):
        if self.metric_values:
            for v1 in self.metric_values.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_execution_time is not None:
            result['AvgExecutionTime'] = self.avg_execution_time

        if self.avg_planning_time is not None:
            result['AvgPlanningTime'] = self.avg_planning_time

        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt

        if self.max_execution_time is not None:
            result['MaxExecutionTime'] = self.max_execution_time

        if self.max_planning_time is not None:
            result['MaxPlanningTime'] = self.max_planning_time

        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt

        result['MetricValues'] = {}
        if self.metric_values is not None:
            for k1, v1 in self.metric_values.items():
                result['MetricValues'][k1] = v1.to_map() if v1 else None

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.query_count_display_value is not None:
            result['QueryCountDisplayValue'] = self.query_count_display_value

        if self.rank is not None:
            result['Rank'] = self.rank

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sql_pattern_hash is not None:
            result['SqlPatternHash'] = self.sql_pattern_hash

        if self.total_query_time is not None:
            result['TotalQueryTime'] = self.total_query_time

        if self.total_scan_cost is not None:
            result['TotalScanCost'] = self.total_scan_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExecutionTime') is not None:
            self.avg_execution_time = m.get('AvgExecutionTime')

        if m.get('AvgPlanningTime') is not None:
            self.avg_planning_time = m.get('AvgPlanningTime')

        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')

        if m.get('MaxExecutionTime') is not None:
            self.max_execution_time = m.get('MaxExecutionTime')

        if m.get('MaxPlanningTime') is not None:
            self.max_planning_time = m.get('MaxPlanningTime')

        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')

        self.metric_values = {}
        if m.get('MetricValues') is not None:
            for k1, v1 in m.get('MetricValues').items():
                temp_model = main_models.ItemsMetricValuesValue()
                self.metric_values[k1] = temp_model.from_map(v1)

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('QueryCountDisplayValue') is not None:
            self.query_count_display_value = m.get('QueryCountDisplayValue')

        if m.get('Rank') is not None:
            self.rank = m.get('Rank')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SqlPatternHash') is not None:
            self.sql_pattern_hash = m.get('SqlPatternHash')

        if m.get('TotalQueryTime') is not None:
            self.total_query_time = m.get('TotalQueryTime')

        if m.get('TotalScanCost') is not None:
            self.total_scan_cost = m.get('TotalScanCost')

        return self

