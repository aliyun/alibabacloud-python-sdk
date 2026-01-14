# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIndicesRequest(DaraModel):
    def __init__(
        self,
        index_name: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The name of the knowledge base. You can query knowledge base by name. The name must be 1 to 20 characters in length and can contain characters classified as letter in Unicode, including English letters, Chinese characters, digits, among others. The name can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is left empty by default, which means that all knowledge bases in the specified workspace are queried.
        self.index_name = index_name
        # The number of the pages to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of knowledge bases to display on each page. No maximum value. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

