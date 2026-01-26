# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataResponse(DaraModel):
    def __init__(
        self,
        results: str = None,
    ):
        self.results = results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.results is not None:
            result['results'] = self.results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('results') is not None:
            self.results = m.get('results')

        return self

