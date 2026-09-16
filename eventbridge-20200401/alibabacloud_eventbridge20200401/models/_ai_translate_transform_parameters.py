# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiTranslateTransformParameters(DaraModel):
    def __init__(
        self,
        input_field: main_models.AiTransformField = None,
        source_language: str = None,
        step_name: str = None,
        target_language: str = None,
    ):
        self.input_field = input_field
        self.source_language = source_language
        self.step_name = step_name
        self.target_language = target_language

    def validate(self):
        if self.input_field:
            self.input_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        return self

