# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEntityStoreDataRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        query: str = None,
        to: int = None,
    ):
        # The start point in time for the query.
        # 
        # This is a UNIX timestamp. It represents the number of seconds that have elapsed since 00:00:00 UTC on January 1, 1970.
        # 
        # This parameter is required.
        self.from_ = from_
        # The search statement.
        # 
        # This parameter is required.
        self.query = query
        # The end point in time for the query.
        # 
        # This is a UNIX timestamp. It represents the number of seconds that have elapsed since 00:00:00 UTC on January 1, 1970.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.query is not None:
            result['query'] = self.query

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

