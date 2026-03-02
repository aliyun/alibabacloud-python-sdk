# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class TableSchema(DaraModel):
    def __init__(
        self,
        collect_sink_operator_id: str = None,
        schema: main_models.Schema = None,
        table_name: str = None,
    ):
        self.collect_sink_operator_id = collect_sink_operator_id
        self.schema = schema
        self.table_name = table_name

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collect_sink_operator_id is not None:
            result['collectSinkOperatorId'] = self.collect_sink_operator_id

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        if self.table_name is not None:
            result['tableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collectSinkOperatorId') is not None:
            self.collect_sink_operator_id = m.get('collectSinkOperatorId')

        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        return self

