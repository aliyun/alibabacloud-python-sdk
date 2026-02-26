# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class UpdateTriggerRequest(DaraModel):
    def __init__(
        self,
        actions: List[main_models.UpdateTriggerRequestActions] = None,
        id: str = None,
        input: main_models.Input = None,
        project_name: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The processing templates.
        self.actions = actions
        # The ID of the trigger. You can obtain the ID of the trigger from the response of the [CreateTrigger](https://help.aliyun.com/document_detail/479912.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The data source configurations.
        self.input = input
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The custom tags. You can search for or filter asynchronous tasks by custom tag.
        self.tags = tags

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.UpdateTriggerRequestActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            temp_model = main_models.Input()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class UpdateTriggerRequestActions(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: List[str] = None,
    ):
        # The template name.
        self.name = name
        # The template parameters.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self

