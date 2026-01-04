# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlaEventListRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        ip: str = None,
        page: int = None,
        page_size: int = None,
        region: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.ip = ip
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The type of the service Valid values:
        # 
        # *   **cn**: Anti-DDoS Pro
        # *   **cn-hongkong**: Anti-DDoS Premium
        # 
        # This parameter is required.
        self.region = region
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

