# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PullLogsRequest(DaraModel):
    def __init__(
        self,
        count: int = None,
        cursor: str = None,
        end_cursor: str = None,
        query: str = None,
    ):
        # This parameter is required.
        self.count = count
        # This parameter is required.
        self.cursor = cursor
        self.end_cursor = end_cursor
        # The SPL statement that is used to filter data. For more information, see [SPL instructions](https://help.aliyun.com/document_detail/2536530.html).
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.end_cursor is not None:
            result['end_cursor'] = self.end_cursor

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('end_cursor') is not None:
            self.end_cursor = m.get('end_cursor')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

