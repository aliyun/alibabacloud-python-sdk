# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssUsageDataRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        end_time: str = None,
        period: str = None,
        start_time: str = None,
    ):
        # The name of the logical Object Storage Service (OSS) bucket.
        self.bucket = bucket
        # The end of the time range to query. The time must be in UTC. Format: 2010-01-21T09:50:23Z.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The aggregation granularity. Unit: minutes.
        # 
        # Default value: 5. Valid values: 5 to 1440.
        self.period = period
        # The beginning of the time range to query. The time must be in UTC. Format: 2010-01-21T09:50:23Z.
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
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

