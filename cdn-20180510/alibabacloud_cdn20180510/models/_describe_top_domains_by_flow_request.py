# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTopDomainsByFlowRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The maximum number of domain names to query. Valid values: **1** to **100**. Default value: **20**.
        self.limit = limit
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The value of StartTime must be in UTC. For example, if the local time is 00:00 on June 1, 2021, set StartTime to 2021-05-31T16:00:00Z.
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

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

