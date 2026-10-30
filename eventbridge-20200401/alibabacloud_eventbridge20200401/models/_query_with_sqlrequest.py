# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWithSQLRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        query: str = None,
    ):
        # The number of entries to return. Default value: 20. Maximum value: 50.
        self.limit = limit
        # The query statement. Typically, a three-part table name in the format of catalog.namespace.table is used.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

