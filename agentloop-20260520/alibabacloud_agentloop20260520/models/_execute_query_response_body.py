# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ExecuteQueryResponseBody(DaraModel):
    def __init__(
        self,
        column_types: List[str] = None,
        columns: List[str] = None,
        meta: main_models.ExecuteQueryResponseBodyMeta = None,
        request_id: str = None,
        rows: List[List[Any]] = None,
    ):
        self.column_types = column_types
        self.columns = columns
        self.meta = meta
        self.request_id = request_id
        self.rows = rows

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_types is not None:
            result['columnTypes'] = self.column_types

        if self.columns is not None:
            result['columns'] = self.columns

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.rows is not None:
            result['rows'] = self.rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnTypes') is not None:
            self.column_types = m.get('columnTypes')

        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('meta') is not None:
            temp_model = main_models.ExecuteQueryResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('rows') is not None:
            self.rows = m.get('rows')

        return self

class ExecuteQueryResponseBodyMeta(DaraModel):
    def __init__(
        self,
        affected_rows: int = None,
        count: int = None,
        elapsed_millisecond: int = None,
        progress: str = None,
    ):
        self.affected_rows = affected_rows
        self.count = count
        self.elapsed_millisecond = elapsed_millisecond
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_rows is not None:
            result['affectedRows'] = self.affected_rows

        if self.count is not None:
            result['count'] = self.count

        if self.elapsed_millisecond is not None:
            result['elapsedMillisecond'] = self.elapsed_millisecond

        if self.progress is not None:
            result['progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedRows') is not None:
            self.affected_rows = m.get('affectedRows')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('elapsedMillisecond') is not None:
            self.elapsed_millisecond = m.get('elapsedMillisecond')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        return self

