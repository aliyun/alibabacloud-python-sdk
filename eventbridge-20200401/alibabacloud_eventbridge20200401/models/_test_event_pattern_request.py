# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TestEventPatternRequest(DaraModel):
    def __init__(
        self,
        event: str = None,
        event_pattern: str = None,
    ):
        # The event.
        # 
        # This parameter is required.
        self.event = event
        # The event pattern.
        # 
        # This parameter is required.
        self.event_pattern = event_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.event_pattern is not None:
            result['EventPattern'] = self.event_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventPattern') is not None:
            self.event_pattern = m.get('EventPattern')

        return self

