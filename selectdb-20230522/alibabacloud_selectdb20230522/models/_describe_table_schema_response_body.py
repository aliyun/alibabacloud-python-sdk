# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTableSchemaResponseBody(DaraModel):
    def __init__(
        self,
        create_statement: str = None,
        database: str = None,
        request_id: str = None,
        table: str = None,
    ):
        # The CREATE TABLE statement.
        self.create_statement = create_statement
        # The database name.
        self.database = database
        # The request ID.
        self.request_id = request_id
        # The table name.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_statement is not None:
            result['CreateStatement'] = self.create_statement

        if self.database is not None:
            result['Database'] = self.database

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateStatement') is not None:
            self.create_statement = m.get('CreateStatement')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

