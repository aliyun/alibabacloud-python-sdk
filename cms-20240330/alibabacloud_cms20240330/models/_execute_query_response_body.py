# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ExecuteQueryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, str]] = None,
        meta: main_models.ExecuteQueryResponseBodyMeta = None,
        request_id: str = None,
    ):
        self.data = data
        self.meta = meta
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
            temp_model = main_models.ExecuteQueryResponseBodyMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

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

