# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainTopAttackListRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        interval: int = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.interval = interval
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

