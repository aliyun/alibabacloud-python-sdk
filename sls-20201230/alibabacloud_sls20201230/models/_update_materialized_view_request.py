# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMaterializedViewRequest(DaraModel):
    def __init__(
        self,
        agg_interval_mins: int = None,
        enable: bool = None,
        original_sql: str = None,
        ttl: int = None,
    ):
        self.agg_interval_mins = agg_interval_mins
        self.enable = enable
        self.original_sql = original_sql
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_interval_mins is not None:
            result['aggIntervalMins'] = self.agg_interval_mins

        if self.enable is not None:
            result['enable'] = self.enable

        if self.original_sql is not None:
            result['originalSql'] = self.original_sql

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggIntervalMins') is not None:
            self.agg_interval_mins = m.get('aggIntervalMins')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('originalSql') is not None:
            self.original_sql = m.get('originalSql')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

