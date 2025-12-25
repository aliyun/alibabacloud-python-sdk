# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProcessListRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: str = None,
        query_order: int = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The query ID.
        self.initial_query_id = initial_query_id
        # The user who executes the query statement.
        self.initial_user = initial_user
        # The keyword of the query statement.
        self.keyword = keyword
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The execution duration of slow SQL queries. Minimum value: 1000. Unit: milliseconds.
        self.query_duration_ms = query_duration_ms
        # Specifies the columns by which the query results are sorted in descending order.
        # 
        # *   0: The query results are sorted by the query_duration_ms column.
        # *   1: The query results are sorted by the query_duration_ms and query_start_time columns.
        # *   2: The query results are sorted by the query_duration_ms, query_start_time, and user columns.
        self.query_order = query_order
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id

        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms

        if self.query_order is not None:
            result['QueryOrder'] = self.query_order

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')

        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')

        if m.get('QueryOrder') is not None:
            self.query_order = m.get('QueryOrder')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

