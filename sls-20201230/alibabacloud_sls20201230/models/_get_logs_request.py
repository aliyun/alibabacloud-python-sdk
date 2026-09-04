# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLogsRequest(DaraModel):
    def __init__(
        self,
        forward: bool = None,
        from_: int = None,
        highlight: bool = None,
        is_accurate: bool = None,
        line: int = None,
        offset: int = None,
        power_sql: bool = None,
        query: str = None,
        reverse: bool = None,
        session: str = None,
        to: int = None,
        topic: str = None,
    ):
        self.forward = forward
        # This parameter is required.
        self.from_ = from_
        self.highlight = highlight
        self.is_accurate = is_accurate
        self.line = line
        self.offset = offset
        self.power_sql = power_sql
        self.query = query
        self.reverse = reverse
        self.session = session
        # This parameter is required.
        self.to = to
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward is not None:
            result['forward'] = self.forward

        if self.from_ is not None:
            result['from'] = self.from_

        if self.highlight is not None:
            result['highlight'] = self.highlight

        if self.is_accurate is not None:
            result['isAccurate'] = self.is_accurate

        if self.line is not None:
            result['line'] = self.line

        if self.offset is not None:
            result['offset'] = self.offset

        if self.power_sql is not None:
            result['powerSql'] = self.power_sql

        if self.query is not None:
            result['query'] = self.query

        if self.reverse is not None:
            result['reverse'] = self.reverse

        if self.session is not None:
            result['session'] = self.session

        if self.to is not None:
            result['to'] = self.to

        if self.topic is not None:
            result['topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forward') is not None:
            self.forward = m.get('forward')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('highlight') is not None:
            self.highlight = m.get('highlight')

        if m.get('isAccurate') is not None:
            self.is_accurate = m.get('isAccurate')

        if m.get('line') is not None:
            self.line = m.get('line')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('reverse') is not None:
            self.reverse = m.get('reverse')

        if m.get('session') is not None:
            self.session = m.get('session')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        return self

