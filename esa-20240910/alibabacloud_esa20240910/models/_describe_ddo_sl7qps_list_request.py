# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSL7QpsListRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        record_id: int = None,
        site_id: int = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        # This parameter is required.
        self.interval = interval
        self.record_id = record_id
        # This parameter is required.
        self.site_id = site_id
        # This parameter is required.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

