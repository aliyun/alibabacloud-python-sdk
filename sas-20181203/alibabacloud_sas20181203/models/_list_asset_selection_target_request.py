# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAssetSelectionTargetRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        selection_key: str = None,
    ):
        # The number of the page to return. Pages start from page 1. Default value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The globally unique identifier (GUID) of the asset.
        # 
        # This parameter is required.
        self.selection_key = selection_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        return self

