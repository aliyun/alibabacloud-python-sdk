# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SearchContextRequest(DaraModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
        formatted: bool = None,
        limit: int = None,
        query: str = None,
        retrieval_option: str = None,
        threshold: float = None,
    ):
        self.filter = filter
        self.formatted = formatted
        self.limit = limit
        # This parameter is required.
        self.query = query
        self.retrieval_option = retrieval_option
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.formatted is not None:
            result['formatted'] = self.formatted

        if self.limit is not None:
            result['limit'] = self.limit

        if self.query is not None:
            result['query'] = self.query

        if self.retrieval_option is not None:
            result['retrievalOption'] = self.retrieval_option

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('formatted') is not None:
            self.formatted = m.get('formatted')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('retrievalOption') is not None:
            self.retrieval_option = m.get('retrievalOption')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

