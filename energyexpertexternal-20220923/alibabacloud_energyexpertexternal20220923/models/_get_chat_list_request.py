# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        session_id: str = None,
    ):
        # Pagination parameter, page number, starting from 1.
        self.current_page = current_page
        # Page size.
        self.page_size = page_size
        # Q&A session ID, used to record multiple Q&As for the same user.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

