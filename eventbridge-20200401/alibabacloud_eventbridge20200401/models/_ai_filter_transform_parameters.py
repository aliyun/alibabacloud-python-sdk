# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiFilterTransformParameters(DaraModel):
    def __init__(
        self,
        condition: str = None,
        input_field: main_models.AiTransformField = None,
        on_mismatch: str = None,
        step_name: str = None,
    ):
        # The retention condition described in natural language. The model uses this condition to determine whether an event matches.
        self.condition = condition
        # The input text field.
        self.input_field = input_field
        # The behavior when a mismatch occurs. Valid values: discard (default): discards the event. forward: forwards the event as-is.
        self.on_mismatch = on_mismatch
        # The field name in the CloudEvent to which the output is attached. Default value: transform0.
        self.step_name = step_name

    def validate(self):
        if self.input_field:
            self.input_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.on_mismatch is not None:
            result['OnMismatch'] = self.on_mismatch

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('OnMismatch') is not None:
            self.on_mismatch = m.get('OnMismatch')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

