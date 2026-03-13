# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceConfig(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        start_time: int = None,
    ):
        # The name of the Logstore. The trigger periodically subscribes to data from this Logstore and then triggers the function.
        self.logstore = logstore
        # The start time of consumption. Unit: seconds. If you do not specify this parameter, consumption starts from the latest data. If this parameter is specified, a trigger event is generated for data written after the specified time. For consumption of existing data, the trigger interval is ignored to catch up with the consumption delay until the real-time trigger progress is caught up. When the catch-up is complete, the trigger starts to trigger function invocations based on the specified trigger event interval without delay.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

