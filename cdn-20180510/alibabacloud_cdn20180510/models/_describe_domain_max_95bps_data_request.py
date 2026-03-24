# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainMax95BpsDataRequest(DaraModel):
    def __init__(
        self,
        cycle: str = None,
        domain_name: str = None,
        end_time: str = None,
        start_time: str = None,
        time_point: str = None,
    ):
        # The cycle to query the 95th percentile bandwidth data. Default value: **day**. Valid values:
        # 
        # *   **day**: queries the 95th percentile bandwidth data by day.
        # *   **month**: queries the 95th percentile bandwidth data by month.
        self.cycle = cycle
        # The accelerated domain name. If you do not specify a domain name, data of all domain names is queried.
        # 
        # > You cannot specify multiple domain names in a DescribeDomainMax95BpsData request.
        self.domain_name = domain_name
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

