# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class PreviewPipelineResponseBody(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        meta: main_models.PreviewPipelineResponseBodyMeta = None,
        request_id: str = None,
    ):
        # The `data` field is a collection of sample rows (an array of maps) that contains only the first N rows (up to 5 by default) and does not reflect the complete write plan.
        self.data = data
        # The query metadata.
        self.meta = meta
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('meta') is not None:
            temp_model = main_models.PreviewPipelineResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class PreviewPipelineResponseBodyMeta(DaraModel):
    def __init__(
        self,
        agg_query: str = None,
        column_types: List[str] = None,
        count: int = None,
        cpu_cores: int = None,
        cpu_sec: float = None,
        elapsed_millisecond: int = None,
        has_sql: bool = None,
        is_accurate: bool = None,
        keys: List[str] = None,
        limited: int = None,
        mode: int = None,
        processed_bytes: int = None,
        processed_rows: int = None,
        progress: str = None,
        scan_bytes: int = None,
        terms: List[Dict[str, Any]] = None,
        where_query: str = None,
    ):
        # The aggregation analysis SPL statement.
        self.agg_query = agg_query
        # The `meta.columnTypes` field provides a mapping from column names to data types (string / long / double / json).
        self.column_types = column_types
        # The number of matched log entries.
        self.count = count
        # The number of CPU cores consumed.
        self.cpu_cores = cpu_cores
        # The CPU time consumed, in seconds.
        self.cpu_sec = cpu_sec
        # The query duration, in milliseconds.
        self.elapsed_millisecond = elapsed_millisecond
        # Indicates whether the query is an SQL query.
        self.has_sql = has_sql
        # Indicates whether nanosecond-level ordering is enabled.
        self.is_accurate = is_accurate
        # The list of result column names.
        self.keys = keys
        # The maximum number of result rows returned.
        self.limited = limited
        # The query mode identifier.
        self.mode = mode
        # The number of processed data bytes.
        self.processed_bytes = processed_bytes
        # The number of processed log rows.
        self.processed_rows = processed_rows
        # The SLS query progress. A value of Complete indicates that the query is complete.
        self.progress = progress
        # The number of raw data bytes scanned.
        self.scan_bytes = scan_bytes
        # The column type and aggregation information.
        self.terms = terms
        # The filter condition SPL statement.
        self.where_query = where_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_query is not None:
            result['aggQuery'] = self.agg_query

        if self.column_types is not None:
            result['columnTypes'] = self.column_types

        if self.count is not None:
            result['count'] = self.count

        if self.cpu_cores is not None:
            result['cpuCores'] = self.cpu_cores

        if self.cpu_sec is not None:
            result['cpuSec'] = self.cpu_sec

        if self.elapsed_millisecond is not None:
            result['elapsedMillisecond'] = self.elapsed_millisecond

        if self.has_sql is not None:
            result['hasSQL'] = self.has_sql

        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate

        if self.keys is not None:
            result['keys'] = self.keys

        if self.limited is not None:
            result['limited'] = self.limited

        if self.mode is not None:
            result['mode'] = self.mode

        if self.processed_bytes is not None:
            result['processedBytes'] = self.processed_bytes

        if self.processed_rows is not None:
            result['processedRows'] = self.processed_rows

        if self.progress is not None:
            result['progress'] = self.progress

        if self.scan_bytes is not None:
            result['scanBytes'] = self.scan_bytes

        if self.terms is not None:
            result['terms'] = self.terms

        if self.where_query is not None:
            result['whereQuery'] = self.where_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggQuery') is not None:
            self.agg_query = m.get('aggQuery')

        if m.get('columnTypes') is not None:
            self.column_types = m.get('columnTypes')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('cpuCores') is not None:
            self.cpu_cores = m.get('cpuCores')

        if m.get('cpuSec') is not None:
            self.cpu_sec = m.get('cpuSec')

        if m.get('elapsedMillisecond') is not None:
            self.elapsed_millisecond = m.get('elapsedMillisecond')

        if m.get('hasSQL') is not None:
            self.has_sql = m.get('hasSQL')

        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('limited') is not None:
            self.limited = m.get('limited')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('processedBytes') is not None:
            self.processed_bytes = m.get('processedBytes')

        if m.get('processedRows') is not None:
            self.processed_rows = m.get('processedRows')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('scanBytes') is not None:
            self.scan_bytes = m.get('scanBytes')

        if m.get('terms') is not None:
            self.terms = m.get('terms')

        if m.get('whereQuery') is not None:
            self.where_query = m.get('whereQuery')

        return self

