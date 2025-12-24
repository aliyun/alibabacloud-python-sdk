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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # The action that you want Auto Scaling to perform after the lifecycle hook times out. Valid values:
        # 
        # *   CONTINUE: Auto Scaling continues to respond to a scale-in or scale-out request.
        # *   ABANDON: Auto Scaling releases Elastic Compute Service (ECS) instances that are created during scale-out activities or removes ECS instances from the scaling group during scale-in activities.
        # *   ROLLBACK: For scale-in activities, Auto Scaling rejects the requests to release ECS instances but rolls back ECS instances. For scale-out activities, the ROLLBACK setting has the same effect as the ABANDON setting.
        # 
        # If you do not specify this parameter, Auto Scaling performs the action that is specified by the `DefaultResult` parameter after the lifecycle hook times out.
        # 
        # If multiple lifecycle hooks exist in a scaling group and the lifecycle hooks are triggered at the same time, the following rules apply:
        # 
        # *   For scale-in activities, when lifecycle hooks whose LifecycleActionResult parameter is set to ABANDON or ROLLBACK time out, other lifecycle hooks time out ahead of schedule.
        # *   For scale-in and scale-out activities, if you set the LifecycleActionResult parameter for all lifecycle hooks to CONTINUE, Auto Scaling performs the next action only after the last lifecycle hook times out. The action that Auto Scaling performs varies based on the value that you specify for the LifecycleActionResult parameter of the lifecycle hook that last times out.
        self.lifecycle_action_result = lifecycle_action_result
        # The token of the lifecycle action. You can obtain the token from the Simple Message Queue (SMQ, formerly MNS) queue or topic that is specified for the lifecycle hook.
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

