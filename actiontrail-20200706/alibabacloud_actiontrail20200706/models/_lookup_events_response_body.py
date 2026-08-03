# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class LookupEventsResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        events: List[Dict[str, Any]] = None,
        next_token: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range of the retrieved events.
        self.end_time = end_time
        # The list of retrieved events.
        self.events = events
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        # 
        # > If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The start of the time range of the retrieved events.
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

        if self.events is not None:
            result['Events'] = self.events

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Events') is not None:
            self.events = m.get('Events')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

