# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, Dict

from darabonba.model import DaraModel

class DescribeSlowQueryStatsResponseBody(DaraModel):
    def __init__(
        self,
        by_database: Any = None,
        by_time_bucket: Any = None,
        by_user: Any = None,
        percentiles: Dict[str, Any] = None,
        request_id: str = None,
        summary: Dict[str, Any] = None,
        top_queries: Any = None,
        top_sql_digests: Any = None,
    ):
        # An array of slow query statistics, grouped by database.
        self.by_database = by_database
        # An array of slow query statistics, grouped by time bucket.
        self.by_time_bucket = by_time_bucket
        # An array of slow query statistics, grouped by user.
        self.by_user = by_user
        # The percentile statistics for query latency.
        self.percentiles = percentiles
        # The request ID.
        self.request_id = request_id
        # The summary of slow query statistics.
        self.summary = summary
        # An array of detailed audit records for the top N slow queries.
        self.top_queries = top_queries
        # An array of statistics for the top N slow queries, grouped by SQL digest. Available for kernel version 5.0 and later.
        self.top_sql_digests = top_sql_digests

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.by_database is not None:
            result['ByDatabase'] = self.by_database

        if self.by_time_bucket is not None:
            result['ByTimeBucket'] = self.by_time_bucket

        if self.by_user is not None:
            result['ByUser'] = self.by_user

        if self.percentiles is not None:
            result['Percentiles'] = self.percentiles

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.top_queries is not None:
            result['TopQueries'] = self.top_queries

        if self.top_sql_digests is not None:
            result['TopSqlDigests'] = self.top_sql_digests

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByDatabase') is not None:
            self.by_database = m.get('ByDatabase')

        if m.get('ByTimeBucket') is not None:
            self.by_time_bucket = m.get('ByTimeBucket')

        if m.get('ByUser') is not None:
            self.by_user = m.get('ByUser')

        if m.get('Percentiles') is not None:
            self.percentiles = m.get('Percentiles')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TopQueries') is not None:
            self.top_queries = m.get('TopQueries')

        if m.get('TopSqlDigests') is not None:
            self.top_sql_digests = m.get('TopSqlDigests')

        return self

