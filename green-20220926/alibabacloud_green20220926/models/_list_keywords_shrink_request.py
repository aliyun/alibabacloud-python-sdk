# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKeywordsShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lib_id: str = None,
        page_size: int = None,
        region_id: str = None,
        sort_shrink: str = None,
        word: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Library ID.
        self.lib_id = lib_id
        # Page size.
        self.page_size = page_size
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort_shrink = sort_shrink
        # Keyword.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink

        if self.word is not None:
            result['Word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')

        if m.get('Word') is not None:
            self.word = m.get('Word')

        return self

