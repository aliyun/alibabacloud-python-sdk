# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeliveryOption(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        event_schema: str = None,
    ):
        self.concurrency = concurrency
        self.event_schema = event_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.event_schema is not None:
            result['eventSchema'] = self.event_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('eventSchema') is not None:
            self.event_schema = m.get('eventSchema')

        return self

