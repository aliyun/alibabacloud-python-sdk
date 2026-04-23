# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchInventoryKnowledgeRequest(DaraModel):
    def __init__(
        self,
        job_id: int = None,
        offset: int = None,
        query: str = None,
        show_type: str = None,
        size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id
        self.offset = offset
        self.query = query
        self.show_type = show_type
        self.size = size
        self.sort_by = sort_by
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.query is not None:
            result['Query'] = self.query

        if self.show_type is not None:
            result['ShowType'] = self.show_type

        if self.size is not None:
            result['Size'] = self.size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ShowType') is not None:
            self.show_type = m.get('ShowType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

