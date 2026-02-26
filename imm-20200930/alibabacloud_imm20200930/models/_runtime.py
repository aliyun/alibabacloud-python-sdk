# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Runtime(DaraModel):
    def __init__(
        self,
        hyperparameters: main_models.Hyperparameters = None,
        resource: main_models.Resource = None,
    ):
        # The hyperparameters.
        # 
        # This parameter is required.
        self.hyperparameters = hyperparameters
        # The resource.
        # 
        # This parameter is required.
        self.resource = resource

    def validate(self):
        if self.hyperparameters:
            self.hyperparameters.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hyperparameters is not None:
            result['Hyperparameters'] = self.hyperparameters.to_map()

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hyperparameters') is not None:
            temp_model = main_models.Hyperparameters()
            self.hyperparameters = temp_model.from_map(m.get('Hyperparameters'))

        if m.get('Resource') is not None:
            temp_model = main_models.Resource()
            self.resource = temp_model.from_map(m.get('Resource'))

        return self

