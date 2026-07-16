# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContextsRequest(DaraModel):
    def __init__(
        self,
        context_ids: str = None,
        filter: str = None,
    ):
        # A comma-separated list of context IDs.
        self.context_ids = context_ids
        # The filter condition, specified as a JSON string in the query. The syntax is the same as the `filter` parameter of the `SearchContext` operation.
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_ids is not None:
            result['contextIds'] = self.context_ids

        if self.filter is not None:
            result['filter'] = self.filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextIds') is not None:
            self.context_ids = m.get('contextIds')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        return self

