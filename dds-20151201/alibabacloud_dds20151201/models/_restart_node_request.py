# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestartNodeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_id: str = None,
        switch_mode: str = None,
    ):
        # The instance ID.
        # 
        # > If the instance is a sharded cluster instance, also set the `NodeId` parameter.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the Mongos, shard, or Configserver node in the sharded cluster instance. Call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/62010.html) operation to query the node ID.
        # 
        # > This parameter is required if **DBInstanceId** is set to the ID of a sharded cluster instance.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role ID of the node.
        # 
        # 1. Call the [DescribeReplicaSetRole](https://help.aliyun.com/document_detail/468469.html) operation to query the role ID of a node in a replica set instance.
        # 
        # 2. Call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/468472.html) operation to query the role ID of a node in a sharded cluster instance.
        # 
        # This parameter is required.
        self.role_id = role_id
        # The time to execute the task. Valid values:
        # 
        # - **0**: The task is executed immediately. This is the default value.
        # 
        # - **1**: The task is executed during the maintenance window.
        # 
        # > Call the [ModifyInstanceMaintainTime](https://help.aliyun.com/document_detail/473775.html) operation to modify the maintenance window of the instance.
        self.switch_mode = switch_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        return self

