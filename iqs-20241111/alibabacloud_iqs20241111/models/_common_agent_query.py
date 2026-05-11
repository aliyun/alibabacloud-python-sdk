# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CommonAgentQuery(DaraModel):
    def __init__(
        self,
        limit: int = None,
        query: str = None,
        query_scene_enum_code: str = None,
        search_model: str = None,
    ):
        self.limit = limit
        self.query = query
        self.query_scene_enum_code = query_scene_enum_code
        self.search_model = search_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.query is not None:
            result['query'] = self.query

        if self.query_scene_enum_code is not None:
            result['querySceneEnumCode'] = self.query_scene_enum_code

        if self.search_model is not None:
            result['searchModel'] = self.search_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('querySceneEnumCode') is not None:
            self.query_scene_enum_code = m.get('querySceneEnumCode')

        if m.get('searchModel') is not None:
            self.search_model = m.get('searchModel')

        return self

