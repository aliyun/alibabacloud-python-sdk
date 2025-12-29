# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInterventionDictionaryNerResultsRequest(DaraModel):
    def __init__(
        self,
        query: str = None,
    ):
        # Query keywords.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')

        return self

