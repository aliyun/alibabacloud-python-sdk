# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EventCenterQueryEventsShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        bus_name: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The request body.
        # 
        # This parameter is required.
        self.body_shrink = body_shrink
        # The name of the event bus.
        self.bus_name = bus_name
        # The number of entries per page. Valid values: 0 to 10000. Default value: 100.
        self.max_results = max_results
        # 用来标记当前开始读取的位置。置空表示从头开始。
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink

        if self.bus_name is not None:
            result['BusName'] = self.bus_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('BusName') is not None:
            self.bus_name = m.get('BusName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

