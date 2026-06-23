# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBClusterPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The end of the time range to query. Specify the time in UTC using the `yyyy-MM-ddTHH:mmZ` format.
        # 
        # > The end time must be later than the start time. The maximum time range cannot exceed 32 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The performance metrics that you want to query. Separate multiple metric names with a comma (,). You can query up to five performance metrics at a time. The following performance metrics are supported:
        # 
        # > **Key** is required.
        # 
        # - **CPU**:
        # 
        #   - **CPU_USAGE**: The CPU utilization.
        # 
        # - **Memory**:
        # 
        #   - **MEM_USAGE**: The memory utilization.
        # 
        #   - **MEM_USAGE_SIZE**: The memory usage in MB.
        # 
        # - **Disk**:
        # 
        #   - **DISK_USAGE**: The disk utilization.
        # 
        #   - **DISK_USAGE_SIZE**: The disk usage in MB.
        # 
        #   - **IOPS**: The disk input/output operations per second (IOPS).
        # 
        # - **Connection**:
        # 
        #   - **CONN_USAGE**: The database connection utilization.
        # 
        #   - **CONN_USAGE_COUNT**: The number of database connections.
        # 
        # - **Write**:
        # 
        #   - **TPS**: The number of rows written per second (TPS).
        # 
        #   - **INSERT_SIZE**: The write size per second in MB.
        # 
        # - **Query**:
        # 
        #   - **QPS**: The queries per second (QPS).
        # 
        #   - **AVG_SEEK**: The number of random SEEK calls.
        # 
        # - **WAIT**:
        # 
        #   - **ZK_WAIT**: The average wait time of ZooKeeper (ZK) in ms.
        # 
        #   - **IO_WAIT**: The average I/O wait time in ms.
        # 
        #   - **CPU_WAIT**: The average CPU wait time in ms.
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. Specify the time in UTC using the `yyyy-MM-ddTHH:mmZ` format.
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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

