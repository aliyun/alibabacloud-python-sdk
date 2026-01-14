# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataLiteTopicLagMapValue(DaraModel):
    def __init__(
        self,
        ready_count: int = None,
        delivery_duration: int = None,
    ):
        self.ready_count = ready_count
        self.delivery_duration = delivery_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ready_count is not None:
            result['readyCount'] = self.ready_count

        if self.delivery_duration is not None:
            result['deliveryDuration'] = self.delivery_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('readyCount') is not None:
            self.ready_count = m.get('readyCount')

        if m.get('deliveryDuration') is not None:
            self.delivery_duration = m.get('deliveryDuration')

        return self

