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
        # The end of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # > The value must be on the hour or half hour.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity of the query data. Unit: seconds.
        # - Valid values: 300, 3600, 14400, 28800, and 86400.
        # - If you do not specify this parameter or specify an unsupported value, the default value 3600 is used.
        self.interval = interval
        # The ID of the resource group to which the Anti-DDoS Pro and Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: seconds.
        # > The value must be on the hour or half hour.
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

