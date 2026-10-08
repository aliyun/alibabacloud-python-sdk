# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySlsLogStoreListRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        current_page: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of the page to return. Pages start from Page 1.
        self.current_page = current_page
        # The number of entries to return on each page.
        self.page_size = page_size
        # The type of data that is collected by Log Service. Valid values:
        # 
        # - file: the file type
        # 
        # - stdout: the standard output type
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

