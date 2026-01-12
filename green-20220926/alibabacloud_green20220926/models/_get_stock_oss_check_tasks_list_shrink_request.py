# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStockOssCheckTasksListShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        is_inc: bool = None,
        media_type: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_time: str = None,
        task_type: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # End time.
        self.end_time = end_time
        # Whether it is a scheduled scan task.
        self.is_inc = is_inc
        # Media type.
        self.media_type = media_type
        # Page size.
        self.page_size = page_size
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort_shrink = sort_shrink
        # Start time.
        self.start_time = start_time
        # Task type.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.is_inc is not None:
            result['IsInc'] = self.is_inc

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IsInc') is not None:
            self.is_inc = m.get('IsInc')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

