# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScaleWithAdjustmentShrinkRequest(DaraModel):
    def __init__(
        self,
        activity_metadata: str = None,
        adjustment_type: str = None,
        adjustment_value: int = None,
        client_token: str = None,
        execution_mode: str = None,
        lifecycle_hook_context_shrink: str = None,
        min_adjustment_magnitude: int = None,
        overrides_shrink: str = None,
        owner_id: int = None,
        parallel_task: bool = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
        sync_activity: bool = None,
    ):
        # The metadata for the scaling activity.
        self.activity_metadata = activity_metadata
        # The method used to adjust the number of instances in a scaling activity. Valid values:
        # 
        # - `QuantityChangeInCapacity`: Adds or removes a specified number of ECS instances.
        # 
        # - `PercentChangeInCapacity`: Adds or removes a specified percentage of ECS instances.
        # 
        # - `TotalCapacity`: Adjusts the number of ECS instances in the scaling group to a specified number.
        # 
        # This parameter is required.
        self.adjustment_type = adjustment_type
        # The adjustment value for the scaling activity. A single adjustment cannot add or remove more than 1,000 ECS instances. The valid range depends on `AdjustmentType`:
        # 
        # - `QuantityChangeInCapacity`: -1000 to 1000.
        # 
        # - `PercentChangeInCapacity`: -100 to 10000.
        # 
        # - `TotalCapacity`: 0 to 2000.
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # A client-generated token to ensure the idempotence of the request. This token must be a unique string of up to 64 ASCII characters.
        self.client_token = client_token
        # The execution mode. Valid values:
        # 
        # - `None`: Executes a standard scaling activity.
        # 
        # - `PlanOnly`: Only performs elastic planning and returns the results in `PlanResult` without triggering the scaling activity. The results include details such as instance types, availability zones, billing methods, and the number of new instances.
        # 
        # Default value: None.
        self.execution_mode = execution_mode
        # The lifecycle hook context.
        self.lifecycle_hook_context_shrink = lifecycle_hook_context_shrink
        # The minimum number of instances to adjust in a scaling activity. This parameter takes effect only when `AdjustmentType` is set to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The parameters to override when scaling out an ECI scaling group.
        self.overrides_shrink = overrides_shrink
        self.owner_id = owner_id
        # Specifies whether the current scaling activity supports concurrency.
        self.parallel_task = parallel_task
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # Specifies whether to execute the scaling activity synchronously. This parameter applies only to scaling groups that are configured with an expected number of instances. Valid values:
        # 
        # - `true`: Synchronous execution. The scaling activity is triggered immediately.
        # 
        # - `false`: Asynchronous execution. The call updates the expected number of instances without immediately triggering the scaling activity. The activity occurs when the system detects a discrepancy between the new expected number and the current number of instances.
        # 
        # > For more information about the expected number of instances, see [Expected number of instances](https://help.aliyun.com/document_detail/146231.html).
        # 
        # Default value: false.
        self.sync_activity = sync_activity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_metadata is not None:
            result['ActivityMetadata'] = self.activity_metadata

        if self.adjustment_type is not None:
            result['AdjustmentType'] = self.adjustment_type

        if self.adjustment_value is not None:
            result['AdjustmentValue'] = self.adjustment_value

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.lifecycle_hook_context_shrink is not None:
            result['LifecycleHookContext'] = self.lifecycle_hook_context_shrink

        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude

        if self.overrides_shrink is not None:
            result['Overrides'] = self.overrides_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parallel_task is not None:
            result['ParallelTask'] = self.parallel_task

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.sync_activity is not None:
            result['SyncActivity'] = self.sync_activity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityMetadata') is not None:
            self.activity_metadata = m.get('ActivityMetadata')

        if m.get('AdjustmentType') is not None:
            self.adjustment_type = m.get('AdjustmentType')

        if m.get('AdjustmentValue') is not None:
            self.adjustment_value = m.get('AdjustmentValue')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('LifecycleHookContext') is not None:
            self.lifecycle_hook_context_shrink = m.get('LifecycleHookContext')

        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')

        if m.get('Overrides') is not None:
            self.overrides_shrink = m.get('Overrides')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParallelTask') is not None:
            self.parallel_task = m.get('ParallelTask')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SyncActivity') is not None:
            self.sync_activity = m.get('SyncActivity')

        return self

