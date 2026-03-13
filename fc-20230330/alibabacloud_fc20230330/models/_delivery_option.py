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
        # The maximum number of concurrent events that can be delivered by the upstream event source to Function Compute. This parameter is valid only when ApsaraMQ for Kafka is used as the event source.
        self.concurrency = concurrency
        # The format of each data element in the event parameter of the function. CloudEvents: describes event data in a common format, including event description and event payload data. CloudEvents is designed to simplify event declaration and transmission between different services and platforms. This is the default value. RawData: delivers only the event payload data and does not include other metadata information in the CloudEvents format.
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

