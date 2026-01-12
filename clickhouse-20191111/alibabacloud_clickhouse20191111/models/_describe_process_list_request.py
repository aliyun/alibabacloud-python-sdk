# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeProcessListRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        initial_query_id: str = None,
        initial_user: str = None,
        keyword: str = None,
        order: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_duration_ms: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to query information about all the clusters that are deployed in a specific region. The information includes the cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the query statement.
        self.initial_query_id = initial_query_id
        # The account that is used to log on to the database.
        self.initial_user = initial_user
        # The keyword that is used to query.
        self.keyword = keyword
        # Sorting by the specified column name. Valid values:
        # 
        # *   elapsed: the cumulative execution time
        # *   written_rows: the number of written rows
        # *   read_rows: the number of read rows
        # *   memory_usage: the memory usage
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return per page. Default value: 30. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The minimum query duration. The minimum value is **1000**, and the default value is **1000**. Unit: milliseconds. Queries that last longer than this duration are returned in response parameters.
        self.query_duration_ms = query_duration_ms
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.initial_query_id is not None:
            result['InitialQueryId'] = self.initial_query_id

        if self.initial_user is not None:
            result['InitialUser'] = self.initial_user

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_duration_ms is not None:
            result['QueryDurationMs'] = self.query_duration_ms

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('InitialQueryId') is not None:
            self.initial_query_id = m.get('InitialQueryId')

        if m.get('InitialUser') is not None:
            self.initial_user = m.get('InitialUser')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDurationMs') is not None:
            self.query_duration_ms = m.get('QueryDurationMs')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

