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
        self.lifecycle_hook_context = lifecycle_hook_context
        # The minimum number of instances allowed in each adjustment. This parameter takes effect only if you set the `AdjustmentType` parameter to `PercentChangeInCapacity`.
        self.min_adjustment_magnitude = min_adjustment_magnitude
        # The overrides that allow you to adjust the scaling group of the Elastic Container Instance (ECI) type during a scale-out event.
        self.overrides = overrides
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
        # The list of parameters that you want to use to override specific configurations for containers.
        self.container_overrides = container_overrides
        # The number of vCPUs that you want to allocate to the instance. Unit: vCPUs.
        self.cpu = cpu
        # The memory size that you want to allocate to the instance. Unit: GiB.
        self.memory = memory
        # The user data of the Elastic Compute Service (ECS) instance. The user data must be encoded in Base64 format. The size of raw data before Base64 encoding cannot exceed 32 KB.
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
        # The argument that corresponds to the startup command of the container. You can specify up to 10 arguments.
        self.args = args
        # The container startup commands. You can specify up to 20 commands. Each command can contain up to 256 characters.
        self.commands = commands
        # The number of vCPUs that you want to allocate to the container. Unit: vCPUs.
        self.cpu = cpu
        # The information about the environment variables.
        self.environment_vars = environment_vars
        # The memory size that you want to allocate to the container. Unit: GiB.
        self.memory = memory
        # The name of the container. If you specify ContainerOverrides, you must also specify Name. ContainerOverrides takes effect only when the container name specified by Name matches that specified in the scaling configuration.
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
        # The name of the environment variable. The name must be 1 to 128 characters in length. Format requirement: `[0-9a-zA-Z]` and underscores (_). It cannot start with a digit.
        self.key = key
        # The value of the environment variable. The value can be up to 256 characters in length.
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
        # Specifies whether to disable the lifecycle hook. Valid values:
        # 
        # *   true
        # *   false
        self.disable_lifecycle_hook = disable_lifecycle_hook
        # The IDs of the lifecycle hooks that you want to disable.
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

