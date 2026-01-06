# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListContactRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        show_size: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The keyword used in the query. For example, you can specify a keyword in names, email addresses, and mobile phone numbers.
        self.keyword = keyword
        # The number of contacts per page.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

