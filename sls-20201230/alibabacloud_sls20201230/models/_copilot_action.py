# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CopilotAction(DaraModel):
    def __init__(
        self,
        action: str = None,
        description: str = None,
        name: str = None,
        parameters: List[main_models.CopilotActionParameters] = None,
        query_max_length: int = None,
        query_template: str = None,
        query_template_parameters: List[main_models.CopilotActionQueryTemplateParameters] = None,
        scene: str = None,
    ):
        self.action = action
        self.description = description
        self.name = name
        self.parameters = parameters
        self.query_max_length = query_max_length
        self.query_template = query_template
        self.query_template_parameters = query_template_parameters
        self.scene = scene

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()
        if self.query_template_parameters:
            for v1 in self.query_template_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['parameters'].append(k1.to_map() if k1 else None)

        if self.query_max_length is not None:
            result['queryMaxLength'] = self.query_max_length

        if self.query_template is not None:
            result['queryTemplate'] = self.query_template

        result['queryTemplateParameters'] = []
        if self.query_template_parameters is not None:
            for k1 in self.query_template_parameters:
                result['queryTemplateParameters'].append(k1.to_map() if k1 else None)

        if self.scene is not None:
            result['scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.parameters = []
        if m.get('parameters') is not None:
            for k1 in m.get('parameters'):
                temp_model = main_models.CopilotActionParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('queryMaxLength') is not None:
            self.query_max_length = m.get('queryMaxLength')

        if m.get('queryTemplate') is not None:
            self.query_template = m.get('queryTemplate')

        self.query_template_parameters = []
        if m.get('queryTemplateParameters') is not None:
            for k1 in m.get('queryTemplateParameters'):
                temp_model = main_models.CopilotActionQueryTemplateParameters()
                self.query_template_parameters.append(temp_model.from_map(k1))

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        return self

class CopilotActionQueryTemplateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        prompt: str = None,
        required: str = None,
        type: str = None,
    ):
        self.name = name
        self.prompt = prompt
        self.required = required
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CopilotActionParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        prompt: str = None,
        required: str = None,
        type: str = None,
    ):
        self.name = name
        self.prompt = prompt
        self.required = required
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.required is not None:
            result['required'] = self.required

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

