# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteMonitorDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        length: int = None,
        metric_name: str = None,
        next_token: str = None,
        period: str = None,
        region_id: str = None,
        start_time: str = None,
        task_id: str = None,
        type: str = None,
    ):
        # The end of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 UTC on Thursday, January 1, 1970.
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format.
        self.end_time = end_time
        # The number of data points to return.
        self.length = length
        # The metric name. Valid values:
        # 
        # *   Availability
        # *   ResponseTime
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The pagination token.
        self.next_token = next_token
        # The statistical period. The value is an integral multiple of 60. Unit: seconds.
        # 
        # >  The default value equals the minimum interval at which detection requests are sent to the monitored address.
        self.period = period
        self.region_id = region_id
        # The start of the time range to query. The following formats are supported:
        # 
        # *   UNIX timestamp: the number of milliseconds that have elapsed since 00:00:00 UTC on Thursday, January 1, 1970.
        # *   UTC time: the UTC time that follows the YYYY-MM-DDThh:mm:ssZ format.
        self.start_time = start_time
        # The job ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The type of the monitored object whose monitoring data is to be queried. Valid values:
        # 
        # *   metric
        # *   event
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

