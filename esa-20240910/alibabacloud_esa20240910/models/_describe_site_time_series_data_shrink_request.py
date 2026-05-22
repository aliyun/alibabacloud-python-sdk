# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSiteTimeSeriesDataShrinkRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        fields_shrink: str = None,
        interval: str = None,
        site_id: str = None,
        start_time: str = None,
    ):
        # The end time for obtaining data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0 time, in the format yyyy-MM-ddTHH:mm:ssZ.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # Query metrics.
        # 
        # This parameter is required.
        self.fields_shrink = fields_shrink
        # The time granularity for querying data, in seconds.
        # 
        # Depending on the maximum time span of a single query, this parameter supports values of 60 (1 minute), 300 (5 minutes), 3600 (1 hour), and 86400 (1 day). For details, see the **Supported Query Time Granularities**.
        self.interval = interval
        # Site ID. Obtain the site ID by calling the [ListSites](~~ListSites~~) interface.
        # 
        # If this parameter is empty, user-level data will be queried.
        self.site_id = site_id
        # The start time for obtaining data.
        # 
        # The date format follows ISO8601 notation and uses UTC+0 time, in the format yyyy-MM-ddTHH:mm:ssZ.
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

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

