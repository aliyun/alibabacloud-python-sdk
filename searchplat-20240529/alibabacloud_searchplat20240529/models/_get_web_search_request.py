# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetWebSearchRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        history: List[main_models.GetWebSearchRequestHistory] = None,
        query: str = None,
        query_rewrite: bool = None,
        top_k: int = None,
        way: str = None,
    ):
        self.content_type = content_type
        self.history = history
        # This parameter is required.
        self.query = query
        self.query_rewrite = query_rewrite
        self.top_k = top_k
        self.way = way

    def validate(self):
        if self.history:
            for v1 in self.history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['content_type'] = self.content_type

        result['history'] = []
        if self.history is not None:
            for k1 in self.history:
                result['history'].append(k1.to_map() if k1 else None)

        if self.query is not None:
            result['query'] = self.query

        if self.query_rewrite is not None:
            result['query_rewrite'] = self.query_rewrite

        if self.top_k is not None:
            result['top_k'] = self.top_k

        if self.way is not None:
            result['way'] = self.way

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        self.history = []
        if m.get('history') is not None:
            for k1 in m.get('history'):
                temp_model = main_models.GetWebSearchRequestHistory()
                self.history.append(temp_model.from_map(k1))

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('query_rewrite') is not None:
            self.query_rewrite = m.get('query_rewrite')

        if m.get('top_k') is not None:
            self.top_k = m.get('top_k')

        if m.get('way') is not None:
            self.way = m.get('way')

        return self

class GetWebSearchRequestHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

