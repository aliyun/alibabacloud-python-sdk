# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSqlPatternCompareReportsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The number of rows per page for token-based pagination. Valid values: 1 to 100.
        # 
        # Default value: 50.
        # 
        # > - When you use `NextToken` for pagination, keep this parameter unchanged.
        # > - This parameter does not take effect when you use `PageNumber` and `PageSize` for pagination.
        # > - We recommend that you use `PageNumber` and `PageSize` for pagination.
        self.max_results = max_results
        # The token for the next page.
        # 
        # > - Do not specify this parameter for the first query. For subsequent queries, pass in the `NextToken` value returned by the previous query.
        # > - Do not use this parameter together with `PageNumber` or `PageSize`.
        # > - Use `PageNumber` and `PageSize` for pagination.
        self.next_token = next_token
        # Sorts the query results by a specified field. The value is a JSON array string, for example, `[{"Field":"CreatedAt","Type":"Desc"}]`. The array can contain only one object. Fields:
        # 
        # - `Field`: the field by which to sort. Valid values:
        #     - `CreatedAt`: the time when the report was created.
        #     - `StartTime`: the start time of time range 1.
        #     - `CompareStartTime`: the start time of time range 2.
        # - `Type`: the sort order. This value is case-insensitive. Valid values:
        #     - `Asc`: ascending order.
        #     - `Desc`: descending order.
        # 
        # > If you do not specify this parameter, the results are sorted by `CreatedAt` in descending order by default.
        self.order = order
        # The page number. Pages start from 1.
        # 
        # Default value: 1.
        # 
        # > Use this parameter together with `PageSize`. If you specify this parameter, `NextToken` must be empty.
        self.page_number = page_number
        # The number of rows per page. Valid values: 1 to 100.
        # 
        # Default value: 50.
        # 
        # > Use this parameter together with `PageNumber`. If you specify this parameter, `NextToken` must be empty.
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

