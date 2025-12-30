# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLiveRecordTemplatesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
        template_ids: List[str] = None,
        type: str = None,
    ):
        # The search keyword. You can use the template ID or name as the keyword to search for templates. If you search for templates by name, fuzzy match is supported.
        self.keyword = keyword
        # The page number. Minimum value: 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The sorting order. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   asc: sorts the query results in ascending order.
        # *   desc: sorts the query results in descending order.
        self.sort_by = sort_by
        self.template_ids = template_ids
        # The type of the template.
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
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

