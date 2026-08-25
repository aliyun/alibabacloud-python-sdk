# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutesRequest(DaraModel):
    def __init__(
        self,
        network_id: int = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: str = None,
    ):
        # The ID of the network resource.
        self.network_id = network_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The unique identifier of the general quota.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The list of sort fields. Fields such as scheduled time and start time are supported. The format is "sort field + sort order (Desc/Asc)" (Asc is the default if omitted). Valid values:
        # 
        # - Id (Desc/Asc): route ID
        # - DestinationCidr (Desc/Asc): destination CIDR
        # - CreateTime (Desc/Asc): creation time
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
        if self.network_id is not None:
            result['NetworkId'] = self.network_id

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
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

