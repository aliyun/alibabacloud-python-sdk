# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStatsEventRecordsRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        level: str = None,
        status: str = None,
    ):
        self.event_type = event_type
        self.level = level
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['eventType'] = self.event_type

        if self.level is not None:
            result['level'] = self.level

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventType') is not None:
            self.event_type = m.get('eventType')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

