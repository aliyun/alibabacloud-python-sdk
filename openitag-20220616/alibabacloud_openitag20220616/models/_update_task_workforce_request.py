# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class UpdateTaskWorkforceRequest(DaraModel):
    def __init__(
        self,
        workforce: List[main_models.SimpleWorkforce] = None,
    ):
        # User List.
        self.workforce = workforce

    def validate(self):
        if self.workforce:
            for v1 in self.workforce:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Workforce'] = []
        if self.workforce is not None:
            for k1 in self.workforce:
                result['Workforce'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workforce = []
        if m.get('Workforce') is not None:
            for k1 in m.get('Workforce'):
                temp_model = main_models.SimpleWorkforce()
                self.workforce.append(temp_model.from_map(k1))

        return self

