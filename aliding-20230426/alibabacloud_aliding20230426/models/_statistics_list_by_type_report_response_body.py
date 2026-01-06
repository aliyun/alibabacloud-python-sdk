# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StatisticsListByTypeReportResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        next_cursor: int = None,
        request_id: str = None,
        userid_list: List[str] = None,
    ):
        self.has_more = has_more
        self.next_cursor = next_cursor
        # requestId
        self.request_id = request_id
        self.userid_list = userid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.userid_list is not None:
            result['useridList'] = self.userid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('useridList') is not None:
            self.userid_list = m.get('useridList')

        return self

