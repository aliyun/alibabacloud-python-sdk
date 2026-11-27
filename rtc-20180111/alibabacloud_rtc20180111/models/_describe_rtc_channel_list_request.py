# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRtcChannelListRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        service_area: str = None,
        sort_type: str = None,
        time_point: str = None,
        user_id: str = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        self.app_id = app_id
        # The channel ID. Only a single ID is supported.
        self.channel_id = channel_id
        self.owner_id = owner_id
        # The page number. Valid values: greater than **0**. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Valid values: greater than **0**. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The service area. By default, all areas are queried. Valid values:
        # 
        # - **cn**: China.
        # 
        # - **us**: United States.
        self.service_area = service_area
        # The sort order. By default, the records are sorted in descending order of StartTime.
        self.sort_type = sort_type
        # The query time in UTC. The format is yyyy-MM-ddTHH:mm:ssZ. The time granularity is one day.
        # 
        # This parameter is required.
        self.time_point = time_point
        # The user ID. Only a single ID is supported.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.service_area is not None:
            result['ServiceArea'] = self.service_area

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServiceArea') is not None:
            self.service_area = m.get('ServiceArea')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

