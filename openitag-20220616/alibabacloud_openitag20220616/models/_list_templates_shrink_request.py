# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        types_shrink: str = None,
    ):
        # Page number
        self.page_number = page_number
        # Page size
        self.page_size = page_size
        # Search content
        self.search_key = search_key
        # List of application types.
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.types_shrink is not None:
            result['Types'] = self.types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')

        return self

