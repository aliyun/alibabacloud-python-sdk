# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSBpsMaxRequest(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        end_time: str = None,
        site_id: int = None,
        start_time: str = None,
    ):
        # The protection region. If this parameter is not specified, the default value global is used. Valid values:
        # 
        # - domestic: the Chinese mainland.
        # 
        # - overseas: global (excluding the Chinese mainland).
        # 
        # - global: global.
        self.coverage = coverage
        # The end of the time range to query. Specify the time in ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        # 
        # >The end time must be later than the start time.
        self.end_time = end_time
        # The site ID, which can be obtained by calling the [ListSites](url) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The beginning of the time range to query. Specify the time in ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
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
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

