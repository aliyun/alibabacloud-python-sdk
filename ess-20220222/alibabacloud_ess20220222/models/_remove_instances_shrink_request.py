# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        decrease_desired_capacity: bool = None,
        ignore_invalid_instance: bool = None,
        instance_ids: List[str] = None,
        lifecycle_hook_context_shrink: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        remove_policy: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        stop_instance_timeout: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to adjust the expected number of ECS instances in the scaling group. Valid values:
        # 
        # *   true: After ECS instances are removed from the scaling group, the expected number of ECS instances in the scaling group decreases.
        # *   false: After ECS instances are removed from the scaling group, the expected number of ECS instances in the scaling group remains unchanged.
        # 
        # Default value: true.
        self.decrease_desired_capacity = decrease_desired_capacity
        # Specifies whether to ignore invalid instances when you remove a batch of instances from the scaling group. Valid values:
        # 
        # *   true: ignores invalid instances. If invalid instances exist and valid instances are deleted, the corresponding scaling activity enters the Warning state. You can check the scaling activity details to view the invalid instances that are ignored.
        # *   false: does not ignore invalid instances. If invalid instances exist in the batch of instances that you want to remove from the scaling group, an error is reported.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances that you want to remove from the scaling group.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The context of the lifecycle hook.
        self.lifecycle_hook_context_shrink = lifecycle_hook_context_shrink
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        # The action subsequent to the removal of the Elastic Compute Service (ECS) instances. Valid values:
        # 
        # *   recycle: The ECS instances enter the Economical Mode.
        # 
        #     **
        # 
        #     **Note** This setting is applicable only if you set `ScalingPolicy` to `recycle`.
        # 
        # *   release: The ECS instances are released.
        # 
        # ScalingPolicy of the CreateScalingGroup operation specifies the reclaim mode of the scaling group while RemovePolicy of the RemoveInstances operation specifies the subsequent action when an ECS instance is removed from the scaling group. Examples:
        # 
        # *   If you set ScalingPolicy and RemovePolicy to recycle, the ECS instances enter the Economical Mode when they are removed.
        # *   If you set ScalingPolicy to recycle and RemovePolicy to release, the ECS instances are released when they are removed.
        # *   If you set ScalingPolicy to release and RemovePolicy to recycle, the ECS instances are released when they are removed.
        # *   If you set ScalingPolicy and RemovePolicy to release, the ECS instances are released when they are removed.
        # 
        # Default value: release.
        self.remove_policy = remove_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The period of time required by the ECS instance to enter the Stopped state. Unit: seconds. Valid values: 30 to 240.
        # 
        # > 
        # 
        # *   By default, this parameter inherits the value of StopInstanceTimeout specified in the CreateScalingGroup or ModifyScalingGroup operation. You can also specify a different value for this parameter in the RemoveInstances operation.
        # 
        # *   This parameter takes effect only if you set RemovePolicy to release.
        # 
        # *   If you specify this parameter, the system waits for the ECS instance to enter the Stopped state only for up to the specified period of time before continuing with the scale-in operation, regardless of the status of the ECS instance.
        # 
        # *   If you do not specify this parameter, the system continues with the scale-in operation until the ECS instance enters the Stopped state. If the ECS instance is not successfully stopped, the scale-in process is rolled back and considered failed.
        self.stop_instance_timeout = stop_instance_timeout

    def validate(self):
        pass

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

        if self.lifecycle_hook_context_shrink is not None:
            result['LifecycleHookContext'] = self.lifecycle_hook_context_shrink

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
            self.lifecycle_hook_context_shrink = m.get('LifecycleHookContext')

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

