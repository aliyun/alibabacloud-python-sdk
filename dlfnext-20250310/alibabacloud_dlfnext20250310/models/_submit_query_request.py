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
        self.default_catalog = default_catalog
        self.default_database = default_database
        self.limit = limit
        self.sql = sql
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

