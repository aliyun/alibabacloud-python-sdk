# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTracedEventsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        event_bus_name: str = None,
        event_source: str = None,
        event_type: str = None,
        limit: int = None,
        matched_rule: str = None,
        next_token: str = None,
        start_time: int = None,
        subject: str = None,
    ):
        # The end of the time range when event traces are queried. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The name of the event source.
        self.event_source = event_source
        # The event type.
        self.event_type = event_type
        # The maximum number of entries to return in a request. You can use this parameter and NextToken to implement paging.
        # 
        # >  A maximum of 100 entries can be returned in a request.
        self.limit = limit
        # The name of the event rule that is matched.
        self.matched_rule = matched_rule
        # If you configure Limit and excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The beginning of the time range to query event traces. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.matched_rule is not None:
            result['MatchedRule'] = self.matched_rule

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.subject is not None:
            result['Subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('MatchedRule') is not None:
            self.matched_rule = m.get('MatchedRule')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        return self

