# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateHttpApiOperationRequest(DaraModel):
    def __init__(
        self,
        operation: main_models.HttpApiOperation = None,
    ):
        # operation definition.
        self.operation = operation

    def validate(self):
        if self.operation:
            self.operation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['operation'] = self.operation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operation') is not None:
            temp_model = main_models.HttpApiOperation()
            self.operation = temp_model.from_map(m.get('operation'))

        return self

