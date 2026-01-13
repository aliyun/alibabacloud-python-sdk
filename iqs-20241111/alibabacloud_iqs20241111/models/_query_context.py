# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iqs20241111 import models as main_models
from darabonba.model import DaraModel

class QueryContext(DaraModel):
    def __init__(
        self,
        original_query: main_models.QueryContextOriginalQuery = None,
        rewrite: main_models.QueryContextRewrite = None,
    ):
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()

        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = main_models.QueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m.get('originalQuery'))

        if m.get('rewrite') is not None:
            temp_model = main_models.QueryContextRewrite()
            self.rewrite = temp_model.from_map(m.get('rewrite'))

        return self

class QueryContextRewrite(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        time_range: str = None,
    ):
        self.enabled = enabled
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

class QueryContextOriginalQuery(DaraModel):
    def __init__(
        self,
        industry: str = None,
        page: str = None,
        query: str = None,
        time_range: str = None,
    ):
        self.industry = industry
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
        if self.industry is not None:
            result['industry'] = self.industry

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

