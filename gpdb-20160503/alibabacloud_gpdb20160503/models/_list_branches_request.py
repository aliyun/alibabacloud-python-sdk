# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBranchesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_branch_id: str = None,
        region_id: str = None,
        search: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The maximum number of records to return in this query.
        self.max_results = max_results
        # The pagination token. It is not required for the first query. For subsequent queries, use the NextToken returned from the previous query.
        self.next_token = next_token
        # The page number. The value must be greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of records per page.
        # 
        # Valid values:
        # - 10
        # - 20
        # - 50
        # - 100
        # 
        # Default value: 20.
        self.page_size = page_size
        # The parent branch ID, used to specify the parent branch for a new branch or as a query filter condition.
        self.parent_branch_id = parent_branch_id
        # The region ID. Must be specified when creating a primary branch. When creating a sub-branch, it inherits the region of the primary branch by default.
        self.region_id = region_id
        # The search keyword. Supports fuzzy search by branch ID or branch name.
        self.search = search
        # The sort field.
        # 
        # Valid values:
        # - BranchName: Sort by branch name.
        # - CreateTime: Sort by creation time.
        # - LastRunTime: Sort by last run time.
        # 
        # Default value: CreateTime.
        self.sort_by = sort_by
        # The sort direction.
        # 
        # Valid values:
        # - Asc: Ascending order.
        # - Desc: Descending order.
        # 
        # Default value: Desc.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search is not None:
            result['Search'] = self.search

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Search') is not None:
            self.search = m.get('Search')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

