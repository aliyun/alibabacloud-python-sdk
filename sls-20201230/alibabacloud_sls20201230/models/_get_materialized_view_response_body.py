# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMaterializedViewResponseBody(DaraModel):
    def __init__(
        self,
        agg_interval_mins: int = None,
        enabled: bool = None,
        logstore: str = None,
        name: str = None,
        original_sql: str = None,
        start_time: int = None,
        ttl: int = None,
    ):
        self.agg_interval_mins = agg_interval_mins
        self.enabled = enabled
        self.logstore = logstore
        self.name = name
        self.original_sql = original_sql
        self.start_time = start_time
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

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.name is not None:
            result['name'] = self.name

        if self.original_sql is not None:
            result['originalSql'] = self.original_sql

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggIntervalMins') is not None:
            self.agg_interval_mins = m.get('aggIntervalMins')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('originalSql') is not None:
            self.original_sql = m.get('originalSql')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

