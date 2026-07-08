# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVsTopDomainsByFlowRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        limit: int = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The end time must be later than the start time. The date format follows the ISO 8601 standard and uses UTC.<br>Format: YYYY-MM-DDThh:mm:ssZ<br>
        self.end_time = end_time
        # The maximum number of domain names to return. The default value is 20. Valid values: 1 to 100.
        self.limit = limit
        self.owner_id = owner_id
        # The start of the time range to query. The date format follows the ISO 8601 standard and uses UTC.<br>Format: YYYY-MM-DDThh:mm:ssZ<br>The minimum data granularity is 5 minutes.<br>If you do not specify this parameter, data for the current month is queried.<br><br><br>
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

