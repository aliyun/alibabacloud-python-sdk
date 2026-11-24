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
        # The end time of the query. Format: yyyy-MM-ddTHH:mmZ (UTC time).
        # >The end time must be later than the start time, and the time interval between the start time and the end time cannot exceed 32 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The names of the performance metrics to query. Separate multiple values with commas (,). You can query up to 5 performance metrics at a time. The following performance metrics are supported:
        # >**Key** is required.
        # 
        # - **CPU**:
        #     - **CPU_USAGE**: CPU utilization.
        # - **Memory**:
        #     - **MEM_USAGE**: Memory utilization.
        #     - **MEM_USAGE_SIZE**: Memory usage (unit: MB).
        # - **Disk**:
        #     - **DISK_USAGE**: Disk utilization. 
        #     - **DISK_USAGE_SIZE**: Disk usage (unit: MB).
        #     - **IOPS**: Disk IOPS.
        # - **Connections**:
        #     - **CONN_USAGE**: Database connection utilization.
        #     - **CONN_USAGE_COUNT**: Number of database connections in use.
        # - **Writes**: 
        #     - **TPS**: Number of rows written per second.
        #     - **INSERT_SIZE**: Size of data written per second (unit: MB).
        # - **Queries**: 
        #     - **QPS**: Queries per second (QPS).
        #     - **AVG_SEEK**: Number of random SEEK calls.
        # - **WAIT**: 
        #     - **ZK_WAIT**: Average wait time for ZooKeeper (unit: ms).
        #     - **IO_WAIT**: Average wait time for IO_WAIT (unit: ms).
        #     - **CPU_WAIT**: Average wait time for CPU_WAIT (unit: ms).
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time of the query. Format: yyyy-MM-ddTHH:mmZ (UTC time).
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

