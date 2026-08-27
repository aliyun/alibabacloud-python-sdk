# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class ListChatSessionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        message: str = None,
        page: int = None,
        page_size: str = None,
        request_id: str = None,
        sessions: List[Any] = None,
        tenant_id: str = None,
        total: int = None,
    ):
        # The error code.
        self.code = code
        # Indicates whether there is a next page.
        self.has_more = has_more
        # The status code description.
        self.message = message
        # The current page number.
        self.page = page
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of sessions.
        self.sessions = sessions
        # The effective tenant ID.
        self.tenant_id = tenant_id
        # The total number of records.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sessions is not None:
            result['sessions'] = self.sessions

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sessions') is not None:
            self.sessions = m.get('sessions')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

