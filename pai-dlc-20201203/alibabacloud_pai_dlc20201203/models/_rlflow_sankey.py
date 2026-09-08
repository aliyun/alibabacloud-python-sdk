# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLFlowSankey(DaraModel):
    def __init__(
        self,
        columns: List[main_models.RLFlowSankeyColumn] = None,
        exits: List[main_models.RLFlowSankeyExit] = None,
    ):
        # The five columns of the main chain.
        self.columns = columns
        # The outflow edges of each column.
        self.exits = exits

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.exits:
            for v1 in self.exits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        result['Exits'] = []
        if self.exits is not None:
            for k1 in self.exits:
                result['Exits'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.RLFlowSankeyColumn()
                self.columns.append(temp_model.from_map(k1))

        self.exits = []
        if m.get('Exits') is not None:
            for k1 in m.get('Exits'):
                temp_model = main_models.RLFlowSankeyExit()
                self.exits.append(temp_model.from_map(k1))

        return self

