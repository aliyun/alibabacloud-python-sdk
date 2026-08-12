# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SlsNamedQueryEntry(DaraModel):
    def __init__(
        self,
        end: int = None,
        expr: str = None,
        start: int = None,
        time_unit: str = None,
        window: int = None,
    ):
        # The end offset of the time range. This parameter is mutually exclusive with window.
        self.end = end
        # The SPL query expression.
        self.expr = expr
        # The start offset of the time range. This parameter is mutually exclusive with window.
        self.start = start
        # The time unit. Valid values: day, hour, minute, and second.
        self.time_unit = time_unit
        # The snap window size. This parameter is mutually exclusive with start and end.
        self.window = window

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['end'] = self.end

        if self.expr is not None:
            result['expr'] = self.expr

        if self.start is not None:
            result['start'] = self.start

        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit

        if self.window is not None:
            result['window'] = self.window

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('expr') is not None:
            self.expr = m.get('expr')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')

        if m.get('window') is not None:
            self.window = m.get('window')

        return self

