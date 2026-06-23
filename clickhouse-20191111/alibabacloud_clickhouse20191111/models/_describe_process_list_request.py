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
        # The cluster ID. You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to find information about all clusters in the destination region, including the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ID of the query.
        self.initial_query_id = initial_query_id
        # The database account.
        self.initial_user = initial_user
        # The keyword for the query.
        self.keyword = keyword
        # The column to use for sorting. Valid values:
        # 
        # - elapsed: The total running time.
        # 
        # - written_rows: The number of rows written.
        # 
        # - read_rows: The number of rows read.
        # 
        # - memory_usage: The amount of memory used.
        self.order = order
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values:
        # 
        # - **30** (Default)
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The shortest query duration. The minimum value is **1000**. The default value is **1000**. The unit is milliseconds. The response returns queries that run longer than this duration.
        self.query_duration_ms = query_duration_ms
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/170875.html) operation to find the region ID.
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

