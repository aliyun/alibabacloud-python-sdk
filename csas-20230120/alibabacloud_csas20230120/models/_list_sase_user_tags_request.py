# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSaseUserTagsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        tag_ids: List[str] = None,
    ):
        # The page number of the current page in a paging query. Valid values: 1 to 10000.
        self.current_page = current_page
        # The name of the user label. The name must be 1 to 128 characters in length.
        self.name = name
        # The number of entries per page. Settings: 1 to 1000.
        self.page_size = page_size
        # The collection of user label IDs.
        self.tag_ids = tag_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        return self

