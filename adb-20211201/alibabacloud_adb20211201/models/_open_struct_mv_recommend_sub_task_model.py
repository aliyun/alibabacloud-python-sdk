# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructMvRecommendSubTaskModel(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        min_rewrite_query_count: int = None,
        min_rewrite_query_pattern: int = None,
        scan_queries_count: int = None,
        slow_query_threshold: int = None,
        start_time: str = None,
        status: str = None,
        sub_queries_count: int = None,
        subtask_id: int = None,
    ):
        self.end_time = end_time
        self.min_rewrite_query_count = min_rewrite_query_count
        self.min_rewrite_query_pattern = min_rewrite_query_pattern
        self.scan_queries_count = scan_queries_count
        self.slow_query_threshold = slow_query_threshold
        self.start_time = start_time
        self.status = status
        self.sub_queries_count = sub_queries_count
        self.subtask_id = subtask_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.min_rewrite_query_count is not None:
            result['MinRewriteQueryCount'] = self.min_rewrite_query_count

        if self.min_rewrite_query_pattern is not None:
            result['MinRewriteQueryPattern'] = self.min_rewrite_query_pattern

        if self.scan_queries_count is not None:
            result['ScanQueriesCount'] = self.scan_queries_count

        if self.slow_query_threshold is not None:
            result['SlowQueryThreshold'] = self.slow_query_threshold

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_queries_count is not None:
            result['SubQueriesCount'] = self.sub_queries_count

        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MinRewriteQueryCount') is not None:
            self.min_rewrite_query_count = m.get('MinRewriteQueryCount')

        if m.get('MinRewriteQueryPattern') is not None:
            self.min_rewrite_query_pattern = m.get('MinRewriteQueryPattern')

        if m.get('ScanQueriesCount') is not None:
            self.scan_queries_count = m.get('ScanQueriesCount')

        if m.get('SlowQueryThreshold') is not None:
            self.slow_query_threshold = m.get('SlowQueryThreshold')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubQueriesCount') is not None:
            self.sub_queries_count = m.get('SubQueriesCount')

        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')

        return self

