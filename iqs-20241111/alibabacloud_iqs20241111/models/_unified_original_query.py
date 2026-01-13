# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnifiedOriginalQuery(DaraModel):
    def __init__(
        self,
        query: str = None,
        time_range: str = None,
    ):
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['query'] = self.query

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

