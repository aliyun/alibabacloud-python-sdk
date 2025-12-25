# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCalendarRequest(DaraModel):
    def __init__(
        self,
        calendar_name: str = None,
        cluster_id: str = None,
        year: int = None,
    ):
        # This parameter is required.
        self.calendar_name = calendar_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calendar_name is not None:
            result['CalendarName'] = self.calendar_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalendarName') is not None:
            self.calendar_name = m.get('CalendarName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

