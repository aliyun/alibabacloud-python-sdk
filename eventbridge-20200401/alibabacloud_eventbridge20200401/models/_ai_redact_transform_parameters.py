# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiRedactTransformParameters(DaraModel):
    def __init__(
        self,
        entities: List[str] = None,
        input_field: main_models.AiTransformField = None,
        mask_char: str = None,
        mode: str = None,
        step_name: str = None,
    ):
        # The entity types to identify and mask in the text, such as phone numbers, ID card numbers, and email addresses.
        self.entities = entities
        # The input text field.
        self.input_field = input_field
        # The mask character used in mask mode. Default value: *.
        self.mask_char = mask_char
        # The masking mode. Valid values: mask, replace, and remove.
        self.mode = mode
        # The field name appended to the CloudEvent for output. Default value: transform0.
        self.step_name = step_name

    def validate(self):
        if self.input_field:
            self.input_field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entities is not None:
            result['Entities'] = self.entities

        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.mask_char is not None:
            result['MaskChar'] = self.mask_char

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entities') is not None:
            self.entities = m.get('Entities')

        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('MaskChar') is not None:
            self.mask_char = m.get('MaskChar')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

