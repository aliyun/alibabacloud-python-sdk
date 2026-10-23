# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAliDingGroupChatsRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        exclude_muted: bool = None,
        keyword: str = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # The cursor for the paged query. Set this parameter to 0 for the first request. For subsequent paging requests, set this parameter to the value of **nextCursor** returned in the previous response.
        self.cursor = cursor
        # Specifies whether to exclude muted group chats.
        self.exclude_muted = exclude_muted
        # The keyword for search. The keyword always matches the name field. If the description field is defined in the schema, the keyword also matches the description field.
        # 
        # This parameter is required.
        self.keyword = keyword
        # The page size.
        self.page_size = page_size
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.exclude_muted is not None:
            result['excludeMuted'] = self.exclude_muted

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('excludeMuted') is not None:
            self.exclude_muted = m.get('excludeMuted')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

