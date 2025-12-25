# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRoutineRelatedRecordsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key_word: str = None,
    ):
        # The name of the function.
        # 
        # This parameter is required.
        self.name = name
        # The page number of the returned page. Default value: 1
        self.page_number = page_number
        # The number of entries per page. Valid values: an integer from 1 to 20.
        self.page_size = page_size
        # The keyword used for fuzzy search.
        self.search_key_word = search_key_word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')

        return self

