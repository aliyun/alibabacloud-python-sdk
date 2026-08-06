# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitQueryRequest(DaraModel):
    def __init__(
        self,
        default_catalog: str = None,
        default_database: str = None,
        limit: int = None,
        sql: str = None,
        tier: str = None,
    ):
        # The default catalog.
        self.default_catalog = default_catalog
        # The default database.
        self.default_database = default_database
        # The limit on the number of returned results.
        self.limit = limit
        # The SQL text. Multiple statements separated by semicolons are supported and executed sequentially within the same session.
        self.sql = sql
        # The execution specifications. Default value: standard.
        self.tier = tier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_catalog is not None:
            result['defaultCatalog'] = self.default_catalog

        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database

        if self.limit is not None:
            result['limit'] = self.limit

        if self.sql is not None:
            result['sql'] = self.sql

        if self.tier is not None:
            result['tier'] = self.tier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultCatalog') is not None:
            self.default_catalog = m.get('defaultCatalog')

        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('sql') is not None:
            self.sql = m.get('sql')

        if m.get('tier') is not None:
            self.tier = m.get('tier')

        return self

