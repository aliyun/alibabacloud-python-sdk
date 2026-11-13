# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompleteLifecycleActionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lifecycle_action_result: str = None,
        lifecycle_action_token: str = None,
        lifecycle_hook_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        # Ensures the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the value is unique across different requests. The value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The next action to perform after the wait state of the lifecycle hook ends. Valid values:
        # - CONTINUE: Continues the scale-out activity and adds the ECS instance to the scaling group, or continues the scale-in activity and removes the ECS instance from the scaling group.
        # - ABANDON: Terminates the scale-out activity and releases the created ECS instance, or continues the scale-in activity and removes the ECS instance from the scaling group.
        # - ROLLBACK: Rejects the release of the ECS instance and performs a rollback for a scale-in activity. For a scale-out activity, the effect is the same as ABANDON.
        # 
        # If you do not specify this parameter, the next action after the wait state of the lifecycle hook ends remains the `DefaultResult` value configured for the lifecycle hook.
        # 
        # If multiple lifecycle hooks exist in the scaling group and are triggered simultaneously, the final next action is determined as follows:
        # - For a scale-in activity, when the wait state triggered by an ABANDON or ROLLBACK lifecycle hook ends, the wait states of subsequent lifecycle hooks are ended in advance.
        # - If the lifecycle hook that suspends the scale-in activity is of the CONTINUE type, or for a scale-out activity, subsequent lifecycle hooks continue to suspend the scaling activity until the wait state triggered by the last lifecycle hook ends. The final next action is determined by the type of the last lifecycle hook that ends the wait state.
        self.lifecycle_action_result = lifecycle_action_result
        # The identifier of the wait state for the scaling activity. You can obtain this value from the Message Service (MNS) queue or MNS topic specified by the lifecycle hook.
        # 
        # This parameter is required.
        self.lifecycle_action_token = lifecycle_action_token
        # The ID of the lifecycle hook.
        # 
        # This parameter is required.
        self.lifecycle_hook_id = lifecycle_hook_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.lifecycle_action_result is not None:
            result['LifecycleActionResult'] = self.lifecycle_action_result

        if self.lifecycle_action_token is not None:
            result['LifecycleActionToken'] = self.lifecycle_action_token

        if self.lifecycle_hook_id is not None:
            result['LifecycleHookId'] = self.lifecycle_hook_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('LifecycleActionResult') is not None:
            self.lifecycle_action_result = m.get('LifecycleActionResult')

        if m.get('LifecycleActionToken') is not None:
            self.lifecycle_action_token = m.get('LifecycleActionToken')

        if m.get('LifecycleHookId') is not None:
            self.lifecycle_hook_id = m.get('LifecycleHookId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        return self

