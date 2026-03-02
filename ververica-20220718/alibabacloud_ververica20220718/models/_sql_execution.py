# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SqlExecution(DaraModel):
    def __init__(
        self,
        batch_mode: bool = None,
        description: str = None,
        message: str = None,
        name: str = None,
        namespace: str = None,
        session_cluster_name: str = None,
        sql_execution_id: str = None,
        sql_file_id: str = None,
        sql_script: str = None,
        state: str = None,
        statements: List[main_models.SqlStatement] = None,
        workspace: str = None,
    ):
        self.batch_mode = batch_mode
        self.description = description
        self.message = message
        self.name = name
        self.namespace = namespace
        self.session_cluster_name = session_cluster_name
        self.sql_execution_id = sql_execution_id
        self.sql_file_id = sql_file_id
        self.sql_script = sql_script
        self.state = state
        self.statements = statements
        self.workspace = workspace

    def validate(self):
        if self.statements:
            for v1 in self.statements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_mode is not None:
            result['batchMode'] = self.batch_mode

        if self.description is not None:
            result['description'] = self.description

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name

        if self.sql_execution_id is not None:
            result['sqlExecutionId'] = self.sql_execution_id

        if self.sql_file_id is not None:
            result['sqlFileId'] = self.sql_file_id

        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script

        if self.state is not None:
            result['state'] = self.state

        result['statements'] = []
        if self.statements is not None:
            for k1 in self.statements:
                result['statements'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchMode') is not None:
            self.batch_mode = m.get('batchMode')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')

        if m.get('sqlExecutionId') is not None:
            self.sql_execution_id = m.get('sqlExecutionId')

        if m.get('sqlFileId') is not None:
            self.sql_file_id = m.get('sqlFileId')

        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')

        if m.get('state') is not None:
            self.state = m.get('state')

        self.statements = []
        if m.get('statements') is not None:
            for k1 in m.get('statements'):
                temp_model = main_models.SqlStatement()
                self.statements.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

