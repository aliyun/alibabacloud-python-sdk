# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduleConfigUnified(DaraModel):
    def __init__(
        self,
        interval_secs: int = None,
        type: str = None,
    ):
        # The interval between scheduled runs, in seconds.
        self.interval_secs = interval_secs
        # The type of the schedule.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval_secs is not None:
            result['intervalSecs'] = self.interval_secs

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('intervalSecs') is not None:
            self.interval_secs = m.get('intervalSecs')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

