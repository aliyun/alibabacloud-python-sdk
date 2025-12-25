# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class HttpApiBackendMatchConditions(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.HttpApiBackendMatchCondition] = None,
        default: bool = None,
    ):
        self.conditions = conditions
        self.default = default

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.default is not None:
            result['default'] = self.default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.HttpApiBackendMatchCondition()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('default') is not None:
            self.default = m.get('default')

        return self

