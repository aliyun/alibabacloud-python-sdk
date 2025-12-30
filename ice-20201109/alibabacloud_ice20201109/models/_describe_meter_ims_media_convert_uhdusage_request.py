# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMeterImsMediaConvertUHDUsageRequest(DaraModel):
    def __init__(
        self,
        end_ts: int = None,
        interval: str = None,
        region_id: str = None,
        start_ts: int = None,
    ):
        # The end of the time range to query. The value is a 10-digit timestamp.
        # 
        # This parameter is required.
        self.end_ts = end_ts
        # The time granularity of the query. Valid values: 3600 (hour) and 86400 (day).
        # 
        # This parameter is required.
        self.interval = interval
        # This parameter does not take effect. By default, the usage data of all regions is returned.
        self.region_id = region_id
        # The beginning of the time range to query. The value is a 10-digit timestamp.
        # 
        # This parameter is required.
        self.start_ts = start_ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        return self

