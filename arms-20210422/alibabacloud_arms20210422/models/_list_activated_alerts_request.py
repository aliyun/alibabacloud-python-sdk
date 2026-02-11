# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListActivatedAlertsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        filter: str = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.filter = filter
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

