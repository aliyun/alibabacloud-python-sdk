# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetMaterializedViewResponseBody(DaraModel):
    def __init__(
        self,
        agg_interval_mins: int = None,
        create_time: int = None,
        enabled: bool = None,
        logstore: str = None,
        name: str = None,
        original_sql: str = None,
        shard_count: int = None,
        start_time: int = None,
        status: main_models.GetMaterializedViewResponseBodyStatus = None,
        ttl: int = None,
    ):
        # The aggregation interval of the materialized view results, in minutes.
        self.agg_interval_mins = agg_interval_mins
        # The time when the materialized view was created.
        self.create_time = create_time
        # Indicates whether the materialized view is enabled.
        self.enabled = enabled
        # The Logstore from which the materialized view sources its data.
        self.logstore = logstore
        # Id of the request
        self.name = name
        # The original SQL statement executed by the materialized view.
        self.original_sql = original_sql
        # The number of shards used by the Logstore that stores the materialized view data.
        self.shard_count = shard_count
        # The time from which the materialized view starts processing data.
        self.start_time = start_time
        # The status information of the materialized view.
        self.status = status
        # The number of days that the materialized view results are retained.
        self.ttl = ttl

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_interval_mins is not None:
            result['aggIntervalMins'] = self.agg_interval_mins

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.name is not None:
            result['name'] = self.name

        if self.original_sql is not None:
            result['originalSql'] = self.original_sql

        if self.shard_count is not None:
            result['shardCount'] = self.shard_count

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.ttl is not None:
            result['ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggIntervalMins') is not None:
            self.agg_interval_mins = m.get('aggIntervalMins')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('originalSql') is not None:
            self.original_sql = m.get('originalSql')

        if m.get('shardCount') is not None:
            self.shard_count = m.get('shardCount')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            temp_model = main_models.GetMaterializedViewResponseBodyStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')

        return self

class GetMaterializedViewResponseBodyStatus(DaraModel):
    def __init__(
        self,
        last_run_error: str = None,
        last_run_time: int = None,
        max_cursor_time: int = None,
        stats: main_models.GetMaterializedViewResponseBodyStatusStats = None,
    ):
        # The error message from the last execution of the materialized view.
        self.last_run_error = last_run_error
        # The time when the materialized view was last executed.
        self.last_run_time = last_run_time
        # The latest position up to which the materialized view has processed data.
        self.max_cursor_time = max_cursor_time
        # The execute statistics information of the materialized view.
        self.stats = stats

    def validate(self):
        if self.stats:
            self.stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_run_error is not None:
            result['lastRunError'] = self.last_run_error

        if self.last_run_time is not None:
            result['lastRunTime'] = self.last_run_time

        if self.max_cursor_time is not None:
            result['maxCursorTime'] = self.max_cursor_time

        if self.stats is not None:
            result['stats'] = self.stats.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastRunError') is not None:
            self.last_run_error = m.get('lastRunError')

        if m.get('lastRunTime') is not None:
            self.last_run_time = m.get('lastRunTime')

        if m.get('maxCursorTime') is not None:
            self.max_cursor_time = m.get('maxCursorTime')

        if m.get('stats') is not None:
            temp_model = main_models.GetMaterializedViewResponseBodyStatusStats()
            self.stats = temp_model.from_map(m.get('stats'))

        return self

class GetMaterializedViewResponseBodyStatusStats(DaraModel):
    def __init__(
        self,
        hits: int = None,
        queries: List[str] = None,
    ):
        # The number of times the materialized view was used in the last day.
        self.hits = hits
        # The top 3 most frequently accelerated SQL statements by the materialized view.
        self.queries = queries

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hits is not None:
            result['hits'] = self.hits

        if self.queries is not None:
            result['queries'] = self.queries

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hits') is not None:
            self.hits = m.get('hits')

        if m.get('queries') is not None:
            self.queries = m.get('queries')

        return self

