# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructMvRecommendTaskModel(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        last_run_at: str = None,
        min_rewrite_query_count: int = None,
        min_rewrite_query_pattern: int = None,
        scan_queries_range: int = None,
        scheduling_settings: str = None,
        slow_query_threshold: int = None,
        task_name: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.last_run_at = last_run_at
        self.min_rewrite_query_count = min_rewrite_query_count
        self.min_rewrite_query_pattern = min_rewrite_query_pattern
        self.scan_queries_range = scan_queries_range
        self.scheduling_settings = scheduling_settings
        self.slow_query_threshold = slow_query_threshold
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.last_run_at is not None:
            result['LastRunAt'] = self.last_run_at

        if self.min_rewrite_query_count is not None:
            result['MinRewriteQueryCount'] = self.min_rewrite_query_count

        if self.min_rewrite_query_pattern is not None:
            result['MinRewriteQueryPattern'] = self.min_rewrite_query_pattern

        if self.scan_queries_range is not None:
            result['ScanQueriesRange'] = self.scan_queries_range

        if self.scheduling_settings is not None:
            result['SchedulingSettings'] = self.scheduling_settings

        if self.slow_query_threshold is not None:
            result['SlowQueryThreshold'] = self.slow_query_threshold

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LastRunAt') is not None:
            self.last_run_at = m.get('LastRunAt')

        if m.get('MinRewriteQueryCount') is not None:
            self.min_rewrite_query_count = m.get('MinRewriteQueryCount')

        if m.get('MinRewriteQueryPattern') is not None:
            self.min_rewrite_query_pattern = m.get('MinRewriteQueryPattern')

        if m.get('ScanQueriesRange') is not None:
            self.scan_queries_range = m.get('ScanQueriesRange')

        if m.get('SchedulingSettings') is not None:
            self.scheduling_settings = m.get('SchedulingSettings')

        if m.get('SlowQueryThreshold') is not None:
            self.slow_query_threshold = m.get('SlowQueryThreshold')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

