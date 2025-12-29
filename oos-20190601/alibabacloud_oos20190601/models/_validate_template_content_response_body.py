# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class ValidateTemplateContentResponseBody(DaraModel):
    def __init__(
        self,
        outputs: str = None,
        parameters: str = None,
        ram_role: str = None,
        request_id: str = None,
        tasks: List[main_models.ValidateTemplateContentResponseBodyTasks] = None,
    ):
        # The outputs of the template.
        self.outputs = outputs
        # The parameters of the template.
        self.parameters = parameters
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the request.
        self.request_id = request_id
        # The task defined in the template.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.ValidateTemplateContentResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class ValidateTemplateContentResponseBodyTasks(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        outputs: str = None,
        properties: str = None,
        type: str = None,
    ):
        # The description of the task.
        self.description = description
        # The name of the task.
        self.name = name
        # The outputs of the task.
        self.outputs = outputs
        # The properties of the task.
        self.properties = properties
        # The type of the task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

