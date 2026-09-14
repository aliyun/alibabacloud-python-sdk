# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMetricDataRequest(DaraModel):
    def __init__(
        self,
        aggre_ops: str = None,
        aggre_over_line_ops: str = None,
        dimensions: str = None,
        end_time: str = None,
        group_by_labels: List[str] = None,
        metric_name: str = None,
        period: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The method for aggregating data over time. Valid values:
        # 
        # - SUM_OVER_TIME
        # - COUNT_OVER_TIME
        # - AVG_OVER_TIME
        # - MAX_OVER_TIME
        # - MIN_OVER_TIME
        # - SUM_OVER_TIME_LCRO: The sum of values in a left-closed, right-open interval.
        # - AVG_OVER_TIME_LCRO: The average of values in a left-closed, right-open interval.
        # - SUM_OVER_TIME_LORC: The sum of values in a left-open, right-closed interval.
        # - AVG_OVER_TIME_LORC: The average of values in a left-open, right-closed interval.
        self.aggre_ops = aggre_ops
        # The method for aggregating data across different lines. Valid values:
        # 
        # - NON: No aggregation is performed.
        # - SUM: The sum of values.
        # - AVG: The average of values.
        # - COUNT: The number of values.
        # - MAX: The maximum value.
        # - MIN: The minimum value.
        self.aggre_over_line_ops = aggre_over_line_ops
        # A map of dimensions in the JSON format. The map specifies the dimensions to query. The following keys are supported:
        # 
        # - DiskId: The disk name, such as d-xxx.
        # - DeviceType: The disk category. \\`system\\` indicates a system disk and \\`data\\` indicates a data disk.
        # - DeviceCategory: The disk type, such as cloud_essd.
        # - EcsInstanceId: The name of the ECS instance to which the disk is attached, such as i-xxx.
        # - Azone: The zone, such as cn-hangzhou-a.
        # 
        # The returned results are the intersection of all specified dimension-based filter conditions.
        self.dimensions = dimensions
        # The end of the time range to query metric data. The time cannot be later than the current time. The time must be in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # A list of fields for grouping and aggregation.
        self.group_by_labels = group_by_labels
        # The name of the metric. Valid values:
        # 
        # - disk_bps_percent
        # - disk_iops_percent
        # - disk_read_block_size
        # - disk_read_bps
        # - disk_read_iops
        # - disk_write_block_size
        # - disk_write_bps
        # - disk_write_iops
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The interval at which to query metric data. Unit: seconds. The default value is 5. Valid values:
        # 
        # - 5: 5-second precision. You can query data within a 12-hour time range.
        # - 10: 10-second precision. You can query data within a 24-hour time range.
        # - 60: 60-second precision. You can query data within a 7-day time range.
        # - 300: 300-second precision. You can query data within a 30-day time range.
        # - 600: 600-second precision. You can query data within a 30-day time range.
        # - 3600: 3600-second precision. You can query data within a 30-day time range.
        self.period = period
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query metric data. The start time can be up to 30 days before the current time. If you leave both the StartTime and EndTime parameters empty, the system queries the metrics for the most recent period. The time must be in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggre_ops is not None:
            result['AggreOps'] = self.aggre_ops

        if self.aggre_over_line_ops is not None:
            result['AggreOverLineOps'] = self.aggre_over_line_ops

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by_labels is not None:
            result['GroupByLabels'] = self.group_by_labels

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggreOps') is not None:
            self.aggre_ops = m.get('AggreOps')

        if m.get('AggreOverLineOps') is not None:
            self.aggre_over_line_ops = m.get('AggreOverLineOps')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupByLabels') is not None:
            self.group_by_labels = m.get('GroupByLabels')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

