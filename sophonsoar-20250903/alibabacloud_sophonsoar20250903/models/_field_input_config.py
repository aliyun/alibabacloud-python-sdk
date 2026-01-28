# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20250903 import models as main_models
from darabonba.model import DaraModel

class FieldInputConfig(DaraModel):
    def __init__(
        self,
        arrayed: bool = None,
        default_value: str = None,
        field_check_regex: str = None,
        field_class: str = None,
        field_configs: List[main_models.FieldInputConfig] = None,
        field_description: str = None,
        field_example: str = None,
        field_name: str = None,
        field_path: str = None,
        field_type: str = None,
        required: bool = None,
    ):
        self.arrayed = arrayed
        self.default_value = default_value
        self.field_check_regex = field_check_regex
        self.field_class = field_class
        self.field_configs = field_configs
        self.field_description = field_description
        self.field_example = field_example
        self.field_name = field_name
        self.field_path = field_path
        self.field_type = field_type
        self.required = required

    def validate(self):
        if self.field_configs:
            for v1 in self.field_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrayed is not None:
            result['Arrayed'] = self.arrayed

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.field_check_regex is not None:
            result['FieldCheckRegex'] = self.field_check_regex

        if self.field_class is not None:
            result['FieldClass'] = self.field_class

        result['FieldConfigs'] = []
        if self.field_configs is not None:
            for k1 in self.field_configs:
                result['FieldConfigs'].append(k1.to_map() if k1 else None)

        if self.field_description is not None:
            result['FieldDescription'] = self.field_description

        if self.field_example is not None:
            result['FieldExample'] = self.field_example

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_path is not None:
            result['FieldPath'] = self.field_path

        if self.field_type is not None:
            result['FieldType'] = self.field_type

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arrayed') is not None:
            self.arrayed = m.get('Arrayed')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('FieldCheckRegex') is not None:
            self.field_check_regex = m.get('FieldCheckRegex')

        if m.get('FieldClass') is not None:
            self.field_class = m.get('FieldClass')

        self.field_configs = []
        if m.get('FieldConfigs') is not None:
            for k1 in m.get('FieldConfigs'):
                temp_model = main_models.FieldInputConfig()
                self.field_configs.append(temp_model.from_map(k1))

        if m.get('FieldDescription') is not None:
            self.field_description = m.get('FieldDescription')

        if m.get('FieldExample') is not None:
            self.field_example = m.get('FieldExample')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')

        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

