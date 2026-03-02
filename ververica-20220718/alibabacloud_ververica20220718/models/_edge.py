# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Edge(DaraModel):
    def __init__(
        self,
        column_lineage: List[main_models.Relation] = None,
        table_lineage: List[main_models.Relation] = None,
    ):
        # The field-level data lineage.
        self.column_lineage = column_lineage
        # The table-level data lineage.
        self.table_lineage = table_lineage

    def validate(self):
        if self.column_lineage:
            for v1 in self.column_lineage:
                 if v1:
                    v1.validate()
        if self.table_lineage:
            for v1 in self.table_lineage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['columnLineage'] = []
        if self.column_lineage is not None:
            for k1 in self.column_lineage:
                result['columnLineage'].append(k1.to_map() if k1 else None)

        result['tableLineage'] = []
        if self.table_lineage is not None:
            for k1 in self.table_lineage:
                result['tableLineage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_lineage = []
        if m.get('columnLineage') is not None:
            for k1 in m.get('columnLineage'):
                temp_model = main_models.Relation()
                self.column_lineage.append(temp_model.from_map(k1))

        self.table_lineage = []
        if m.get('tableLineage') is not None:
            for k1 in m.get('tableLineage'):
                temp_model = main_models.Relation()
                self.table_lineage.append(temp_model.from_map(k1))

        return self

