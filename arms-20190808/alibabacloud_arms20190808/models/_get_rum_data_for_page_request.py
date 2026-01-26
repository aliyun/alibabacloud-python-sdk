# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRumDataForPageRequest(DaraModel):
    def __init__(
        self,
        app_group: str = None,
        current_page: int = None,
        end_time: int = None,
        page_size: int = None,
        pid: str = None,
        query: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The group to which the application belongs.
        self.app_group = app_group
        # The page number.
        self.current_page = current_page
        # The beginning of the time range to query. The time is accurate to seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of entries per page.
        self.page_size = page_size
        # The application ID.
        self.pid = pid
        # A query statement that complies with the query syntax of Simple Log Service Logstore. For more information, see the parameters corresponding to this operation on the console page.
        # 
        # This parameter is required.
        self.query = query
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. The time is accurate to seconds.
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
        if self.app_group is not None:
            result['AppGroup'] = self.app_group

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGroup') is not None:
            self.app_group = m.get('AppGroup')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

