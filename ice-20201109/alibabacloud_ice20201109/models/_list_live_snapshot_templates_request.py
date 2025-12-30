# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLiveSnapshotTemplatesRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        search_key_word: str = None,
        sort_by: str = None,
        template_ids: List[str] = None,
        type: str = None,
    ):
        # The page number. Valid values: [1,n). Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The search keyword. You can use the template ID or name as the keyword to search for templates. If you search for templates by name, fuzzy match is supported.
        # 
        # *   It cannot exceed 128 characters in length.
        self.search_key_word = search_key_word
        # The sorting order. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   asc: sorts the query results by creation time in ascending order.
        # *   desc: sorts the query results by creation time in descending order.
        self.sort_by = sort_by
        # The template IDs.
        # 
        # *   If you specify the SearchKeyWord parameter, this condition does not take effect.
        # *   The maximum length of the array is 200.
        self.template_ids = template_ids
        # The type of the template. By default, all types are queried.
        # 
        # Valid values:
        # 
        # *   system
        # *   custom
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

