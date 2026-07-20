# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCompaniesRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        current_page: int = None,
        keyword: str = None,
        show_size: int = None,
    ):
        # The company ID.
        self.company_id = company_id
        # The page number of the current page. Default value: 1.
        self.current_page = current_page
        # The search keyword. For example, a keyword for the company name, province, country code, or city.
        self.keyword = keyword
        # The number of contacts to display per page in a paged query.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

