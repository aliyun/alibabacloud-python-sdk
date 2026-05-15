# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ExecuteStatementRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        max_bytes: int = None,
        max_rows: int = None,
        parameters: List[Any] = None,
        query_timeout: int = None,
        sql: str = None,
    ):
        self.db_name = db_name
        self.max_bytes = max_bytes
        self.max_rows = max_rows
        self.parameters = parameters
        self.query_timeout = query_timeout
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.max_bytes is not None:
            result['maxBytes'] = self.max_bytes

        if self.max_rows is not None:
            result['maxRows'] = self.max_rows

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.query_timeout is not None:
            result['queryTimeout'] = self.query_timeout

        if self.sql is not None:
            result['sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('maxBytes') is not None:
            self.max_bytes = m.get('maxBytes')

        if m.get('maxRows') is not None:
            self.max_rows = m.get('maxRows')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('queryTimeout') is not None:
            self.query_timeout = m.get('queryTimeout')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        return self

