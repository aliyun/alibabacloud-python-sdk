# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRCMetricListRequest(DaraModel):
    def __init__(
        self,
        dimensions: str = None,
        end_time: str = None,
        express: str = None,
        instance_id: str = None,
        length: str = None,
        metric_name: str = None,
        next_token: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.dimensions = dimensions
        # The end of the time range to query. The end time must be later than the start time. Example: `2024-08-06 10:15:00`.
        self.end_time = end_time
        # The reserved parameter.
        self.express = express
        # The instance ID.
        self.instance_id = instance_id
        # The number of entries per page.
        # 
        # Default value: 1000.
        # 
        # >  The maximum value of the Length parameter in a request is 1440.
        self.length = length
        # The metric that you want to use. For more information, see [CloudMonitor metrics](https://cms.console.aliyun.com/metric-meta/acs_ecs_dashboard/ecs).
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The pagination token.
        self.next_token = next_token
        # The statistical period of the monitoring data.
        # 
        # Set the value to 60 or an integer multiple of 60.
        # 
        # Unit: seconds.
        # 
        # Default value: 60.
        self.period = period
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Example: `2024-08-06 10:05:00`.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.express is not None:
            result['Express'] = self.express

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Express') is not None:
            self.express = m.get('Express')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

