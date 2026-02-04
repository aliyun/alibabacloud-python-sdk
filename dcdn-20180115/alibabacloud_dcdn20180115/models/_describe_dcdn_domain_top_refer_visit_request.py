# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainTopReferVisitRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The sorting order. Valid values:
        # 
        # *   **traf**: by network traffic
        # *   **pv**: by the number of visits
        # 
        # Default value: **pv**.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # To query the data on a specified day, use the yyyy-MM-ddT16:00:00Z format.
        # 
        # If you do not set this parameter, data collected within the last 24 hours is queried.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

