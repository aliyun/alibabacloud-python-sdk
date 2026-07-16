# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOperationEventScheduleTimeRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        schedule_time: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')

        return self

