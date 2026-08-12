# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDomainMetasRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        default_template: bool = None,
        list_type: str = None,
        name: str = None,
        page_size: int = None,
    ):
        # The current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Specifies whether to include system default template lists.
        self.default_template = default_template
        # The list type (blacklist/whitelist).
        # 
        # This parameter is required.
        self.list_type = list_type
        # The list name. Fuzzy match is supported.
        self.name = name
        # The number of entries per page in a paged query. Settings: 1 to 1000. Paging is used to return results.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.default_template is not None:
            result['DefaultTemplate'] = self.default_template

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DefaultTemplate') is not None:
            self.default_template = m.get('DefaultTemplate')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

