# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEventBusRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        event_bus_name: str = None,
    ):
        # The description of the event bus.
        self.description = description
        # Indicates whether the request is successful. The value true indicates that the request is successful.
        # 
        # This parameter is required.
        self.event_bus_name = event_bus_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.event_bus_name is not None:
            result['EventBusName'] = self.event_bus_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EventBusName') is not None:
            self.event_bus_name = m.get('EventBusName')

        return self

