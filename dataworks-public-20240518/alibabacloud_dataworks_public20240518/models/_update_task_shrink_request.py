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
        # The client unique code of the node, used to uniquely identify a node. This code is used to implement asynchronous operations and idempotence. If not specified during creation, the system automatically generates one, and the code is uniquely bound to the resource ID. When updating or deleting a resource, if this parameter is specified, it must be consistent with the client unique code used during creation.
        self.client_unique_code = client_unique_code
        # The associated data source information.
        self.data_source_shrink = data_source_shrink
        # The dependency information.
        self.dependencies_shrink = dependencies_shrink
        # The description.
        self.description = description
        # The project environment. Valid values:
        # - Prod: production.
        # - Dev: development.
        self.env_type = env_type
        # The node ID.
        # 
        # This parameter is required.
        self.id = id
        # The input information.
        self.inputs_shrink = inputs_shrink
        # The instance generation mode. Valid values:
        # - T+1: The instance is generated the next day.
        # - Immediately: The instance is generated immediately. Note: Only periodic instances whose scheduled time is at least ten minutes after the node publish time are generated normally. During the full instance generation period (22:00 to 24:00), real-time instance generation is not available. You can submit and publish nodes, but new nodes do not automatically generate instances.
        self.instance_mode = instance_mode
        # The name.
        self.name = name
        # The output information.
        self.outputs_shrink = outputs_shrink
        # The account ID of the node owner.
        self.owner = owner
        # The retry time interval, in milliseconds. The value cannot exceed 1800000.
        self.rerun_interval = rerun_interval
        # Specifies whether the node can be rerun. Valid values:
        # - AllDenied: The node cannot be rerun regardless of whether it succeeds or fails.
        # - FailureAllowed: The node can be rerun only when it fails.
        # - AllAllowed: The node can be rerun regardless of whether it succeeds or fails.
        self.rerun_mode = rerun_mode
        # The number of retries. This parameter takes effect when the node is configured to allow reruns.
        self.rerun_times = rerun_times
        # The environment configuration, such as resource group information.
        self.runtime_resource_shrink = runtime_resource_shrink
        # The script information.
        self.script_shrink = script_shrink
        # The list of node tags.
        self.tags_shrink = tags_shrink
        # The node execution timeout period, in seconds. The value must be greater than 3600.
        self.timeout = timeout
        # The node trigger method.
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

