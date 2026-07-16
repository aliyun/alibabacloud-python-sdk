# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class TagSelector(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.TagCondition] = None,
        expression: str = None,
        relation: str = None,
    ):
        self.conditions = conditions
        self.expression = expression
        self.relation = relation

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

        if self.expression is not None:
            result['expression'] = self.expression

        if self.relation is not None:
            result['relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.TagCondition()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        return self

