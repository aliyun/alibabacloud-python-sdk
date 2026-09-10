# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlTableLineageRequest(DaraModel):
    def __init__(
        self,
        default_schema: str = None,
        dialect: str = None,
        source_sql_script_base_64: str = None,
    ):
        # The default schema (database) name, which is used to complete table references in the SQL script that do not explicitly specify a database name.
        self.default_schema = default_schema
        # The SQL dialect.
        self.dialect = dialect
        # The source script content, Base64-encoded.
        self.source_sql_script_base_64 = source_sql_script_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_schema is not None:
            result['defaultSchema'] = self.default_schema

        if self.dialect is not None:
            result['dialect'] = self.dialect

        if self.source_sql_script_base_64 is not None:
            result['sourceSqlScriptBase64'] = self.source_sql_script_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultSchema') is not None:
            self.default_schema = m.get('defaultSchema')

        if m.get('dialect') is not None:
            self.dialect = m.get('dialect')

        if m.get('sourceSqlScriptBase64') is not None:
            self.source_sql_script_base_64 = m.get('sourceSqlScriptBase64')

        return self

