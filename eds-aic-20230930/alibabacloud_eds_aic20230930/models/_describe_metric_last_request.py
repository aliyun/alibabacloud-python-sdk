# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeMetricLastRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        end_time: str = None,
        instance_ids: List[str] = None,
        length: str = None,
        metric_names: List[str] = None,
        next_token: str = None,
        period: int = None,
        start_time: str = None,
    ):
        # For instance-level monitoring, specify a list of Cloud Phone instance IDs.
        # 
        # <props="china">
        # 
        # For matrix-level monitoring, specify a list of matrix IDs.
        self.android_instance_ids = android_instance_ids
        # The end time for the query.
        self.end_time = end_time
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The number of monitoring data records to return on each page for a paged query.
        # 
        # The default value is 1000. This means that 1000 monitoring data records are returned per page.
        self.length = length
        # The list of monitoring metrics.
        # 
        # This parameter is required.
        self.metric_names = metric_names
        # The token that marks the start of the current read position. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The statistic period for monitoring data.
        # 
        # Valid values: 60, 900, and 3600.
        # 
        # Unit: seconds.
        self.period = period
        # The start time for the query.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.length is not None:
            result['Length'] = self.length

        if self.metric_names is not None:
            result['MetricNames'] = self.metric_names

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('MetricNames') is not None:
            self.metric_names = m.get('MetricNames')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

