# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDatasourceTablesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tables: List[str] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tables = tables
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

