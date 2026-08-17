# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDomainItemsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        item_value: str = None,
        list_id: str = None,
        list_type: str = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        self.item_value = item_value
        # This parameter is required.
        self.list_id = list_id
        # This parameter is required.
        self.list_type = list_type
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

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        if self.list_id is not None:
            result['ListId'] = self.list_id

        if self.list_type is not None:
            result['ListType'] = self.list_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        if m.get('ListId') is not None:
            self.list_id = m.get('ListId')

        if m.get('ListType') is not None:
            self.list_type = m.get('ListType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

