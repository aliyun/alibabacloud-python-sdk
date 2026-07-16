# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlowLogRecordsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbname: str = None,
        end_time: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sqlhash: str = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query all clusters in the target region and their cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database name.
        self.dbname = dbname
        # The end of the query time range. The end time must be later than the start time. The time range cannot exceed 24 hours. Specify the time in UTC in the `YYYY-MM-DDThh:mmZ` format.
        # 
        # > The time must be in UTC. If your service is in a different time zone, you must convert the time. For example, to query data from 08:00 to 12:00 in the UTC+8 time zone, you must set the time range from 00:00 UTC to 04:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The node ID.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be an integer greater than 0.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of records per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions and their region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The SQL hash of a slow query. Obtain this hash from slow query log statistics to retrieve the details of a specific slow query.
        self.sqlhash = sqlhash
        # The start of the query time range. Specify the time in UTC in the `YYYY-MM-DDThh:mmZ` format.
        # 
        # > - You can query slow query logs from the past 30 days.
        # >
        # > - The time must be in UTC. If your service is in a different time zone, you must convert the time. For example, to query data from 08:00 to 12:00 in the UTC+8 time zone, you must set the time range from 00:00 UTC to 04:00 UTC.
        # 
        # This parameter is required.
        self.start_time = start_time

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

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

        if self.sqlhash is not None:
            result['SQLHASH'] = self.sqlhash

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

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

        if m.get('SQLHASH') is not None:
            self.sqlhash = m.get('SQLHASH')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

