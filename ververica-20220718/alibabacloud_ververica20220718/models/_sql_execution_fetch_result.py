# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class SqlExecutionFetchResult(DaraModel):
    def __init__(
        self,
        dql_result: main_models.DqlResult = None,
        sql_execution: main_models.SqlExecution = None,
    ):
        self.dql_result = dql_result
        self.sql_execution = sql_execution

    def validate(self):
        if self.dql_result:
            self.dql_result.validate()
        if self.sql_execution:
            self.sql_execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dql_result is not None:
            result['dqlResult'] = self.dql_result.to_map()

        if self.sql_execution is not None:
            result['sqlExecution'] = self.sql_execution.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dqlResult') is not None:
            temp_model = main_models.DqlResult()
            self.dql_result = temp_model.from_map(m.get('dqlResult'))

        if m.get('sqlExecution') is not None:
            temp_model = main_models.SqlExecution()
            self.sql_execution = temp_model.from_map(m.get('sqlExecution'))

        return self

