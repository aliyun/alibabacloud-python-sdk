# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecDataCheckSqlPreviewRequest(DaraModel):
    def __init__(
        self,
        check_column: str = None,
        data_source_id: str = None,
        engine_id: str = None,
        full_table_name: str = None,
        partition_condition: str = None,
        task_id: int = None,
        where_clause: str = None,
    ):
        # The columns to check.
        self.check_column = check_column
        # The ID of the data source.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The ID of the check engine. Used in Spark scenarios.
        self.engine_id = engine_id
        # The name of the table to check, in the format `schema.table`.
        # 
        # This parameter is required.
        self.full_table_name = full_table_name
        # The partition condition.
        self.partition_condition = partition_condition
        # The ID of the check task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The WHERE condition.
        self.where_clause = where_clause

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_column is not None:
            result['checkColumn'] = self.check_column

        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id

        if self.engine_id is not None:
            result['engineId'] = self.engine_id

        if self.full_table_name is not None:
            result['fullTableName'] = self.full_table_name

        if self.partition_condition is not None:
            result['partitionCondition'] = self.partition_condition

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.where_clause is not None:
            result['whereClause'] = self.where_clause

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkColumn') is not None:
            self.check_column = m.get('checkColumn')

        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')

        if m.get('engineId') is not None:
            self.engine_id = m.get('engineId')

        if m.get('fullTableName') is not None:
            self.full_table_name = m.get('fullTableName')

        if m.get('partitionCondition') is not None:
            self.partition_condition = m.get('partitionCondition')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('whereClause') is not None:
            self.where_clause = m.get('whereClause')

        return self

