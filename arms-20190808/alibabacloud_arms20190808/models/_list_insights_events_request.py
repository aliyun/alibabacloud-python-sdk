# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInsightsEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        insights_types: str = None,
        pid: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The value is a timestamp.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The types of the events that you want to query. Separate multiple event types with commas (,). If you do not specify this parameter, all events are queried.
        # 
        # *   errorIncrease: API error-rate spike events. Examples: HTTP API error-rate spike events and Dubbo API error-rate spike events.
        # *   topErrorIncrease: the top five API error-rate spike events with the highest traffic.
        # *   topRtIncrease: API response-time spike events. Examples: HTTP API response-time spike events and Dubbo API response-time spike events.
        # *   rtIncrease: the top five API response-time spike events with the highest traffic.
        self.insights_types = insights_types
        # The ID of the application.
        self.pid = pid
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start of the time range to query. The value is a timestamp.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.insights_types is not None:
            result['InsightsTypes'] = self.insights_types

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InsightsTypes') is not None:
            self.insights_types = m.get('InsightsTypes')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

