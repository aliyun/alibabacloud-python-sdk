# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamsTotalCountRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
        typ: str = None,
    ):
        # The ingest domain or streaming domain. This parameter is required if you want to query data based on domain names. You can specify up to 10 domain names. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The maximum time range for a query is 15 days. The end time must be earlier than the current time. Data of the current day can be queried on the next day.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  You can query data in the last 18 months.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of data that you want to query. If you leave this parameter empty, data is returned by domain name. If you want to query data by UID, specify the UID for this parameter.
        self.typ = typ

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.typ is not None:
            result['Typ'] = self.typ

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Typ') is not None:
            self.typ = m.get('Typ')

        return self

