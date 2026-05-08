# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCreateTableSQLResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
        sql: str = None,
    ):
        # The detailed reason why the access was denied.
        self.access_denied_detail = access_denied_detail
        # The request ID.
        self.request_id = request_id
        # The SQL statement.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sql is not None:
            result['SQL'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        return self

