# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataAgentThemeRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        theme_from: str = None,
        theme_type: str = None,
    ):
        # The common scenarios. Valid values: report, infographic, and others.
        self.category = category
        # **[Not supported]** The page size. Maximum value: 100.
        self.max_results = max_results
        # **[Not supported]** The pagination token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query exists.
        # - If **NextToken** has a return value, the value indicates the token for the next query.
        self.next_token = next_token
        # The current page number.
        self.page_number = page_number
        # The current page size.
        self.page_size = page_size
        # The source of the theme. Valid values:
        # 
        # - system
        # - custom
        # - derived
        self.theme_from = theme_from
        # The theme stage. Valid values:
        # 
        # - design: contains only design.md.
        # - template: complete and renderable.
        self.theme_type = theme_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.theme_from is not None:
            result['ThemeFrom'] = self.theme_from

        if self.theme_type is not None:
            result['ThemeType'] = self.theme_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ThemeFrom') is not None:
            self.theme_from = m.get('ThemeFrom')

        if m.get('ThemeType') is not None:
            self.theme_type = m.get('ThemeType')

        return self

