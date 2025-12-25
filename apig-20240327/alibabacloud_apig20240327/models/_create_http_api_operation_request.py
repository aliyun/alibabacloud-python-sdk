# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateHttpApiOperationRequest(DaraModel):
    def __init__(
        self,
        operations: List[main_models.HttpApiOperation] = None,
    ):
        # List of operation definitions.
        self.operations = operations

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['operations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.operations = []
        if m.get('operations') is not None:
            for k1 in m.get('operations'):
                temp_model = main_models.HttpApiOperation()
                self.operations.append(temp_model.from_map(k1))

        return self

