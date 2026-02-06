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
        # The cycle to query the 95th percentile bandwidth data. Valid values:
        # 
        # *   day (default)
        # *   month
        self.cycle = cycle
        # The domain name to be queried for acceleration. If the parameter is empty, the data merged from all accelerated domain names will be returned by default.
        # 
        # > Batch domain name queries are not supported.
        self.domain_name = domain_name
        # End time point. The date format follows the ISO8601 representation and uses UTC time, in the format yyyy-MM-dd\\"T\\"HH:mm:ssZ.
        self.end_time = end_time
        self.owner_id = owner_id
        # Start time point. The date format follows the ISO8601 representation and uses UTC time, in the format yyyy-MM-dd\\"T\\"HH:mm:ssZ.
        self.start_time = start_time
        # The start time point for getting the data. The date format follows the ISO8601 representation and uses UTC time, in the format yyyy-MM-dd\\"T\\"HH:mm:ssZ.
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

