# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        data_source_shrink: str = None,
        dependencies_shrink: str = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        inputs_shrink: str = None,
        instance_mode: str = None,
        name: str = None,
        outputs_shrink: str = None,
        owner: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        runtime_resource_shrink: str = None,
        script_shrink: str = None,
        tags_shrink: str = None,
        timeout: int = None,
        trigger_shrink: str = None,
    ):
        # The unique code of the client. This code uniquely identifies a task. This parameter is used to create a task asynchronously and implement the idempotence of the task. If you do not specify this parameter when you create the task, the system automatically generates a unique code. The unique code is uniquely associated with the task ID. If you specify this parameter when you update or delete the task, the value of this parameter must be the unique code that is used to create the task.
        self.client_unique_code = client_unique_code
        # The information about the associated data source.
        self.data_source_shrink = data_source_shrink
        # The dependency information.
        self.dependencies_shrink = dependencies_shrink
        # The description of the task.
        self.description = description
        # The project environment.
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The task ID.
        # 
        # This parameter is required.
        self.id = id
        # The input information.
        self.inputs_shrink = inputs_shrink
        # The instance generation mode.
        # 
        # *   T+1: the next day
        # *   Immediately Note: Scheduled instances are generated only if the scheduled time is at least 10 minutes after the publish time. Real-time instance generation is unavailable during the global instance generation period (23:30 to 24:00). You can publish nodes during this period, but instances for the new nodes will not be generated automatically.
        self.instance_mode = instance_mode
        # Name.
        self.name = name
        # The output information.
        self.outputs_shrink = outputs_shrink
        # The account ID of the task owner.
        self.owner = owner
        # The rerun interval. Unit: milliseconds. Must not exceed 1800000.
        self.rerun_interval = rerun_interval
        # The rerun mode. Valid values:
        # 
        # *   AllDenied: The task cannot be rerun.
        # *   FailureAllowed: The task can be rerun only after it fails.
        # *   AllAllowed: The task can always be rerun.
        self.rerun_mode = rerun_mode
        # The number of times that the task is rerun. This parameter takes effect only if the RerunMode parameter is set to AllAllowed or FailureAllowed.
        self.rerun_times = rerun_times
        # Runtime environment configurations, such as resource group information.
        self.runtime_resource_shrink = runtime_resource_shrink
        # The run script information.
        self.script_shrink = script_shrink
        # The tags.
        self.tags_shrink = tags_shrink
        # Task execution timeout in seconds. Must be greater than 3600.
        self.timeout = timeout
        # The triggering method.
        self.trigger_shrink = trigger_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_unique_code is not None:
            result['ClientUniqueCode'] = self.client_unique_code

        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink

        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs_shrink is not None:
            result['Outputs'] = self.outputs_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times

        if self.runtime_resource_shrink is not None:
            result['RuntimeResource'] = self.runtime_resource_shrink

        if self.script_shrink is not None:
            result['Script'] = self.script_shrink

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')

        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            self.outputs_shrink = m.get('Outputs')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource_shrink = m.get('RuntimeResource')

        if m.get('Script') is not None:
            self.script_shrink = m.get('Script')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        return self

