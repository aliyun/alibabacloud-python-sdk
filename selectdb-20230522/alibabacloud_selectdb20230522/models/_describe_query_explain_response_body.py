# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQueryExplainResponseBody(DaraModel):
    def __init__(
        self,
        explain_result: str = None,
        request_id: str = None,
        sql: str = None,
    ):
        # The Explain result.
        self.explain_result = explain_result
        # The request ID.
        self.request_id = request_id
        # The SQL statement for which the execution plan is retrieved. Excessively long SQL statements in audit logs may be truncated.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.explain_result is not None:
            result['ExplainResult'] = self.explain_result

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sql is not None:
            result['Sql'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExplainResult') is not None:
            self.explain_result = m.get('ExplainResult')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        return self

