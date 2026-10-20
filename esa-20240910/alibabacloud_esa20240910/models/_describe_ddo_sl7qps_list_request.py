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
        # The end time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. The time span between the start time and the end time cannot exceed 31 days. If you do not specify this parameter, the current time is used as the end time.
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values: 60 (1 minute), 300 (5 minutes), 1800 (30 minutes), and 3600 (1 hour). The supported values vary based on the maximum time span of a single query.
        # 
        # This parameter is required.
        self.interval = interval
        # The record ID. You can call the [ListRecords](~~ListRecords~~) operation to obtain the record ID.
        self.record_id = record_id
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The start time of the query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

