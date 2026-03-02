# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class StackDetailResult(DaraModel):
    def __init__(
        self,
        stacks: List[main_models.StackInfo] = None,
    ):
        self.stacks = stacks

    def validate(self):
        if self.stacks:
            for v1 in self.stacks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['stacks'] = []
        if self.stacks is not None:
            for k1 in self.stacks:
                result['stacks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stacks = []
        if m.get('stacks') is not None:
            for k1 in m.get('stacks'):
                temp_model = main_models.StackInfo()
                self.stacks.append(temp_model.from_map(k1))

        return self

