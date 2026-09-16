# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiSummarizeTransformParameters(DaraModel):
    def __init__(
        self,
        input_field: main_models.AiTransformField = None,
        max_length: int = None,
        step_name: str = None,
    ):
        # The input text field.
        self.input_field = input_field
        # The maximum summary length. The value must be a positive integer. Default value: 200.
        self.max_length = max_length
        # The field name attached to the CloudEvent for output. Default value: transform0.
        self.step_name = step_name

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

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

