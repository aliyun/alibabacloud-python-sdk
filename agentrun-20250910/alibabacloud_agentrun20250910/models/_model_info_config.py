# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ModelInfoConfig(DaraModel):
    def __init__(
        self,
        model_features: main_models.ModelFeatures = None,
        model_name: str = None,
        model_parameter_rules: List[main_models.ModelParameterRule] = None,
        model_properties: main_models.ModelProperties = None,
    ):
        self.model_features = model_features
        self.model_name = model_name
        self.model_parameter_rules = model_parameter_rules
        self.model_properties = model_properties

    def validate(self):
        if self.model_features:
            self.model_features.validate()
        if self.model_parameter_rules:
            for v1 in self.model_parameter_rules:
                 if v1:
                    v1.validate()
        if self.model_properties:
            self.model_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_features is not None:
            result['modelFeatures'] = self.model_features.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        result['modelParameterRules'] = []
        if self.model_parameter_rules is not None:
            for k1 in self.model_parameter_rules:
                result['modelParameterRules'].append(k1.to_map() if k1 else None)

        if self.model_properties is not None:
            result['modelProperties'] = self.model_properties.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelFeatures') is not None:
            temp_model = main_models.ModelFeatures()
            self.model_features = temp_model.from_map(m.get('modelFeatures'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        self.model_parameter_rules = []
        if m.get('modelParameterRules') is not None:
            for k1 in m.get('modelParameterRules'):
                temp_model = main_models.ModelParameterRule()
                self.model_parameter_rules.append(temp_model.from_map(k1))

        if m.get('modelProperties') is not None:
            temp_model = main_models.ModelProperties()
            self.model_properties = temp_model.from_map(m.get('modelProperties'))

        return self

