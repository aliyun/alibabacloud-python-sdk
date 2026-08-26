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
        # The ingest domain or streaming domain. This parameter is required when you query domain-level data. You can specify up to 10 domain names in a batch query. Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time. The end time must be later than the start time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        # > The interval between StartTime and EndTime must be within 15 days, and EndTime cannot be later than the current time. Data for the current day can be queried only on the next day.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The start time. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format (UTC).
        # > The maximum query range is the last 1.5 years.
        # 
        # This parameter is required.
        self.start_time = start_time
        # If you leave this parameter empty, domain-level data is queried by default. Set this parameter to aliuid to query UID-level data.
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

