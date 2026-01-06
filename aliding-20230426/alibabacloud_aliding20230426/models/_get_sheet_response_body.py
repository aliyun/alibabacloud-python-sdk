# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSheetResponseBody(DaraModel):
    def __init__(
        self,
        column_count: int = None,
        id: str = None,
        last_non_empty_column: int = None,
        last_non_empty_row: int = None,
        name: str = None,
        request_id: str = None,
        row_count: int = None,
        visibility: str = None,
    ):
        self.column_count = column_count
        self.id = id
        self.last_non_empty_column = last_non_empty_column
        self.last_non_empty_row = last_non_empty_row
        self.name = name
        # requestId
        self.request_id = request_id
        self.row_count = row_count
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_count is not None:
            result['columnCount'] = self.column_count

        if self.id is not None:
            result['id'] = self.id

        if self.last_non_empty_column is not None:
            result['lastNonEmptyColumn'] = self.last_non_empty_column

        if self.last_non_empty_row is not None:
            result['lastNonEmptyRow'] = self.last_non_empty_row

        if self.name is not None:
            result['name'] = self.name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.row_count is not None:
            result['rowCount'] = self.row_count

        if self.visibility is not None:
            result['visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnCount') is not None:
            self.column_count = m.get('columnCount')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastNonEmptyColumn') is not None:
            self.last_non_empty_column = m.get('lastNonEmptyColumn')

        if m.get('lastNonEmptyRow') is not None:
            self.last_non_empty_row = m.get('lastNonEmptyRow')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('rowCount') is not None:
            self.row_count = m.get('rowCount')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

