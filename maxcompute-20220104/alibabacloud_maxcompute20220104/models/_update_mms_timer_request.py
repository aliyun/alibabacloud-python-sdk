# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateMmsTimerRequest(DaraModel):
    def __init__(
        self,
        schedule_type: str = None,
        stopped: bool = None,
        table_black_list: List[str] = None,
        table_white_list: List[str] = None,
        value: str = None,
    ):
        # The scheduling type of the scheduled task.
        self.schedule_type = schedule_type
        # Indicates whether the scheduled task is stopped.
        self.stopped = stopped
        # The tables to exclude when type is set to Database.
        self.table_black_list = table_black_list
        # The tables to migrate when type is set to Database.
        self.table_white_list = table_white_list
        # The scheduling time of the scheduled task. If scheduleType is set to Daily, the value is in the HH:MM format. If scheduleType is set to Hourly, the value is in the MM format.
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

        if self.table_black_list is not None:
            result['tableBlackList'] = self.table_black_list

        if self.table_white_list is not None:
            result['tableWhiteList'] = self.table_white_list

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheduleType') is not None:
            self.schedule_type = m.get('scheduleType')

        if m.get('stopped') is not None:
            self.stopped = m.get('stopped')

        if m.get('tableBlackList') is not None:
            self.table_black_list = m.get('tableBlackList')

        if m.get('tableWhiteList') is not None:
            self.table_white_list = m.get('tableWhiteList')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

