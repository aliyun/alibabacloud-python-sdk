# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SingleSqlDryRunRequest(DaraModel):
    def __init__(
        self,
        datasource_name: str = None,
        sql: str = None,
    ):
        # The data source name.
        self.datasource_name = datasource_name
        # The SQL statement.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_name is not None:
            result['datasourceName'] = self.datasource_name

        if self.sql is not None:
            result['sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasourceName') is not None:
            self.datasource_name = m.get('datasourceName')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        return self

