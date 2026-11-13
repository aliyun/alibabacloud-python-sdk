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
        # The metadata of the scaling activity.
        self.activity_metadata = activity_metadata
        # The adjustment method for the scaling activity. Valid values:
        # 
        # - QuantityChangeInCapacity: Increases or decreases a specified number of ECS instances.
        # - PercentChangeInCapacity: Increases or decreases a specified percentage of ECS instances.
        # - TotalCapacity: Adjusts the number of ECS instances in the current scaling group to a specified number.
        # 
        # This parameter is required.
        self.adjustment_type = adjustment_type
        # The adjustment value for the scaling activity. In all cases, the number of ECS instances adjusted in a single operation cannot exceed 1,000. Otherwise, the adjustment fails. Valid values vary based on the adjustment method:
        # - QuantityChangeInCapacity: -1,000 to 1,000.
        # - PercentChangeInCapacity: -100 to 10,000.
        # - TotalCapacity: 0 to 2,000.
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions. You can generate the value of this parameter on the client side. The value must be unique across different requests and can be up to 64 ASCII characters in length. The value cannot contain non-ASCII characters.
        self.client_token = client_token
        # The execution mode. Valid values:
        # 
        # - None: Not specified. Normal scaling is performed.
        # - PlanOnly: Does not trigger scaling. Only elastic planning is executed. The planning results, including instance types, zone IDs, billing methods, and the number of instances to be created, are returned in PlanResult.
        # 
        # Default value: None.
        self.execution_mode = execution_mode
        # The context information of the lifecycle hook.
        self.lifecycle_hook_context_shrink = lifecycle_hook_context_shrink
        # The minimum number of instances to be adjusted in the scaling activity. This parameter takes effect only when `AdjustmentType` is set to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The override parameters specified for scaling out an Elastic Container Instance (ECI) scaling group.
        self.overrides_shrink = overrides_shrink
        self.owner_id = owner_id
        # Specifies whether the current scaling task supports concurrent execution.
        self.parallel_task = parallel_task
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # Specifies whether to synchronously execute the scaling activity. This parameter is valid only for scaling groups that have the expected number of instances configured. Valid values:
        # 
        # - true: Synchronous process. When the scaling rule is executed, the scale-out or scale-in activity of the scaling group is directly triggered.
        # - false: Asynchronous process. When the expected number of instances in the scaling group is modified, the actual scale-out or scale-in activity of the scaling group is not immediately triggered. The system automatically detects the difference between the expected number of instances and the current number of instances in the scaling group, and then triggers the scale-out or scale-in activity.
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

