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
        # The type of the scaling policy. Valid values:
        # 
        # *   QuantityChangeInCapacity: adds the specified number of ECS instances to or removes the specified number of ECS instances from the scaling group.
        # *   PercentChangeInCapacity: adds the specified percentage of ECS instances to or removes the specified percentage of ECS instances from the scaling group.
        # *   TotalCapacity: adjusts the number of ECS instances in the scaling group to a specified number.
        # 
        # This parameter is required.
        self.adjustment_type = adjustment_type
        # The number of instances in each adjustment. The number of ECS instances in each adjustment cannot exceed 1,000.
        # 
        # *   Valid values if you set the AdjustmentType parameter to QuantityChangeInCapacity: -1000 to 1000.
        # *   Valid values if you set the AdjustmentType parameter to PercentChangeInCapacity: -100 to 10000.
        # *   Valid values if you set the AdjustmentType parameter to TotalCapacity: 0 to 2000.
        # 
        # This parameter is required.
        self.adjustment_value = adjustment_value
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The execution mode. Valid values:
        # 
        # *   None: If this is not specified, auto scaling is performed.
        # *   PlanOnly: Scaling is not triggered. Only elastic planning is performed. The planning result is returned in PlanResult, including the instance type, zone ID, billing type, and number of created instances.
        # 
        # Default value: None.
        self.execution_mode = execution_mode
        # The context of the lifecycle hook.
        self.lifecycle_hook_context_shrink = lifecycle_hook_context_shrink
        # The minimum number of instances allowed in each adjustment. This parameter takes effect only if you set the `AdjustmentType` parameter to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The overrides that allow you to adjust the scaling group of the Elastic Container Instance (ECI) type during a scale-out event.
        self.overrides_shrink = overrides_shrink
        self.owner_id = owner_id
        # Whether the current scale-out task supports concurrency.
        self.parallel_task = parallel_task
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # Specifies whether to trigger the scaling task in a synchronous manner. This parameter takes effect only on scaling groups for which you specified an expected number of instances. Valid Values:
        # 
        # *   true: triggers the scaling task in a synchronous manner. A scaling activity is triggered at the time when the scaling rule is executed.
        # *   false: does not trigger the scaling task in a synchronous manner. After you change the expected number of instances for the scaling group, Auto Scaling checks whether the total number of instances in the scaling group matches the new expected number and determines whether to trigger the scaling activity based on the check result.
        # 
        # >  For more information, see [Expected number of instances](https://help.aliyun.com/document_detail/146231.html).
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

