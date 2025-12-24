# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecordLifecycleActionHeartbeatRequest(DaraModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        heartbeat_timeout: int = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The time window during which the ECS instance stays in a Pending state. When the time window ends, Auto Scaling executes the default action. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call this operation to extend the time window during which the ECS instance stays in a Pending state. You can also call the [CompleteLifecycleAction](https://help.aliyun.com/document_detail/459335.html) operation to remove the ECS instance from the Pending state ahead of schedule.
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The action token of the lifecycle hook. You can obtain the token from the details page of the Simple Message Queue (SMQ, formerly MNS) queue specified for the lifecycle hook.
        # 
        # You can also call the [DescribeLifecycleActions](https://help.aliyun.com/document_detail/459333.html) operation to obtain the action token of the lifecycle hook.
        # 
        # If you specified an SMQ topic for the lifecycle hook, you can obtain the token from the MNS topic.
        # 
        # This parameter is required.
        self.lifecycle_action_token = lifecycle_action_token
        # The ID of the lifecycle hook.
        # 
        # This parameter is required.
        self.lifecycle_hook_id = lifecycle_hook_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.heartbeat_timeout is not None:
            result['heartbeatTimeout'] = self.heartbeat_timeout

        if self.lifecycle_action_token is not None:
            result['lifecycleActionToken'] = self.lifecycle_action_token

        if self.lifecycle_hook_id is not None:
            result['lifecycleHookId'] = self.lifecycle_hook_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('heartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('heartbeatTimeout')

        if m.get('lifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('lifecycleActionToken')

        if m.get('lifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('lifecycleHookId')

        return self

