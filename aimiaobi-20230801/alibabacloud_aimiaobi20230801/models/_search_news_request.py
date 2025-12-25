# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchNewsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        filter_not_null: bool = None,
        include_content: bool = None,
        page: int = None,
        page_size: int = None,
        query: str = None,
        search_sources: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.filter_not_null = filter_not_null
        self.include_content = include_content
        self.page = page
        self.page_size = page_size
        self.query = query
        self.search_sources = search_sources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.filter_not_null is not None:
            result['FilterNotNull'] = self.filter_not_null

        if self.include_content is not None:
            result['IncludeContent'] = self.include_content

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query is not None:
            result['Query'] = self.query

        if self.search_sources is not None:
            result['SearchSources'] = self.search_sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('FilterNotNull') is not None:
            self.filter_not_null = m.get('FilterNotNull')

        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SearchSources') is not None:
            self.search_sources = m.get('SearchSources')

        return self

