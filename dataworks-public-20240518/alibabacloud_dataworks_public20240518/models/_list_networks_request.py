# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetworksRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The unique identifier of the general resource group.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The sort fields. Supports fields such as scheduled time and start time. The format is sort field + sort order (Desc/Asc), where Asc can be omitted. Valid values for sort fields:
        # 
        # - Id (Desc/Asc): Network ID
        # - Status (Desc/Asc): Network status
        # - CreateUser (Desc/Asc): Creator
        # - CreateTime (Desc/Asc): Creation time
        # 
        # Default value: CreateTime Asc.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

