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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to modify the expected number of instances. Valid values:
        # 
        # - true: After the ECS instances are removed from the scaling group, the expected number of instances is decreased by the number of removed instances.
        # - false: After the ECS instances are removed from the scaling group, the expected number of instances remains unchanged.
        # 
        # Default value: true.
        self.decrease_desired_capacity = decrease_desired_capacity
        # Specifies whether to ignore invalid instances when removing a batch of instances from the scaling group. Valid values:
        # - true: Invalid instances are ignored when removing a batch of instances from the scaling group. If invalid instances exist and valid instances are successfully removed, the execution status of the scaling activity is displayed as Warning. You can view the invalid instances in the scaling activity details.
        # - false: Invalid instances are not ignored when removing a batch of instances from the scaling group. If invalid instances exist in the batch, an error is reported.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances to be removed.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The context information of the lifecycle hook.
        self.lifecycle_hook_context_shrink = lifecycle_hook_context_shrink
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        # Specifies the action for the removed ECS instances. Valid values:
        # 
        # - recycle: The ECS instances are stopped in economical mode.
        # 
        #     > This value takes effect only when `ScalingPolicy` is set to `recycle`.
        # - release: The ECS instances are released.
        # 
        # The ScalingPolicy parameter of CreateScalingGroup specifies the reclaim mode of the scaling group, but the specific action when an instance is removed is determined by the RemovePolicy parameter of RemoveInstances. Examples:
        # 
        # - If ScalingPolicy is set to recycle and RemovePolicy is set to recycle, the ECS instances are stopped in economical mode.
        # - If ScalingPolicy is set to recycle and RemovePolicy is set to release, the ECS instances are released.
        # - If ScalingPolicy is set to release and RemovePolicy is set to recycle, the ECS instances are released.
        # - If ScalingPolicy is set to release and RemovePolicy is set to release, the ECS instances are released.
        # 
        # Default value: release.
        self.remove_policy = remove_policy
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The timeout period for waiting for the ECS instances to be successfully stopped during the scale-in process. Unit: seconds.
        # Valid values: 30 to 240.
        # 
        # > - By default, this parameter inherits the value from the scaling group. You can also reset it when calling RemoveInstances.
        # > - This parameter takes effect only in the scale-in process when RemovePolicy is set to release.  
        # > - If this parameter is set, the system waits for a maximum of the StopInstanceTimeout period for the instances to be successfully stopped. After the timeout period, the scale-in process continues regardless of whether the instances are successfully stopped.  
        # > - If this parameter is not set, the system waits for a long time for the instances to be successfully stopped. The scale-in process continues only after the instances are successfully stopped. If the instances fail to be stopped, the scale-in process is rolled back and the scale-in fails.
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

