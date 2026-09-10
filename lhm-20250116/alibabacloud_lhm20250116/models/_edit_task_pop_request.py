# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditTaskPopRequest(DaraModel):
    def __init__(
        self,
        concurrency: int = None,
        dql_test_datasource_name: str = None,
        source_dialect: str = None,
        target_dialect: str = None,
        task_id: int = None,
        task_name: str = None,
        task_type: int = None,
    ):
        # The concurrency for controlling the number of concurrent conversion executions.
        # 
        # This parameter is required.
        self.concurrency = concurrency
        # The name of the test data source associated with a DQL task.
        # 
        # This parameter is required.
        self.dql_test_datasource_name = dql_test_datasource_name
        # The source SQL dialect.
        # 
        # This parameter is required.
        self.source_dialect = source_dialect
        # The target SQL dialect.
        # 
        # This parameter is required.
        self.target_dialect = target_dialect
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The task name.
        # 
        # This parameter is required.
        self.task_name = task_name
        # The task type. Valid values:
        # 
        # - 1: DDL
        # - 2: DQL
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.dql_test_datasource_name is not None:
            result['dqlTestDatasourceName'] = self.dql_test_datasource_name

        if self.source_dialect is not None:
            result['sourceDialect'] = self.source_dialect

        if self.target_dialect is not None:
            result['targetDialect'] = self.target_dialect

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('dqlTestDatasourceName') is not None:
            self.dql_test_datasource_name = m.get('dqlTestDatasourceName')

        if m.get('sourceDialect') is not None:
            self.source_dialect = m.get('sourceDialect')

        if m.get('targetDialect') is not None:
            self.target_dialect = m.get('targetDialect')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

