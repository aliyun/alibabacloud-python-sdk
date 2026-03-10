# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ExperimentConfig(DaraModel):
    def __init__(
        self,
        label: str = None,
        model_name: str = None,
        model_parameters: main_models.ModelParameters = None,
        model_provider: str = None,
        name: str = None,
        prompt_template: List[main_models.PromptTemplateItem] = None,
    ):
        self.label = label
        self.model_name = model_name
        self.model_parameters = model_parameters
        self.model_provider = model_provider
        self.name = name
        self.prompt_template = prompt_template

    def validate(self):
        if self.model_parameters:
            self.model_parameters.validate()
        if self.prompt_template:
            for v1 in self.prompt_template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_parameters is not None:
            result['modelParameters'] = self.model_parameters.to_map()

        if self.model_provider is not None:
            result['modelProvider'] = self.model_provider

        if self.name is not None:
            result['name'] = self.name

        result['promptTemplate'] = []
        if self.prompt_template is not None:
            for k1 in self.prompt_template:
                result['promptTemplate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelParameters') is not None:
            temp_model = main_models.ModelParameters()
            self.model_parameters = temp_model.from_map(m.get('modelParameters'))

        if m.get('modelProvider') is not None:
            self.model_provider = m.get('modelProvider')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.prompt_template = []
        if m.get('promptTemplate') is not None:
            for k1 in m.get('promptTemplate'):
                temp_model = main_models.PromptTemplateItem()
                self.prompt_template.append(temp_model.from_map(k1))

        return self

