# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Row(DaraModel):
    def __init__(
        self,
        cells: List[main_models.Cell] = None,
    ):
        self.cells = cells

    def validate(self):
        if self.cells:
            for v1 in self.cells:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cells'] = []
        if self.cells is not None:
            for k1 in self.cells:
                result['cells'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cells = []
        if m.get('cells') is not None:
            for k1 in m.get('cells'):
                temp_model = main_models.Cell()
                self.cells.append(temp_model.from_map(k1))

        return self

