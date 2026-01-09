# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetLogsV2ResponseBody(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        meta: main_models.GetLogsV2ResponseBodyMeta = None,
    ):
        # The returned result.
        self.data = data
        # The metadata of the returned data.
        self.meta = meta

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('meta') is not None:
            temp_model = main_models.GetLogsV2ResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        return self

class GetLogsV2ResponseBodyMeta(DaraModel):
    def __init__(
        self,
        agg_query: str = None,
        column_types: List[str] = None,
        count: int = None,
        cpu_cores: int = None,
        cpu_sec: float = None,
        elapsed_millisecond: int = None,
        has_sql: bool = None,
        highlights: List[List[main_models.LogContent]] = None,
        is_accurate: bool = None,
        keys: List[str] = None,
        limited: int = None,
        mode: int = None,
        phrase_query_info: main_models.GetLogsV2ResponseBodyMetaPhraseQueryInfo = None,
        processed_bytes: int = None,
        processed_rows: int = None,
        progress: str = None,
        scan_bytes: int = None,
        telementry_type: str = None,
        terms: List[Dict[str, Any]] = None,
        where_query: str = None,
    ):
        # The SQL statement after | in the query statement.
        self.agg_query = agg_query
        self.column_types = column_types
        # The number of rows that are returned.
        self.count = count
        self.cpu_cores = cpu_cores
        self.cpu_sec = cpu_sec
        # The amount of time that is consumed by the request. Unit: milliseconds.
        self.elapsed_millisecond = elapsed_millisecond
        # Indicates whether the query is an SQL query.
        self.has_sql = has_sql
        self.highlights = highlights
        # Indicates whether the returned result is accurate to seconds.
        self.is_accurate = is_accurate
        # All keys in the query result.
        self.keys = keys
        self.limited = limited
        self.mode = mode
        self.phrase_query_info = phrase_query_info
        # The number of logs that are processed in the request.
        self.processed_bytes = processed_bytes
        # The number of rows that are processed in the query.
        self.processed_rows = processed_rows
        # Indicates whether the query result is complete. Valid values:
        # 
        # *   Complete: The query was successful, and the complete result is returned.
        # *   Incomplete: The query was successful, but the query result is incomplete. To obtain the complete result, you must call the operation again.
        self.progress = progress
        self.scan_bytes = scan_bytes
        # The type of observable data.
        self.telementry_type = telementry_type
        # All terms in the query statement.
        self.terms = terms
        # The part before | in the query statement.
        self.where_query = where_query

    def validate(self):
        if self.highlights:
            for v1 in self.highlights:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.phrase_query_info:
            self.phrase_query_info.validate()

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

        result['highlights'] = []
        if self.highlights is not None:
            for k1 in self.highlights:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['highlights'].append(l1)

        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate

        if self.keys is not None:
            result['keys'] = self.keys

        if self.limited is not None:
            result['limited'] = self.limited

        if self.mode is not None:
            result['mode'] = self.mode

        if self.phrase_query_info is not None:
            result['phraseQueryInfo'] = self.phrase_query_info.to_map()

        if self.processed_bytes is not None:
            result['processedBytes'] = self.processed_bytes

        if self.processed_rows is not None:
            result['processedRows'] = self.processed_rows

        if self.progress is not None:
            result['progress'] = self.progress

        if self.scan_bytes is not None:
            result['scanBytes'] = self.scan_bytes

        if self.telementry_type is not None:
            result['telementryType'] = self.telementry_type

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

        self.highlights = []
        if m.get('highlights') is not None:
            for k1 in m.get('highlights'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.LogContent()
                    l1.append(temp_model.from_map(k2))
                self.highlights.append(l1)

        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('limited') is not None:
            self.limited = m.get('limited')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('phraseQueryInfo') is not None:
            temp_model = main_models.GetLogsV2ResponseBodyMetaPhraseQueryInfo()
            self.phrase_query_info = temp_model.from_map(m.get('phraseQueryInfo'))

        if m.get('processedBytes') is not None:
            self.processed_bytes = m.get('processedBytes')

        if m.get('processedRows') is not None:
            self.processed_rows = m.get('processedRows')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('scanBytes') is not None:
            self.scan_bytes = m.get('scanBytes')

        if m.get('telementryType') is not None:
            self.telementry_type = m.get('telementryType')

        if m.get('terms') is not None:
            self.terms = m.get('terms')

        if m.get('whereQuery') is not None:
            self.where_query = m.get('whereQuery')

        return self

class GetLogsV2ResponseBodyMetaPhraseQueryInfo(DaraModel):
    def __init__(
        self,
        begin_offset: int = None,
        end_offset: int = None,
        end_time: int = None,
        scan_all: bool = None,
    ):
        self.begin_offset = begin_offset
        self.end_offset = end_offset
        self.end_time = end_time
        self.scan_all = scan_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_offset is not None:
            result['beginOffset'] = self.begin_offset

        if self.end_offset is not None:
            result['endOffset'] = self.end_offset

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.scan_all is not None:
            result['scanAll'] = self.scan_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginOffset') is not None:
            self.begin_offset = m.get('beginOffset')

        if m.get('endOffset') is not None:
            self.end_offset = m.get('endOffset')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('scanAll') is not None:
            self.scan_all = m.get('scanAll')

        return self

