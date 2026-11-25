# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApsActionLogsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        keyword: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        stage: str = None,
        start_time: str = None,
        state: str = None,
        workload_id: str = None,
    ):
        # <props="china">The ID of the cluster. The cluster must be of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition.
        # <props="intl">The ID of the Data Lakehouse Edition cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/454250.html) operation to query the cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end time of the logs. Specify the time in the **yyyy-MM-ddTHH:mmZ** format. The time must be in UTC.
        # 
        # > When you query logs, the end time must be later than the start time, and the time span between the start time and the end time cannot exceed 30 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The keyword for the query. Fuzzy matching is applied during log query.
        self.keyword = keyword
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that is greater than 0 and does not exceed the maximum value of the Integer data type. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # - **30** (default)
        # - **50**
        # - **100**
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/454314.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The task stage. Valid values:
        # 
        # - **StructureMigrate**: Schema migration.
        # - **FullDataSync**: Full data synchronization.
        # - **IncrementalSync**: Incremental data synchronization.
        # 
        # > If you do not specify this parameter, logs of all task stages are queried by default.
        self.stage = stage
        # The start time of the logs. Specify the time in the **yyyy-MM-ddTHH:mmZ** format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The log type. Separate multiple log types with commas (,). Valid values:
        # 
        # - **INFO**: Information.
        # - **WARN**: Warning.
        # - **ERROR**: Error.
        # 
        # > If you do not specify this parameter, logs of all types are queried by default.
        self.state = state
        # The ID of the data link task.
        # 
        # This parameter is required.
        self.workload_id = workload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

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

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.workload_id is not None:
            result['WorkloadId'] = self.workload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

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

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('WorkloadId') is not None:
            self.workload_id = m.get('WorkloadId')

        return self

