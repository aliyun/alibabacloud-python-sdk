# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUuidsByWebPathRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        type: str = None,
        web_path: str = None,
    ):
        # The number of the page to return.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The path type of the web directory. Valid values:
        # 
        # *   **def**: automatically identified
        # *   **customize**: manually added
        self.type = type
        # The path to the web directory.
        self.web_path = web_path

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

        if self.type is not None:
            result['Type'] = self.type

        if self.web_path is not None:
            result['WebPath'] = self.web_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WebPath') is not None:
            self.web_path = m.get('WebPath')

        return self

