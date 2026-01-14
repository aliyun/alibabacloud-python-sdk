# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataTopicLagMapValue(DaraModel):
    def __init__(
        self,
        ready_count: int = None,
        inflight_count: int = None,
        delivery_duration: int = None,
        last_consume_timestamp: int = None,
    ):
        # Ready message count
        self.ready_count = ready_count
        # The number of messages being consumed.
        self.inflight_count = inflight_count
        # Delivery delay time, in seconds
        self.delivery_duration = delivery_duration
        # lastConsumeTimestamp
        self.last_consume_timestamp = last_consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ready_count is not None:
            result['readyCount'] = self.ready_count

        if self.inflight_count is not None:
            result['inflightCount'] = self.inflight_count

        if self.delivery_duration is not None:
            result['deliveryDuration'] = self.delivery_duration

        if self.last_consume_timestamp is not None:
            result['lastConsumeTimestamp'] = self.last_consume_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('readyCount') is not None:
            self.ready_count = m.get('readyCount')

        if m.get('inflightCount') is not None:
            self.inflight_count = m.get('inflightCount')

        if m.get('deliveryDuration') is not None:
            self.delivery_duration = m.get('deliveryDuration')

        if m.get('lastConsumeTimestamp') is not None:
            self.last_consume_timestamp = m.get('lastConsumeTimestamp')

        return self

