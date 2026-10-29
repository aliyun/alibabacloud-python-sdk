# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVsDevicesDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        group_id: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        # The end time of the data to retrieve. The end time must be later than the start time.
        # 
        # > - Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # > - The minimum data granularity is 5 minutes.
        # > - If you do not specify this parameter, the data of the last 24 hours is retrieved by default.
        self.end_time = end_time
        # The workspace ID.
        self.group_id = group_id
        self.owner_id = owner_id
        # The start time of the data to retrieve.    
        # > - Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        # > - The minimum data granularity is 5 minutes.
        # > - If you do not specify this parameter, the data of the last 24 hours is retrieved by default.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

