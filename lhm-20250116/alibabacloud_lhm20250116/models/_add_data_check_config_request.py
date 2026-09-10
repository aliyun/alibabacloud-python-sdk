# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDataCheckConfigRequest(DaraModel):
    def __init__(
        self,
        is_full_table_count: int = None,
        source_columns: str = None,
        source_group_clause: str = None,
        source_hint: str = None,
        source_partition: str = None,
        source_table: str = None,
        source_where_clause: str = None,
        target_columns: str = None,
        target_group_clause: str = None,
        target_hint: str = None,
        target_partition: str = None,
        target_table: str = None,
        target_where_clause: str = None,
        task_config_info: str = None,
        task_id: int = None,
        total_count_threshold: float = None,
    ):
        # Specifies whether to perform full-table validation. Valid values:
        # 
        # - 0: partition-level comparison.
        # - 1: full-table comparison.
        self.is_full_table_count = is_full_table_count
        # The columns of the source table. You can specify multiple columns separated by commas (,).
        self.source_columns = source_columns
        # The GROUP condition of the source table.
        self.source_group_clause = source_group_clause
        # The hint for the source.
        self.source_hint = source_hint
        # The partition of the source table.
        self.source_partition = source_partition
        # The name of the source table.
        self.source_table = source_table
        # The WHERE condition of the source table.
        self.source_where_clause = source_where_clause
        # The columns of the target table. You can specify multiple columns separated by commas (,).
        self.target_columns = target_columns
        # The GROUP condition of the target table.
        self.target_group_clause = target_group_clause
        # The hint for the target.
        self.target_hint = target_hint
        # The partition of the target table.
        self.target_partition = target_partition
        # The name of the target table.
        self.target_table = target_table
        # The WHERE condition of the target table.
        self.target_where_clause = target_where_clause
        # The batch table configurations for same-pattern creation (`taskMode=1`). Separate multiple configurations with a line break (`
        # `).
        self.task_config_info = task_config_info
        # The ID of the validation task.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The total data volume comparison threshold.
        self.total_count_threshold = total_count_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_full_table_count is not None:
            result['isFullTableCount'] = self.is_full_table_count

        if self.source_columns is not None:
            result['sourceColumns'] = self.source_columns

        if self.source_group_clause is not None:
            result['sourceGroupClause'] = self.source_group_clause

        if self.source_hint is not None:
            result['sourceHint'] = self.source_hint

        if self.source_partition is not None:
            result['sourcePartition'] = self.source_partition

        if self.source_table is not None:
            result['sourceTable'] = self.source_table

        if self.source_where_clause is not None:
            result['sourceWhereClause'] = self.source_where_clause

        if self.target_columns is not None:
            result['targetColumns'] = self.target_columns

        if self.target_group_clause is not None:
            result['targetGroupClause'] = self.target_group_clause

        if self.target_hint is not None:
            result['targetHint'] = self.target_hint

        if self.target_partition is not None:
            result['targetPartition'] = self.target_partition

        if self.target_table is not None:
            result['targetTable'] = self.target_table

        if self.target_where_clause is not None:
            result['targetWhereClause'] = self.target_where_clause

        if self.task_config_info is not None:
            result['taskConfigInfo'] = self.task_config_info

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.total_count_threshold is not None:
            result['totalCountThreshold'] = self.total_count_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isFullTableCount') is not None:
            self.is_full_table_count = m.get('isFullTableCount')

        if m.get('sourceColumns') is not None:
            self.source_columns = m.get('sourceColumns')

        if m.get('sourceGroupClause') is not None:
            self.source_group_clause = m.get('sourceGroupClause')

        if m.get('sourceHint') is not None:
            self.source_hint = m.get('sourceHint')

        if m.get('sourcePartition') is not None:
            self.source_partition = m.get('sourcePartition')

        if m.get('sourceTable') is not None:
            self.source_table = m.get('sourceTable')

        if m.get('sourceWhereClause') is not None:
            self.source_where_clause = m.get('sourceWhereClause')

        if m.get('targetColumns') is not None:
            self.target_columns = m.get('targetColumns')

        if m.get('targetGroupClause') is not None:
            self.target_group_clause = m.get('targetGroupClause')

        if m.get('targetHint') is not None:
            self.target_hint = m.get('targetHint')

        if m.get('targetPartition') is not None:
            self.target_partition = m.get('targetPartition')

        if m.get('targetTable') is not None:
            self.target_table = m.get('targetTable')

        if m.get('targetWhereClause') is not None:
            self.target_where_clause = m.get('targetWhereClause')

        if m.get('taskConfigInfo') is not None:
            self.task_config_info = m.get('taskConfigInfo')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('totalCountThreshold') is not None:
            self.total_count_threshold = m.get('totalCountThreshold')

        return self

