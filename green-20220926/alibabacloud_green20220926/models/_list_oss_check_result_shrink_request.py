# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOssCheckResultShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        finish_num: int = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        start_date: str = None,
        status: int = None,
    ):
        # Current page number.
        self.current_page = current_page
        # End date.
        self.end_date = end_date
        # Number of completed tasks.
        self.finish_num = finish_num
        # Page size.
        self.page_size = page_size
        # Search condition.
        self.query = query
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort_shrink = sort_shrink
        # Start date.
        self.start_date = start_date
        # Task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.finish_num is not None:
            result['FinishNum'] = self.finish_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('FinishNum') is not None:
            self.finish_num = m.get('FinishNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

