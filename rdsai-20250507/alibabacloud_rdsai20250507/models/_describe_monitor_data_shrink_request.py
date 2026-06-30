# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMonitorDataShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key_name_shrink: str = None,
        end_time: int = None,
        instance_id: str = None,
        interval: int = None,
        metric: str = None,
        start_time: int = None,
    ):
        # The names of the API keys to use for filtering the data. If this parameter is not specified, data from all keys is returned.
        self.api_key_name_shrink = api_key_name_shrink
        # The end of the query time range, specified as a Unix timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The aggregation interval for monitoring data, in seconds. Default: 15.
        self.interval = interval
        # The metric to query. Valid values:
        # 
        # - `pv`
        # 
        # - `uv`
        # 
        # - `qps`
        # 
        # - `success_rate`
        # 
        # - `rt`
        # 
        # - `rate_limited_count`
        # 
        # This parameter is required.
        self.metric = metric
        # The start of the query time range, specified as a Unix timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_name_shrink is not None:
            result['ApiKeyName'] = self.api_key_name_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyName') is not None:
            self.api_key_name_shrink = m.get('ApiKeyName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

