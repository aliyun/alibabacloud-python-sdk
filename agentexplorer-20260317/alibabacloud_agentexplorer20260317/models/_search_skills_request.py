# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchSkillsRequest(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        search_mode: str = None,
        skip: int = None,
    ):
        # The skill category code. Separate multiple codes with commas. For a second-level category, use the format: first-level category.second-level category.
        self.category_code = category_code
        # The search keyword.
        self.keyword = keyword
        # The maximum number of entries per page for a paged query. Maximum value: 100. Default value: 20.
        self.max_results = max_results
        # The token for the next query. Set this to the NextToken value returned by the previous API call.
        self.next_token = next_token
        self.search_mode = search_mode
        # The number of entries to skip for pagination.
        self.skip = skip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['categoryCode'] = self.category_code

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.search_mode is not None:
            result['searchMode'] = self.search_mode

        if self.skip is not None:
            result['skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('categoryCode') is not None:
            self.category_code = m.get('categoryCode')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('searchMode') is not None:
            self.search_mode = m.get('searchMode')

        if m.get('skip') is not None:
            self.skip = m.get('skip')

        return self

