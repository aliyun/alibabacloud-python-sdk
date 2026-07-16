# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInventoryJobsRequest(DaraModel):
    def __init__(
        self,
        offset: int = None,
        query: str = None,
        size: int = None,
        sort_by: str = None,
        sort_order: str = None,
        status: int = None,
    ):
        self.offset = offset
        self.query = query
        self.size = size
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        if self.query is not None:
            result['Query'] = self.query

        if self.size is not None:
            result['Size'] = self.size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

