# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatSessionListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # Pagination parameter, page number, default is 1.
        self.current_page = current_page
        # Session name.
        self.name = name
        # Page size, default is 10.
        self.page_size = page_size
        # The unique identifier of the user. If not provided, the SDK calling account will be used as the user ID by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.name is not None:
            result['name'] = self.name

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

