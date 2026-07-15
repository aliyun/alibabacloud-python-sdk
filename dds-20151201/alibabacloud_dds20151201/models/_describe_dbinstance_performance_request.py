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
        # > **NodeId** is required when specifying a sharded cluster instance ID
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The data granularity of the performance metrics in seconds. Valid values: 5, 30, 60, 600, 1800, 3600, and 86400.
        self.interval = interval
        # The performance metrics. For more information, see [Metrics](https://help.aliyun.com/document_detail/216973.html).
        # 
        # > To specify multiple metrics, separate them with commas (,).
        # 
        # This parameter is required.
        self.key = key
        # The ID of a mongos or shard node in the sharded cluster instance. This parameter lets you query the performance of a single node.
        # 
        # > Available only when **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The role of a node in a standalone or replica set instance. Valid values:
        # 
        # - **Primary**: The primary node.
        # 
        # - **Secondary**: A secondary node.
        # 
        # > * Available only when **DBInstanceId** is set to the ID of a standalone or replica set instance.
        # >
        # > * If **DBInstanceId** is set to the ID of a standalone instance, this parameter only supports the value **Primary**.
        self.replica_set_role = replica_set_role
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role ID of a node in a standalone or replica set instance. To query the role ID, call the [DescribeReplicaSetRole](https://help.aliyun.com/document_detail/62134.html) operation.
        # 
        # > Available only when **DBInstanceId** is set to the ID of a standalone or replica set instance.
        self.role_id = role_id
        # The Search node ID.
        # 
        # > Available only after the Search feature is enabled for the instance.
        self.search_id = search_id
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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

