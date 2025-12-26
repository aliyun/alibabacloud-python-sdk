# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class AllocateStrategySpec(DaraModel):
    def __init__(
        self,
        node_specs: List[main_models.NodeSpec] = None,
    ):
        self.node_specs = node_specs

    def validate(self):
        if self.node_specs:
            for v1 in self.node_specs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeSpecs'] = []
        if self.node_specs is not None:
            for k1 in self.node_specs:
                result['NodeSpecs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_specs = []
        if m.get('NodeSpecs') is not None:
            for k1 in m.get('NodeSpecs'):
                temp_model = main_models.NodeSpec()
                self.node_specs.append(temp_model.from_map(k1))

        return self

