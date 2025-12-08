# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConversationsRequest(DaraModel):
    def __init__(
        self,
        last_id: str = None,
        limit: str = None,
        pinned: str = None,
        sort_by: str = None,
    ):
        self.last_id = last_id
        self.limit = limit
        self.pinned = pinned
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_id is not None:
            result['LastId'] = self.last_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.pinned is not None:
            result['Pinned'] = self.pinned

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastId') is not None:
            self.last_id = m.get('LastId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Pinned') is not None:
            self.pinned = m.get('Pinned')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

