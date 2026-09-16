# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AiEmbedTransformParameters(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        input_field: main_models.AiTransformField = None,
        model: str = None,
        step_name: str = None,
    ):
        # The vector dimensions. Must be a dimension supported by the selected model. If not specified, the default value of the model is used (1024 for most models, 1536 for v1/v2/async).
        self.dimension = dimension
        # The input text field.
        self.input_field = input_field
        # The embedding model. Default value: text-embedding-v4.
        self.model = model
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
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.input_field is not None:
            result['InputField'] = self.input_field.to_map()

        if self.model is not None:
            result['Model'] = self.model

        if self.step_name is not None:
            result['StepName'] = self.step_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('InputField') is not None:
            temp_model = main_models.AiTransformField()
            self.input_field = temp_model.from_map(m.get('InputField'))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        return self

