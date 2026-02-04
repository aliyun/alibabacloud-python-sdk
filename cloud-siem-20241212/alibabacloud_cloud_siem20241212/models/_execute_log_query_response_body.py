# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ExecuteLogQueryResponseBody(DaraModel):
    def __init__(
        self,
        query_result: List[Any] = None,
        request_id: str = None,
    ):
        self.query_result = query_result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_result is not None:
            result['QueryResult'] = self.query_result

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryResult') is not None:
            self.query_result = m.get('QueryResult')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

