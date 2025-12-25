# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateScheduledPreloadExecutionRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: str = None,
        interval: int = None,
        slice_len: int = None,
        start_time: str = None,
    ):
        # The end time of the prefetch plan.
        self.end_time = end_time
        # The ID of the prefetch plan.
        # 
        # This parameter is required.
        self.id = id
        # The time interval between each batch execution. Unit: seconds.
        self.interval = interval
        # The number of URLs prefetched in each batch.
        self.slice_len = slice_len
        # The start time of the prefetch plan.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.slice_len is not None:
            result['SliceLen'] = self.slice_len

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('SliceLen') is not None:
            self.slice_len = m.get('SliceLen')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

