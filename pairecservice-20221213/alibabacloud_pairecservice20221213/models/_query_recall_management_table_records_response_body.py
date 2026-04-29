# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class QueryRecallManagementTableRecordsResponseBody(DaraModel):
    def __init__(
        self,
        records: List[Dict[str, Any]] = None,
        request_id: str = None,
    ):
        self.records = records
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.records is not None:
            result['Records'] = self.records

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            self.records = m.get('Records')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

