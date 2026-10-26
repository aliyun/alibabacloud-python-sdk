# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeColdStorageInstanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        engine_type: str = None,
        expire_time: int = None,
        max_results: int = None,
        next_token: str = None,
        object_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        table_name: str = None,
    ):
        # The PolarDB cluster ID.
        self.dbcluster_id = dbcluster_id
        # The name of the database.
        self.dbname = dbname
        # The supported engine types. The return value is the sum of the following engine type values:
        # 
        # - 1: search engine
        # - 2: time series engine
        # - 4: wide table engine
        # - 8: file engine
        # 
        # > For example, if the EngineType value is 15, 15 = 8 + 4 + 2 + 1, which indicates that the instance supports the search engine, time series engine, wide table engine, and file engine. If the EngineType value is 6, 6 = 4 + 2, which indicates that the instance supports the time series engine and wide table engine.
        self.engine_type = engine_type
        # The expiration time of the cluster. Note: A specific value is returned only for clusters whose billing method is Prepaid (subscription). For Postpaid (pay-as-you-go) clusters, a null value is returned.
        self.expire_time = expire_time
        # - If you do not specify the **MaxResults** parameter, batch query is not required. The value of the **MaxResults** parameter returned after the API call indicates the total number of list entries.
        # - If you specify the **MaxResults** parameter, batch query is required. The value of **MaxResults** indicates the number of entries displayed per batch. Valid values: **1** to **100**. The value of the **MaxResults** parameter returned after the API call indicates the number of list entries in the current query batch. Set the **MaxResults** parameter to **20**.
        self.max_results = max_results
        # The query token. Set the value to the NextToken value returned from the previous API call. If there are no more queries, do not specify this parameter.
        self.next_token = next_token
        # The object type. Valid values: TABLE, PARTITION_TABLE, and LOB.
        self.object_type = object_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # > * You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query the region information of all clusters under the target account.
        # * If this parameter is left empty, scheduled tasks in all regions under the current account are queried by default.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the data table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

