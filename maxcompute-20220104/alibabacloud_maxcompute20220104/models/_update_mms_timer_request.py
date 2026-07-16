# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMmsTimerRequest(DaraModel):
    def __init__(
        self,
        schedule_type: str = None,
        stopped: bool = None,
        value: str = None,
    ):
        self.schedule_type = schedule_type
        self.stopped = stopped
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_type is not None:
            result['scheduleType'] = self.schedule_type

        if self.stopped is not None:
            result['stopped'] = self.stopped

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

