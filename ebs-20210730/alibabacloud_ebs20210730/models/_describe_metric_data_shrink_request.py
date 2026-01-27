# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricDataShrinkRequest(DaraModel):
    def __init__(
        self,
        aggre_ops: str = None,
        aggre_over_line_ops: str = None,
        dimensions: str = None,
        end_time: str = None,
        group_by_labels_shrink: str = None,
        metric_name: str = None,
        period: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # Aggregation method over time. Possible values include:
        # 
        # - SUM_OVER_TIME
        # - COUNT_OVER_TIME
        # - AVG_OVER_TIME
        # - MAX_OVER_TIME
        # - MIN_OVER_TIME
        # - SUM_OVER_TIME_LCRO: Sum over a left-closed, right-open interval
        # - AVG_OVER_TIME_LCRO: Average over a left-closed, right-open interval
        # - SUM_OVER_TIME_LORC: Sum over a left-open, right-closed interval
        # - AVG_OVER_TIME_LORC: Average over a left-open, right-closed interval
        self.aggre_ops = aggre_ops
        # Aggregation method between lines. Possible values include:
        # - NON: No aggregation
        # - SUM: Sum
        # - AVG: Average
        # - COUNT: Count
        # - MAX: Maximum
        # - MIN: Minimum
        self.aggre_over_line_ops = aggre_over_line_ops
        # The dimension map, in the JSON format. Valid values:
        # 
        # *   DiskId: the disk name. Example: d-xxx.
        # *   DeviceType: the disk type. system indicates the system disk, and data indicates the data disk.
        # *   DeviceCategory: the disk category. Example: cloud_essd.
        # *   EcsInstanceId: the ECS instance name. Example: i-xxx.
        # *   Azone: the zone, such as cn-hangzhou-a.
        # 
        # The returned result is the intersection of all dimension filtering conditions.
        self.dimensions = dimensions
        # The end time point for obtaining metric data. It should not be later than the current moment. Represented according to the ISO 8601 standard, using UTC +0 time, in the format yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # The list of fields used for grouping and aggregation.
        self.group_by_labels_shrink = group_by_labels_shrink
        # Metric name. Possible values include:
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
        # The granularity at which data is collected for the metric. Unit: seconds. Default value: 5. Valid values:
        # 
        # *   5: 5 seconds. The query time range can be up to 12 hours.
        # *   10: 10 seconds. The query time range can be up to 24 hours.
        # *   60: 60 seconds. The query time range can be up to 7 days.
        # *   300: 300 seconds. The query time range can be up to 30 days.
        # *   600: 600 seconds. The query time range can be up to 30 days.
        # *   3600: 3,600 seconds. The query time range can be up to 30 days.
        self.period = period
        # Region ID.
        self.region_id = region_id
        # The beginning of the time range to query. You can specify a point in time that is up to 30 days before the current time. If both StartTime and EndTime are left empty, the monitoring metric data of the most recent statistical period is queried. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.group_by_labels_shrink is not None:
            result['GroupByLabels'] = self.group_by_labels_shrink

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
            self.group_by_labels_shrink = m.get('GroupByLabels')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

