# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ModelConfig(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        model_template: main_models.ModelTemplate = None,
    ):
        # The name of the output model. The output model of a joint training job is registered in the Models section of AI Asset Management under this name.
        self.model_name = model_name
        # The model template configuration. This configuration is required if you want to deploy the output model to Elastic Algorithm Service (EAS) with one click.
        self.model_template = model_template

    def validate(self):
        if self.model_template:
            self.model_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_template is not None:
            result['ModelTemplate'] = self.model_template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelTemplate') is not None:
            temp_model = main_models.ModelTemplate()
            self.model_template = temp_model.from_map(m.get('ModelTemplate'))

        return self

