# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdpConfigsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        include: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.include = include
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

        if self.include is not None:
            result['Include'] = self.include

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

