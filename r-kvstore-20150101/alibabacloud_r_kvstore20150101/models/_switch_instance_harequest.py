# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchInstanceHARequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        source_node_id: str = None,
        switch_mode: int = None,
        switch_type: str = None,
        target_node_id: str = None,
        target_shard_name: str = None,
    ):
        # The instance ID. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data shard node. You can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/473782.html) operation to obtain the CustinsId parameter. Separate multiple data shard node IDs with commas (,). To specify all nodes, enter `all`.
        # > This parameter is available and required only when the instance uses the cluster or read/write splitting architecture.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The ID of the original primary node of the shard.
        self.source_node_id = source_node_id
        # The execution time. Valid values:
        # * **0**: executes the operation immediately. This is the default value.
        # * **1**: executes the operation within the maintenance window.
        # 
        # > You can call the [ModifyInstanceMaintainTime](https://help.aliyun.com/document_detail/473775.html) operation to modify the maintenance window of the instance.
        self.switch_mode = switch_mode
        # The switchover mode. Valid values:
        # * **ReliabilityPriority** (default): prioritizes reliability. The primary/secondary switchover is performed only when there is no synchronization latency between the primary and secondary nodes, ensuring no data loss. In scenarios with a large write volume and continuous synchronization latency, this mode may cause the switchover to fail.
        # * **AvailablePriority**: prioritizes availability. The primary/secondary switchover is performed immediately regardless of the synchronization latency between the primary and secondary nodes, which may result in a small amount of data loss.
        # 
        # > Select a switchover mode based on your business requirements for data and services.
        self.switch_type = switch_type
        # The ID of the target primary node after the switchover.
        self.target_node_id = target_node_id
        # The name of the instance shard.
        self.target_shard_name = target_shard_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_node_id is not None:
            result['SourceNodeId'] = self.source_node_id

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

        if self.target_node_id is not None:
            result['TargetNodeId'] = self.target_node_id

        if self.target_shard_name is not None:
            result['TargetShardName'] = self.target_shard_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

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

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceNodeId') is not None:
            self.source_node_id = m.get('SourceNodeId')

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        if m.get('TargetNodeId') is not None:
            self.target_node_id = m.get('TargetNodeId')

        if m.get('TargetShardName') is not None:
            self.target_shard_name = m.get('TargetShardName')

        return self

