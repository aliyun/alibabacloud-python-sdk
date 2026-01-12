# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScanResultShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query_shrink: str = None,
        region_id: str = None,
        resource_type: str = None,
        sort_shrink: str = None,
        start_date: str = None,
    ):
        # Current page.
        self.current_page = current_page
        # End time.
        self.end_date = end_date
        # Page size.
        self.page_size = page_size
        # Search criteria.
        self.query_shrink = query_shrink
        # Region ID.
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Sort fields.
        self.sort_shrink = sort_shrink
        # Start time.
        self.start_date = start_date

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_shrink is not None:
            result['Query'] = self.query_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query_shrink = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

