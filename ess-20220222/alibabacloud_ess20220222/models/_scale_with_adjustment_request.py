# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ScaleWithAdjustmentRequest(DaraModel):
    def __init__(
        self,
        activity_metadata: str = None,
        adjustment_type: str = None,
        adjustment_value: int = None,
        client_token: str = None,
        execution_mode: str = None,
        lifecycle_hook_context: main_models.ScaleWithAdjustmentRequestLifecycleHookContext = None,
        min_adjustment_magnitude: int = None,
        overrides: main_models.ScaleWithAdjustmentRequestOverrides = None,
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
        self.lifecycle_hook_context = lifecycle_hook_context
        # The minimum number of instances to adjust in a scaling activity. This parameter takes effect only when `AdjustmentType` is set to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The parameters to override when scaling out an ECI scaling group.
        self.overrides = overrides
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
        if self.lifecycle_hook_context:
            self.lifecycle_hook_context.validate()
        if self.overrides:
            self.overrides.validate()

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

        if self.lifecycle_hook_context is not None:
            result['LifecycleHookContext'] = self.lifecycle_hook_context.to_map()

        if self.min_adjustment_magnitude is not None:
            result['MinAdjustmentMagnitude'] = self.min_adjustment_magnitude

        if self.overrides is not None:
            result['Overrides'] = self.overrides.to_map()

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
            temp_model = main_models.ScaleWithAdjustmentRequestLifecycleHookContext()
            self.lifecycle_hook_context = temp_model.from_map(m.get('LifecycleHookContext'))

        if m.get('MinAdjustmentMagnitude') is not None:
            self.min_adjustment_magnitude = m.get('MinAdjustmentMagnitude')

        if m.get('Overrides') is not None:
            temp_model = main_models.ScaleWithAdjustmentRequestOverrides()
            self.overrides = temp_model.from_map(m.get('Overrides'))

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

class ScaleWithAdjustmentRequestOverrides(DaraModel):
    def __init__(
        self,
        container_overrides: List[main_models.ScaleWithAdjustmentRequestOverridesContainerOverrides] = None,
        cpu: float = None,
        memory: float = None,
        user_data: str = None,
    ):
        # A list of container-specific overrides.
        self.container_overrides = container_overrides
        # The number of vCPUs for the instance. Unit: cores.
        self.cpu = cpu
        # The memory size for the instance. Unit: GiB.
        self.memory = memory
        # The user data for the ECS instance. It must be Base64-encoded, and the raw data cannot exceed 32 KB.
        self.user_data = user_data

    def validate(self):
        if self.container_overrides:
            for v1 in self.container_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerOverrides'] = []
        if self.container_overrides is not None:
            for k1 in self.container_overrides:
                result['ContainerOverrides'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_overrides = []
        if m.get('ContainerOverrides') is not None:
            for k1 in m.get('ContainerOverrides'):
                temp_model = main_models.ScaleWithAdjustmentRequestOverridesContainerOverrides()
                self.container_overrides.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ScaleWithAdjustmentRequestOverridesContainerOverrides(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[main_models.ScaleWithAdjustmentRequestOverridesContainerOverridesEnvironmentVars] = None,
        memory: float = None,
        name: str = None,
    ):
        # The arguments for the container\\"s startup command. You can specify up to 10 arguments.
        self.args = args
        # The container\\"s startup command, specified as an array of strings. You can specify up to 20 strings, and each can be up to 256 characters long.
        self.commands = commands
        # The number of vCPUs for the container. Unit: cores.
        self.cpu = cpu
        # Environment variables to set in the container.
        self.environment_vars = environment_vars
        # The memory size for the container. Unit: GiB.
        self.memory = memory
        # The name of the container to override. The override takes effect only if this name matches a container name in the scaling configuration.
        self.name = name

    def validate(self):
        if self.environment_vars:
            for v1 in self.environment_vars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.commands is not None:
            result['Commands'] = self.commands

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.ScaleWithAdjustmentRequestOverridesContainerOverridesEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ScaleWithAdjustmentRequestOverridesContainerOverridesEnvironmentVars(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the environment variable. It must be 1 to 128 characters long, cannot start with a digit, and can contain only letters (a-z, A-Z), digits (0-9), and underscores (_).
        self.key = key
        # The value of the environment variable, up to 256 characters long.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ScaleWithAdjustmentRequestLifecycleHookContext(DaraModel):
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
        # A list of lifecycle hook IDs to ignore during the scaling activity.
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

