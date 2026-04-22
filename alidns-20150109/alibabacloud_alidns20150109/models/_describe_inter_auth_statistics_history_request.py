# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInterAuthStatisticsHistoryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_timestamp: int = None,
        rcode: str = None,
        server_region: str = None,
        start_timestamp: int = None,
        statistical_type: str = None,
        zone_name: str = None,
    ):
        self.domain_name = domain_name
        self.end_timestamp = end_timestamp
        self.rcode = rcode
        self.server_region = server_region
        self.start_timestamp = start_timestamp
        self.statistical_type = statistical_type
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.rcode is not None:
            result['Rcode'] = self.rcode

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.statistical_type is not None:
            result['StatisticalType'] = self.statistical_type

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Rcode') is not None:
            self.rcode = m.get('Rcode')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('StatisticalType') is not None:
            self.statistical_type = m.get('StatisticalType')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

