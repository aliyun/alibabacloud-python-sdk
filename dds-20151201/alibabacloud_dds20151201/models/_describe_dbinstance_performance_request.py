# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancePerformanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        interval: str = None,
        key: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        replica_set_role: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_id: str = None,
        search_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        # 
        # >  If you set this parameter to the ID of a sharded cluster instance, you must also specify the **NodeId** parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The interval at which performance data is collected. Valid values: 5, 30, 60, 600, 1800, 3600, 86400.
        self.interval = interval
        # The performance metric. For more information about valid values, see [Monitoring items and metrics](https://help.aliyun.com/document_detail/216973.html).
        # 
        # >  If you need to specify multiple metrics, separate the metrics with commas (,).
        # 
        # This parameter is required.
        self.key = key
        # The ID of the mongos or shard node in a sharded cluster instance. You can specify this parameter to view the performance data of a single node.
        # 
        # >  This parameter is valid when you set the **DBInstanceId** parameter to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The role of the node in the standalone or replica set instance. Valid values:
        # 
        # *   **Primary**
        # *   **Secondary**
        # 
        # >  *  This parameter is valid only when you specify the **DBInstanceId** parameter to the ID of a standalone instance or a replica set instance.
        # > *  This parameter can be set only to **Primary** when you specify the **DBInstanceId** parameter to the ID of a standalone instance.
        self.replica_set_role = replica_set_role
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role ID of the node in a standalone or replica set instance. You can call the [DescribeReplicaSetRole](https://help.aliyun.com/document_detail/62134.html) operation to query the role ID of the node.
        # 
        # >  This parameter is available when you set the **DBInstanceId** parameter to the ID of a standalone instance or a replica set instance.
        self.role_id = role_id
        self.search_id = search_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.key is not None:
            result['Key'] = self.key

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.search_id is not None:
            result['SearchId'] = self.search_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('SearchId') is not None:
            self.search_id = m.get('SearchId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

