# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCursorTimeResponseBody(DaraModel):
    def __init__(
        self,
        cursor_time: str = None,
    ):
        # The server time that corresponds to the cursor. The value is a UNIX timestamp. A UNIX timestamp represents the number of seconds that have elapsed since 1970-01-01 00:00:00 UTC.
        self.cursor_time = cursor_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor_time is not None:
            result['cursor_time'] = self.cursor_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor_time') is not None:
            self.cursor_time = m.get('cursor_time')

        return self

