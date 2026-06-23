# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSEventMaxRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        site_id: int = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # The date is in ISO 8601 format. The time is displayed in UTC. The format is yyyy-MM-ddTHH:mm:ssZ. The maximum time span between the start time and end time is 31 days.
        # 
        # If you do not set this parameter, the current time is used as the end time.
        self.end_time = end_time
        # The site ID, which can be obtained by calling the [ListSites](~~ListSites~~) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The beginning of the time range to query.
        # 
        # The date is in ISO 8601 format. The time is displayed in UTC. The format is yyyy-MM-ddTHH:mm:ssZ.
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

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

