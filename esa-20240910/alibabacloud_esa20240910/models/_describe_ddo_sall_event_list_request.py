# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDoSAllEventListRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        event_type: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
        start_time: str = None,
    ):
        # The end time of the query.
        # 
        # The time must be in ISO 8601 format and in UTC. Format: `yyyy-MM-ddTHH:mm:ssZ`. The time range between `StartTime` and `EndTime` cannot exceed 31 days.
        # 
        # If this parameter is not specified, it defaults to the current time.
        self.end_time = end_time
        # The type of DDoS attack events to query. Valid values:
        # 
        # - **web-cc**: A web resource exhaustion attack.
        # 
        # - **cc**: A connection-based attack.
        # 
        # - **traffic**: A traffic-based attack.
        # 
        # If you do not specify this parameter, the operation queries `web-cc` events by default.
        self.event_type = event_type
        # The page number to return. Valid range: **1** to **100000**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. Valid values: **5**, **10**, and **20**.
        self.page_size = page_size
        # The ID of the site. You can obtain this ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The start time of the query.
        # 
        # The time must be in ISO 8601 format and in UTC. Format: `yyyy-MM-ddTHH:mm:ssZ`.
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

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

