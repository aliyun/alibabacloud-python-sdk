# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AlertRuleTimeSpan(DaraModel):
    def __init__(
        self,
        day_of_week: List[int] = None,
        end_time: str = None,
        gmt_offset: str = None,
        start_time: str = None,
    ):
        # 每周的星期几
        self.day_of_week = day_of_week
        # 结束时间，格式HH:mm
        self.end_time = end_time
        # 默认北京时间： +0800
        self.gmt_offset = gmt_offset
        # 开始时间，格式HH:mm
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.gmt_offset is not None:
            result['gmtOffset'] = self.gmt_offset

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('gmtOffset') is not None:
            self.gmt_offset = m.get('gmtOffset')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

