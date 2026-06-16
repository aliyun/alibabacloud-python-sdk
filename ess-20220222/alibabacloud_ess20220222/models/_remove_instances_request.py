# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class RemoveInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        decrease_desired_capacity: bool = None,
        ignore_invalid_instance: bool = None,
        instance_ids: List[str] = None,
        lifecycle_hook_context: main_models.RemoveInstancesRequestLifecycleHookContext = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_policy: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        stop_instance_timeout: int = None,
    ):
        # A client-generated token to ensure request idempotence. This token must be unique for each request, contain only ASCII characters, and not exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to decrease the desired capacity of the scaling group. Valid values:
        # 
        # - `true`: Decreases the desired capacity of the scaling group by the number of removed instances.
        # 
        # - `false`: The desired capacity of the scaling group remains unchanged.
        # 
        # Default value: true.
        self.decrease_desired_capacity = decrease_desired_capacity
        # Specifies whether to ignore invalid instances when you remove multiple instances from a scaling group. Valid values:
        # 
        # - `true`: Invalid instances are ignored. If valid instances are removed while invalid ones are present, the scaling activity status is set to Warning. The invalid instances are listed in the scaling activity details.
        # 
        # - `false`: The request is rejected and an error is returned if it contains any invalid instances.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances to remove.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The context of the lifecycle hook.
        self.lifecycle_hook_context = lifecycle_hook_context
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        # Specifies the action to take on removed ECS instances. Valid values:
        # 
        # - recycle: The ECS instances enter the economical mode.
        # 
        #   > This value takes effect only when the `ScalingPolicy` parameter of the scaling group is set to `recycle`.
        # 
        # - release: The ECS instances are released.
        # 
        # The `ScalingPolicy` parameter of the `CreateScalingGroup` operation specifies the reclamation mode of a scaling group. However, the `RemovePolicy` parameter of the `RemoveInstances` operation determines the action taken when an instance is removed. For example:
        # 
        # - If `ScalingPolicy` is `recycle` and `RemovePolicy` is `recycle`, the ECS instances enter the economical mode.
        # 
        # - If `ScalingPolicy` is `recycle` and `RemovePolicy` is `release`, the ECS instances are released.
        # 
        # - If `ScalingPolicy` is `release` and `RemovePolicy` is `recycle`, the ECS instances are released.
        # 
        # - If `ScalingPolicy` is `release` and `RemovePolicy` is `release`, the ECS instances are released.
        # 
        # Default value: release.
        self.remove_policy = remove_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The timeout period, in seconds, for an ECS instance to stop during a scale-in. Valid values: 30 to 240.
        # 
        # > - By default, this parameter inherits its value from the scaling group, but you can override it when calling the `RemoveInstances` operation.
        # >
        # > - This parameter takes effect only during scale-in events where `RemovePolicy` is set to `release`.
        # >
        # > - If this parameter is set, the system waits for the specified duration for the instance to stop. The scale-in process continues after the timeout expires, regardless of the instance\\"s state.
        # >
        # > - If this parameter is not set, the system waits until the instance stops before continuing the scale-in process. If the instance fails to stop, the scale-in operation is rolled back and fails.
        self.stop_instance_timeout = stop_instance_timeout

    def validate(self):
        if self.lifecycle_hook_context:
            self.lifecycle_hook_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity

        if self.ignore_invalid_instance is not None:
            result['IgnoreInvalidInstance'] = self.ignore_invalid_instance

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lifecycle_hook_context is not None:
            result['LifecycleHookContext'] = self.lifecycle_hook_context.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remove_policy is not None:
            result['RemovePolicy'] = self.remove_policy

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.stop_instance_timeout is not None:
            result['StopInstanceTimeout'] = self.stop_instance_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')

        if m.get('IgnoreInvalidInstance') is not None:
            self.ignore_invalid_instance = m.get('IgnoreInvalidInstance')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LifecycleHookContext') is not None:
            temp_model = main_models.RemoveInstancesRequestLifecycleHookContext()
            self.lifecycle_hook_context = temp_model.from_map(m.get('LifecycleHookContext'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemovePolicy') is not None:
            self.remove_policy = m.get('RemovePolicy')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('StopInstanceTimeout') is not None:
            self.stop_instance_timeout = m.get('StopInstanceTimeout')

        return self

class RemoveInstancesRequestLifecycleHookContext(DaraModel):
    def __init__(
        self,
        disable_lifecycle_hook: bool = None,
        ignored_lifecycle_hook_ids: List[str] = None,
        lifecycle_hook_result: str = None,
    ):
        # Specifies whether to disable all lifecycle hooks for the scaling activity. Valid values:
        # 
        # - `true`: Disables all lifecycle hooks.
        # 
        # - `false`: Does not disable lifecycle hooks.
        self.disable_lifecycle_hook = disable_lifecycle_hook
        # A list of lifecycle hook IDs to ignore for the scaling activity.
        self.ignored_lifecycle_hook_ids = ignored_lifecycle_hook_ids
        self.lifecycle_hook_result = lifecycle_hook_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_lifecycle_hook is not None:
            result['DisableLifecycleHook'] = self.disable_lifecycle_hook

        if self.ignored_lifecycle_hook_ids is not None:
            result['IgnoredLifecycleHookIds'] = self.ignored_lifecycle_hook_ids

        if self.lifecycle_hook_result is not None:
            result['LifecycleHookResult'] = self.lifecycle_hook_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableLifecycleHook') is not None:
            self.disable_lifecycle_hook = m.get('DisableLifecycleHook')

        if m.get('IgnoredLifecycleHookIds') is not None:
            self.ignored_lifecycle_hook_ids = m.get('IgnoredLifecycleHookIds')

        if m.get('LifecycleHookResult') is not None:
            self.lifecycle_hook_result = m.get('LifecycleHookResult')

        return self

