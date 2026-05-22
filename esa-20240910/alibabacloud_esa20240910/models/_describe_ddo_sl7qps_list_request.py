# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSL7QpsListRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: int = None,
        record_id: int = None,
        site_id: int = None,
        start_time: str = None,
    ):
        # The end time of the query.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ. The maximum span between the start and end times is 31 days.
        # 
        # If this parameter is not set, the current time will be used as the end time of the query.
        self.end_time = end_time
        # The time granularity of the queried data, in seconds.
        # 
        # Depending on the maximum time span of a single query, this parameter supports values of 60 (1 minute), 300 (5 minutes), 1800 (half an hour), and 3600 (1 hour).
        # 
        # This parameter is required.
        self.interval = interval
        # Record ID, which can be obtained by calling the [ListRecords](~~ListRecords~~) interface.
        self.record_id = record_id
        # Site ID, which can be obtained by calling the [ListSites](~~ListSites~~) interface.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The start time of the query.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

