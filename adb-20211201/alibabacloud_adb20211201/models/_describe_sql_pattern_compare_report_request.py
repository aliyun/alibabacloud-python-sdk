# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSqlPatternCompareReportRequest(DaraModel):
    def __init__(
        self,
        change_rate: str = None,
        dbcluster_id: str = None,
        include_pattern: bool = None,
        metric_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        report_id: int = None,
    ):
        # The average change rate filter range for CHANGED reports. The format is `left~right`, where values are expressed as percentages and the interval is left-exclusive and right-inclusive. Examples:
        # 
        # - `100~500`: greater than 100% and less than or equal to 500%.
        # - `100~`: greater than 100% with no upper limit.
        # 
        # > - The left boundary is required and must be no less than 0. The right boundary must be no less than the left boundary.
        # > - This parameter is ignored for NEW reports.
        # > - When the time window 1 metric value is 0 and the time window 2 value is greater than 0, the Pattern is classified as zero-baseline growth and is categorized as `SEVERE` (significant change). To exclude such Patterns, set an upper limit for the change rate.
        self.change_rate = change_rate
        # The ID of the AnalyticDB for MySQL instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to return the parameterized SQL Pattern text. Valid values:
        # 
        # - `true`: Returns the Pattern text.
        # - `false`: Does not return the Pattern text, which reduces the response size.
        # 
        # Default value: `true`.
        self.include_pattern = include_pattern
        # The analysis metric. Valid values:
        # 
        # - `QUERY_COUNT`: the number of query executions.
        # - `CPU_COST`: the CPU consumption.
        # - `SHUFFLE_SIZE`: the amount of shuffle data.
        # - `PEAK_MEMORY`: the peak memory consumption.
        # - `SCAN_SIZE`: the amount of scanned data.
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # Sorts the query results by a specified field. The value is a JSON array string, such as `[{"Field":"Time2SumValue","Type":"Desc"}]`. The array can contain only one object. Parameters:
        # 
        # - `Field`: the sort field. This parameter is case-sensitive. Valid values:
        #     - NEW report: `Time2SumValue`, `Time2AvgValue`, `Time2MaxValue`.
        #     - CHANGED report: `AvgChangeRatePercent`, `AvgTime1Value`, `AvgTime2Value`, `SumChangeRatePercent`, `SumTime1Value`, `SumTime2Value`, `MaxChangeRatePercent`, `MaxTime1Value`, `MaxTime2Value`.
        #     - All report types and analysis metrics: `AvgRt`, `MaxRt`.
        #     - `QUERY_COUNT`: `TotalQueryTime`.
        #     - `CPU_COST`: `QueryCount`, `AvgPlanningTime`, `MaxPlanningTime`, `AvgExecutionTime`, `MaxExecutionTime`.
        #     - `SHUFFLE_SIZE`, `PEAK_MEMORY`: `QueryCount`.
        #     - `SCAN_SIZE`: `QueryCount`, `TotalScanCost`.
        # - `Type`: the sort order. This parameter is case-insensitive. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        # 
        # > - NEW reports are sorted by `Time2SumValue` in descending order by default.
        # > - CHANGED reports are sorted by `AvgChangeRatePercent` in descending order by default.
        # > - The value of `Field` must be applicable to the current report type and `MetricType`.
        self.order = order
        # The page number. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SQL Pattern comparison report.
        # 
        # This parameter is required.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_rate is not None:
            result['ChangeRate'] = self.change_rate

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.include_pattern is not None:
            result['IncludePattern'] = self.include_pattern

        if self.metric_type is not None:
            result['MetricType'] = self.metric_type

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeRate') is not None:
            self.change_rate = m.get('ChangeRate')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('IncludePattern') is not None:
            self.include_pattern = m.get('IncludePattern')

        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        return self

