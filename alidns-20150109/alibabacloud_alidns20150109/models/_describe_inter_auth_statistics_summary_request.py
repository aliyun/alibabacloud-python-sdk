# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInterAuthStatisticsSummaryRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        domain_name: str = None,
        end_timestamp: int = None,
        grow_type: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        period: str = None,
        rcode: str = None,
        server_region: str = None,
        source_type: str = None,
        start_timestamp: int = None,
        statistical_type: str = None,
        zone_name: str = None,
    ):
        self.direction = direction
        self.domain_name = domain_name
        self.end_timestamp = end_timestamp
        self.grow_type = grow_type
        self.order_by = order_by
        self.page_number = page_number
        self.page_size = page_size
        self.period = period
        self.rcode = rcode
        self.server_region = server_region
        self.source_type = source_type
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
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.grow_type is not None:
            result['GrowType'] = self.grow_type

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.period is not None:
            result['Period'] = self.period

        if self.rcode is not None:
            result['Rcode'] = self.rcode

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.statistical_type is not None:
            result['StatisticalType'] = self.statistical_type

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('GrowType') is not None:
            self.grow_type = m.get('GrowType')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Rcode') is not None:
            self.rcode = m.get('Rcode')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('StatisticalType') is not None:
            self.statistical_type = m.get('StatisticalType')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

