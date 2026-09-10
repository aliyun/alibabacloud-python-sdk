# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ExecSqlTransSingleScriptTranslateRequest(DaraModel):
    def __init__(
        self,
        source_dialect: str = None,
        source_sql_script: str = None,
        table_mapping: List[str] = None,
        target_dialect: str = None,
    ):
        # The source SQL dialect type.
        self.source_dialect = source_dialect
        # The source script content. It must be Base64-encoded before being passed in. The server decodes the content before performing the conversion.
        self.source_sql_script = source_sql_script
        # The table name mapping. In string format, the source table and target table are separated by a comma (,).
        self.table_mapping = table_mapping
        # The target SQL dialect type.
        self.target_dialect = target_dialect

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_dialect is not None:
            result['sourceDialect'] = self.source_dialect

        if self.source_sql_script is not None:
            result['sourceSqlScript'] = self.source_sql_script

        if self.table_mapping is not None:
            result['tableMapping'] = self.table_mapping

        if self.target_dialect is not None:
            result['targetDialect'] = self.target_dialect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDialect') is not None:
            self.source_dialect = m.get('sourceDialect')

        if m.get('sourceSqlScript') is not None:
            self.source_sql_script = m.get('sourceSqlScript')

        if m.get('tableMapping') is not None:
            self.table_mapping = m.get('tableMapping')

        if m.get('targetDialect') is not None:
            self.target_dialect = m.get('targetDialect')

        return self

