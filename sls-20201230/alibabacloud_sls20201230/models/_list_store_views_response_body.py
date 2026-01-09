# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListStoreViewsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        storeviews: List[str] = None,
        total: int = None,
    ):
        # The number of returned datasets.
        self.count = count
        # The dataset names.
        self.storeviews = storeviews
        # The total number of datasets in the project.
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

        if self.storeviews is not None:
            result['storeviews'] = self.storeviews

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('storeviews') is not None:
            self.storeviews = m.get('storeviews')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

