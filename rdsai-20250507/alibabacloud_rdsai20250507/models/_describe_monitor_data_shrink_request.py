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
        self.api_key_name_shrink = api_key_name_shrink
        # This parameter is required.
        self.end_time = end_time
        self.instance_id = instance_id
        self.interval = interval
        # This parameter is required.
        self.metric = metric
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

