# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEventSourceRequest(DaraModel):
    def __init__(
        self,
        event_bus_name: str = None,
        event_source_name: str = None,
    ):
        self.event_bus_name = event_bus_name
        # The name of the event source.
        # 
        # This parameter is required.
        self.event_source_name = event_source_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        if self.event_source_name is not None:
            result['EventSourceName'] = self.event_source_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        if m.get('EventSourceName') is not None:
            self.event_source_name = m.get('EventSourceName')

        return self

