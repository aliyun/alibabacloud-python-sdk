# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        next_token: str = None,
        page_size: int = None,
        use_next_token: bool = None,
    ):
        # The page number of the current page to return. Minimum value: 1. Default value: 1.
        self.current_page = current_page
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The token for the next query. If NextToken is empty, no additional results exist. If NextToken has a value, the value indicates the token to use for the next query.
        self.next_token = next_token
        # The maximum number of entries to return on each page in a paging query. Default value: 20. Maximum value: 2000.
        self.page_size = page_size
        # Specifies whether to use the NextToken method to retrieve the vulnerability list data. If this parameter is used, TotalCount is no longer returned. Valid values:
        # 
        # - **true**: Uses the NextToken method.
        # - **false**: Does not use the NextToken method.
        self.use_next_token = use_next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.use_next_token is not None:
            result['UseNextToken'] = self.use_next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UseNextToken') is not None:
            self.use_next_token = m.get('UseNextToken')

        return self

