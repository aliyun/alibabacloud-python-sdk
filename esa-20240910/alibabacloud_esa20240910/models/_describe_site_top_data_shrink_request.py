# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteTopDataShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        fields_shrink: str = None,
        interval: str = None,
        limit: str = None,
        site_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The metrics to query.
        # 
        # This parameter is required.
        self.fields_shrink = fields_shrink
        # The time interval between the data entries to return. Unit: seconds.
        self.interval = interval
        # The number of top-ranking data entries to query.
        self.limit = limit
        # The website ID, which can be obtained by calling the [ListSites](~~ListSites~~) operation.
        # 
        # If you do not specify this parameter, the system returns data by account.
        self.site_id = site_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.fields_shrink is not None:
            result['Fields'] = self.fields_shrink

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Fields') is not None:
            self.fields_shrink = m.get('Fields')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

