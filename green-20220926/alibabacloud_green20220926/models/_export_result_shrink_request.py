# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportResultShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        page_size: int = None,
        query: str = None,
        region_id: str = None,
        sort_shrink: str = None,
        source: str = None,
        start_date: str = None,
    ):
        # Page number of the query result. Default is 1.
        self.current_page = current_page
        # End date.
        self.end_date = end_date
        # Number of items per page in the query result.
        self.page_size = page_size
        # Query condition.
        self.query = query
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort_shrink = sort_shrink
        # Operation source.
        self.source = source
        # Start date.
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

        if self.query is not None:
            result['Query'] = self.query

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.source is not None:
            result['Source'] = self.source

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
            self.query = m.get('Query')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

