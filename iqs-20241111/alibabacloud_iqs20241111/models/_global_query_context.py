# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class GlobalQueryContext(DaraModel):
    def __init__(
        self,
        original_query: main_models.GlobalQueryContextOriginalQuery = None,
    ):
        self.original_query = original_query

    def validate(self):
        if self.original_query:
            self.original_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = main_models.GlobalQueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m.get('originalQuery'))

        return self

class GlobalQueryContextOriginalQuery(DaraModel):
    def __init__(
        self,
        page: str = None,
        query: str = None,
        time_range: str = None,
    ):
        self.page = page
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

