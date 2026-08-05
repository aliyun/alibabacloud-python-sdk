# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOfflineTaskErrorLogsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end timestamp in seconds. If not specified, the current time is used by default.
        self.end_time = end_time
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The start timestamp in seconds. If not specified, the time one hour before the current time is used by default.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

