# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListMaterializedViewResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        materialized_views: List[str] = None,
        total: int = None,
    ):
        self.count = count
        self.materialized_views = materialized_views
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

        if self.materialized_views is not None:
            result['materializedViews'] = self.materialized_views

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('materializedViews') is not None:
            self.materialized_views = m.get('materializedViews')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

