# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAsyncSqlRequest(DaraModel):
    def __init__(
        self,
        line: int = None,
        offset: int = None,
    ):
        # The number of results to return per page. The maximum value is 1000.
        self.line = line
        # The offset for paginated results.
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['line'] = self.line

        if self.offset is not None:
            result['offset'] = self.offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('line') is not None:
            self.line = m.get('line')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        return self

