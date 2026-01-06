# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEventRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_id: str = None,
        event_source: str = None,
    ):
        # The name of the event bus.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name
        # The event ID.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The name of the event source.
        # 
        # *   This parameter is required if you query the system event bus.
        self.event_source = event_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_source is not None:
            result['EventSource'] = self.event_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        return self

