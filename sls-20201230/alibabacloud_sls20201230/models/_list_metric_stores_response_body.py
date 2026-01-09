# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMetricStoresResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        metricstores: List[str] = None,
        total: int = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The names of the Metricstores.
        self.metricstores = metricstores
        # The total number of queried Metricstores.
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

        if self.metricstores is not None:
            result['metricstores'] = self.metricstores

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('metricstores') is not None:
            self.metricstores = m.get('metricstores')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

