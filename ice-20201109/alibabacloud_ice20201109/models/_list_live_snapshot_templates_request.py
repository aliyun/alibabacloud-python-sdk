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
        # The page number. The value must be greater than or equal to 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The search keyword. You can perform a fuzzy search by template ID or template name.
        # 
        # - Maximum length: 128 characters.
        self.search_key_word = search_key_word
        # The sorting method. By default, results are sorted by creation time in descending order.
        self.sort_by = sort_by
        # The template IDs.
        # 
        # - This parameter does not take effect if `SearchKeyWord` is specified.
        # 
        # - You can specify a maximum of 200 template IDs.
        self.template_ids = template_ids
        # The type of the template. By default, templates of all types are queried.
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

