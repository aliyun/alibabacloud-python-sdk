# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSqlTransTableMetaInfoRequest(DaraModel):
    def __init__(
        self,
        source_dialect: str = None,
        source_sql_script: str = None,
        target_dialect: str = None,
    ):
        # The source SQL dialect type.
        self.source_dialect = source_dialect
        # The source script content. You must Base64-encode the script before passing it in. The server decodes the content before parsing.
        self.source_sql_script = source_sql_script
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

        if self.target_dialect is not None:
            result['targetDialect'] = self.target_dialect

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sourceDialect') is not None:
            self.source_dialect = m.get('sourceDialect')

        if m.get('sourceSqlScript') is not None:
            self.source_sql_script = m.get('sourceSqlScript')

        if m.get('targetDialect') is not None:
            self.target_dialect = m.get('targetDialect')

        return self

