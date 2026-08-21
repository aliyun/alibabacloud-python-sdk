# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePlayUserTotalRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        # The end time of the query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # > The end time must be later than the start time. The maximum time span between the start time and end time is 180 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The start time of the query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        # 
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

