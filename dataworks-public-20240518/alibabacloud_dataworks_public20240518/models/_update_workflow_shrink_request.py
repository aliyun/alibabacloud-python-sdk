# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWorkflowShrinkRequest(DaraModel):
    def __init__(
        self,
        client_unique_code: str = None,
        dependencies_shrink: str = None,
        description: str = None,
        env_type: str = None,
        id: int = None,
        instance_mode: str = None,
        name: str = None,
        outputs_shrink: str = None,
        owner: str = None,
        parameters: str = None,
        tags_shrink: str = None,
        tasks_shrink: str = None,
        trigger_shrink: str = None,
    ):
        # The unique code of the client. This parameter is used to create a workflow asynchronously and implement the idempotence of the workflow. If you do not specify this parameter when you create the workflow, the system automatically generates a unique code. The unique code is uniquely associated with the workflow ID. If you specify this parameter when you update or delete the workflow, the value of this parameter must be the unique code that is used to create the workflow.
        self.client_unique_code = client_unique_code
        # The dependency information.
        self.dependencies_shrink = dependencies_shrink
        # The description.
        self.description = description
        # The project environment.
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The workflow ID.
        # 
        # This parameter is required.
        self.id = id
        # The instance generation mode.
        # 
        # *   T+1: the next day
        # *   Immediately Note: Periodic instances will only be generated normally if the workflow\\"s scheduled time is more than 10 minutes after the workflow publication time. Real-time instance generation is not available during the batch instance generation period (23:30 to 24:00). While workflows can be published during this time, instances will not be regenerated immediately after submission.
        self.instance_mode = instance_mode
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The output information.
        self.outputs_shrink = outputs_shrink
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The parameters.
        self.parameters = parameters
        # The tags.
        self.tags_shrink = tags_shrink
        # Details about tasks.
        self.tasks_shrink = tasks_shrink
        # The trigger method.
        # 
        # This parameter is required.
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

        if self.dependencies_shrink is not None:
            result['Dependencies'] = self.dependencies_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs_shrink is not None:
            result['Outputs'] = self.outputs_shrink

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUniqueCode') is not None:
            self.client_unique_code = m.get('ClientUniqueCode')

        if m.get('Dependencies') is not None:
            self.dependencies_shrink = m.get('Dependencies')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            self.outputs_shrink = m.get('Outputs')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        return self

