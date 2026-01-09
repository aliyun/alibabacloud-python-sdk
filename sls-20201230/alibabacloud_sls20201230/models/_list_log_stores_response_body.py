# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLogStoresResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        logstores: List[str] = None,
        total: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The Logstores that meet the query conditions.
        self.logstores = logstores
        # The number of the Logstores that meet the query conditions.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.logstores is not None:
            result['logstores'] = self.logstores

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('logstores') is not None:
            self.logstores = m.get('logstores')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

