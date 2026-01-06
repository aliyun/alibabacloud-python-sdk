# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SparkBatchSQL(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        err_message: str = None,
        query: str = None,
        query_end_time: int = None,
        query_id: str = None,
        query_start_time: int = None,
        query_state: str = None,
        query_submission_time: int = None,
        resource_group_name: str = None,
        schema: str = None,
        statements: List[main_models.SparkBatchSQLStatement] = None,
        uid: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.err_message = err_message
        self.query = query
        self.query_end_time = query_end_time
        self.query_id = query_id
        self.query_start_time = query_start_time
        self.query_state = query_state
        self.query_submission_time = query_submission_time
        self.resource_group_name = resource_group_name
        self.schema = schema
        self.statements = statements
        self.uid = uid

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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.query is not None:
            result['Query'] = self.query

        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.query_state is not None:
            result['QueryState'] = self.query_state

        if self.query_submission_time is not None:
            result['QuerySubmissionTime'] = self.query_submission_time

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.schema is not None:
            result['Schema'] = self.schema

        result['Statements'] = []
        if self.statements is not None:
            for k1 in self.statements:
                result['Statements'].append(k1.to_map() if k1 else None)

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('QueryState') is not None:
            self.query_state = m.get('QueryState')

        if m.get('QuerySubmissionTime') is not None:
            self.query_submission_time = m.get('QuerySubmissionTime')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        self.statements = []
        if m.get('Statements') is not None:
            for k1 in m.get('Statements'):
                temp_model = main_models.SparkBatchSQLStatement()
                self.statements.append(temp_model.from_map(k1))

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

