# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComputeJobsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        region_id: str = None,
        search: str = None,
        sort_direction: str = None,
        sort_field: str = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.search = search
        self.sort_direction = sort_direction
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search is not None:
            result['Search'] = self.search

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        return self

