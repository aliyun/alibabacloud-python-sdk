# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiClassifyTransformParameters(DaraModel):
    def __init__(
        self,
        input_field: main_models.AiTransformField = None,
        instruction: str = None,
        labels: List[str] = None,
        output_mode: str = None,
        step_name: str = None,
    ):
        # The input text field.
        self.input_field = input_field
        # The classification constraints provided to the model, such as priority rules or how to categorize uncertain cases. If left empty, classification is performed based on Labels only.
        self.instruction = instruction
        # The candidate classification labels. The classification result must fall within this list. Specify at least two labels.
        self.labels = labels
        # The output mode. Valid values: single: single-label. multi: multi-label. Default value: single.
        self.output_mode = output_mode
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
        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.output_mode is not None:
            result['OutputMode'] = self.output_mode

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('OutputMode') is not None:
            self.output_mode = m.get('OutputMode')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

