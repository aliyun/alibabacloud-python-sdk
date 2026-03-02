# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TableResult(DaraModel):
    def __init__(
        self,
        collect_sink_operator_id: str = None,
        row_updates: List[main_models.RowUpdate] = None,
        table_name: str = None,
    ):
        self.collect_sink_operator_id = collect_sink_operator_id
        self.row_updates = row_updates
        self.table_name = table_name

    def validate(self):
        if self.row_updates:
            for v1 in self.row_updates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collect_sink_operator_id is not None:
            result['collectSinkOperatorId'] = self.collect_sink_operator_id

        result['rowUpdates'] = []
        if self.row_updates is not None:
            for k1 in self.row_updates:
                result['rowUpdates'].append(k1.to_map() if k1 else None)

        if self.table_name is not None:
            result['tableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectSinkOperatorId') is not None:
            self.collect_sink_operator_id = m.get('collectSinkOperatorId')

        self.row_updates = []
        if m.get('rowUpdates') is not None:
            for k1 in m.get('rowUpdates'):
                temp_model = main_models.RowUpdate()
                self.row_updates.append(temp_model.from_map(k1))

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        return self

