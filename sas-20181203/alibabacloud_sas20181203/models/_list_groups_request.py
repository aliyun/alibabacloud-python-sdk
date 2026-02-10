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
        # The page number. Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The pagination token that is used in the next request to retrieve a new page of results. If the return value of NextToken is empty, no next query is to be sent. If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The number of entries per page. Default value: 20. Maximum value: 2000.
        self.page_size = page_size
        # Specifies whether to use NextToken to query vulnerabilities. If you set this parameter to true, TotalCount is not returned. Valid values:
        # 
        # *   **true**
        # *   **false**
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

