# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOriginPoolsRequest(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        name: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        site_id: int = None,
    ):
        # The match type for name-based queries. Valid values:
        # - fuzzy: fuzzy search.
        # - exact: exact search.
        # Default value: exact.
        self.match_type = match_type
        # The name of the origin address pool.
        self.name = name
        # The sort order. Supports ascending or descending order by ID. The ID is positively correlated with the creation time. Default value: descending order by ID. Valid values:
        # - id: descending order by ID.
        # - id: ascending order by ID.
        self.order_by = order_by
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. The value must be a positive integer. Maximum value: 500. If the value exceeds 500, it is reset to 500.
        self.page_size = page_size
        # The site ID. You can call the [ListSites](~~ListSites~~) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.name is not None:
            result['Name'] = self.name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

