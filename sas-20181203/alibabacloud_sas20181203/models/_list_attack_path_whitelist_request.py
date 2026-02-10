# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAttackPathWhitelistRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        path_name_desc: str = None,
        path_type: str = None,
        whitelist_name: str = None,
    ):
        # When performing a paginated query, set the current page number. The default value is **1**.
        self.current_page = current_page
        # The language type for requests and responses. The default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # When performing a paginated query, set the maximum number of items per page. The default value is 20.
        self.page_size = page_size
        # Path name description.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path name descriptions.
        self.path_name_desc = path_name_desc
        # Path type.
        # > You can call [ListAvailableAttackPath](~~ListAvailableAttackPath~~) to query the path types.
        self.path_type = path_type
        # Whitelist name.
        self.whitelist_name = whitelist_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path_name_desc is not None:
            result['PathNameDesc'] = self.path_name_desc

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.whitelist_name is not None:
            result['WhitelistName'] = self.whitelist_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PathNameDesc') is not None:
            self.path_name_desc = m.get('PathNameDesc')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('WhitelistName') is not None:
            self.whitelist_name = m.get('WhitelistName')

        return self

