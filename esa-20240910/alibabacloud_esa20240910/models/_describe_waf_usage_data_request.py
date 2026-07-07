# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWafUsageDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        interval: str = None,
        record_name: str = None,
        site_id: int = None,
        split_by: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # >The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity for the query data, in seconds.
        # 
        # The valid values vary based on the time range specified by **StartTime** and **EndTime**:
        # 
        # - Less than 3 days: **300**, **3600**, or **86400**. Default value: **300**.
        # 
        # - 3 to 31 days (excluding 31 days): **3600** or **86400**. Default value: **3600**.
        # 
        # - 31 days or more: **86400**. Default value: **86400**.
        self.interval = interval
        # The domain record name. You can call the [ListSites](~~ListSites~~) operation to obtain the domain record name.
        self.record_name = record_name
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        self.site_id = site_id
        # The grouping key. You can set this parameter to **domain**.
        # 
        # - **domain**: groups the data by domain name.
        self.split_by = split_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
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

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.split_by is not None:
            result['SplitBy'] = self.split_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SplitBy') is not None:
            self.split_by = m.get('SplitBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

