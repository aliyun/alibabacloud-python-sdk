# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAdvancedQueryHistoryResponseBody(DaraModel):
    def __init__(
        self,
        dry_run_result: str = None,
        query_id: str = None,
        query_sql: str = None,
        request_id: str = None,
        simple_query: bool = None,
    ):
        self.dry_run_result = dry_run_result
        # The ID of the advanced event query record.
        self.query_id = query_id
        # The advanced event query statement.
        self.query_sql = query_sql
        # The request ID.
        self.request_id = request_id
        # Specifies whether to enable the simple query mode.
        self.simple_query = simple_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.query_sql is not None:
            result['QuerySql'] = self.query_sql

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.simple_query is not None:
            result['SimpleQuery'] = self.simple_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            self.dry_run_result = m.get('DryRunResult')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('QuerySql') is not None:
            self.query_sql = m.get('QuerySql')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SimpleQuery') is not None:
            self.simple_query = m.get('SimpleQuery')

        return self

