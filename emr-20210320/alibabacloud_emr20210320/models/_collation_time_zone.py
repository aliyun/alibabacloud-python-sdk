# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CollationTimeZone(DaraModel):
    def __init__(
        self,
        current_time_offset: str = None,
        time_zone: str = None,
    ):
        self.current_time_offset = current_time_offset
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_time_offset is not None:
            result['CurrentTimeOffset'] = self.current_time_offset

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentTimeOffset') is not None:
            self.current_time_offset = m.get('CurrentTimeOffset')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

