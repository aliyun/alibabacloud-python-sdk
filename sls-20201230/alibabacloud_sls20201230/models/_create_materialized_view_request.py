# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMaterializedViewRequest(DaraModel):
    def __init__(
        self,
        agg_interval_mins: int = None,
        logstore: str = None,
        name: str = None,
        original_sql: str = None,
        start_time: int = None,
        ttl: int = None,
    ):
        # The aggregation interval in minutes. The system creates aggregation tasks based on this interval.
        self.agg_interval_mins = agg_interval_mins
        # The destination Logstore for the aggregated data from the materialized view.
        self.logstore = logstore
        # The name of the materialized view. The name must be unique within the project, 2 to 63 characters long, and contain only lowercase letters, digits, hyphens (-), and underscores (_). It must also start and end with a lowercase letter or a digit.
        self.name = name
        # The query statement that defines the materialized view.
        self.original_sql = original_sql
        # The time when the materialized view starts to aggregate data. Specify the time as a UNIX timestamp in seconds.
        self.start_time = start_time
        # The time-to-live (TTL) of the data in the materialized view, in days. After this period, the data expires and is automatically deleted.
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

