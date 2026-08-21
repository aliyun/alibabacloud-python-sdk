# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodDomainMax95BpsDataRequest(DaraModel):
    def __init__(
        self,
        cycle: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        start_time: str = None,
        time_point: str = None,
    ):
        # The cycle for the 95th percentile bandwidth. Default value: day. Valid values:
        # 
        # - day: queries the 95th percentile bandwidth by day.
        # 
        # - month: queries the 95th percentile bandwidth by month.
        self.cycle = cycle
        # The accelerated domain name to query. If this parameter is left empty, the merged data of all accelerated domain names is returned by default.
        # 
        # 
        # > Batch domain name queries are not supported.
        self.domain_name = domain_name
        # The end time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        self.owner_id = owner_id
        # The start time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The start time point for data retrieval. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

