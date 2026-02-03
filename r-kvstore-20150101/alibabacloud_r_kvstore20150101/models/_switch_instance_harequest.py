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
        switch_mode: int = None,
        switch_type: str = None,
    ):
        # The ID of the instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) operation to query the ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the data shard. You can call the [DescribeRoleZoneInfo](https://help.aliyun.com/document_detail/473782.html) operation to obtain the value of the CustinsId parameter. Separate multiple data shard IDs with commas (,). `all` indicates that all data shards are specified.
        # 
        # > This parameter is available and required only for read/write splitting and cluster instances.
        self.node_id = node_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The time when to perform the switchover. Default value: 0. Valid values:
        # 
        # *   **0**: immediately performs the switchover.
        # *   **1**: performs the switchover during the maintenance window.
        # 
        # > You can call the [ModifyInstanceMaintainTime](https://help.aliyun.com/document_detail/473775.html) operation to modify the maintenance window of a Tair (Redis OSS-compatible) instance.
        self.switch_mode = switch_mode
        # The switching mode. Valid values:
        # 
        # *   **AvailablePriority**: immediately performs a switchover by prioritizing availability. No latency of data synchronization between the master and replica nodes is considered. This may cause data loss.
        # *   **ReliabilityPriority**: performs a switchover by prioritizing reliability. Make sure that no latency of data synchronization between the master and replica nodes exists. This ensures data integrity. This mode may cause switchover failures in scenarios where a large volume of data is written and data synchronization latency consistently exists.
        # 
        # >  You must evaluate the requirements for data and services based on your business scenarios and then select a switching mode.
        self.switch_type = switch_type

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

        if self.switch_mode is not None:
            result['SwitchMode'] = self.switch_mode

        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type

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

        if m.get('SwitchMode') is not None:
            self.switch_mode = m.get('SwitchMode')

        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')

        return self

