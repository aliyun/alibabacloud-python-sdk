# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCursorTimeRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
    ):
        # The cursor for which you want to obtain the timestamp. Call the [GetCursor](https://help.aliyun.com/document_detail/2771314.html) operation to obtain a cursor.
        # 
        # > If the value of the cursor is less than the begin cursor or greater than the end cursor, InvalidCursor is returned. If the shard contains no data, the current time is returned.
        # 
        # This parameter is required.
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        return self

