# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveBaseStrategyPeriodRequest(DaraModel):
    def __init__(
        self,
        entry_id: str = None,
        only_weekdays: bool = None,
        only_workdays: bool = None,
        strategy_level: int = None,
        working_time: List[str] = None,
        working_time_frames_json: str = None,
    ):
        # This parameter is required.
        self.entry_id = entry_id
        self.only_weekdays = only_weekdays
        self.only_workdays = only_workdays
        self.strategy_level = strategy_level
        self.working_time = working_time
        self.working_time_frames_json = working_time_frames_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        if self.only_weekdays is not None:
            result['OnlyWeekdays'] = self.only_weekdays

        if self.only_workdays is not None:
            result['OnlyWorkdays'] = self.only_workdays

        if self.strategy_level is not None:
            result['StrategyLevel'] = self.strategy_level

        if self.working_time is not None:
            result['WorkingTime'] = self.working_time

        if self.working_time_frames_json is not None:
            result['WorkingTimeFramesJson'] = self.working_time_frames_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        if m.get('OnlyWeekdays') is not None:
            self.only_weekdays = m.get('OnlyWeekdays')

        if m.get('OnlyWorkdays') is not None:
            self.only_workdays = m.get('OnlyWorkdays')

        if m.get('StrategyLevel') is not None:
            self.strategy_level = m.get('StrategyLevel')

        if m.get('WorkingTime') is not None:
            self.working_time = m.get('WorkingTime')

        if m.get('WorkingTimeFramesJson') is not None:
            self.working_time_frames_json = m.get('WorkingTimeFramesJson')

        return self

