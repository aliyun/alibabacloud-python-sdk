# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchInformation(DaraModel):
    def __init__(
        self,
        search_time: int = None,
        total: int = None,
    ):
        self.search_time = search_time
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_time is not None:
            result['searchTime'] = self.search_time

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchTime') is not None:
            self.search_time = m.get('searchTime')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

