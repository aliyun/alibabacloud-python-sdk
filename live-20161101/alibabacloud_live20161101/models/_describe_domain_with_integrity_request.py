# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainWithIntegrityRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        integrity: float = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The integrity.
        # 
        # This parameter is required.
        self.integrity = integrity
        self.owner_id = owner_id
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard. The time must be in UTC.
        # 
        # This parameter is required.
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

        if self.integrity is not None:
            result['Integrity'] = self.integrity

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

