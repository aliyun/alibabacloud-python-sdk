# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApiKeyListQry(DaraModel):
    def __init__(
        self,
        client_id: int = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        status: int = None,
    ):
        self.client_id = client_id
        self.keyword = keyword
        self.page = page
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['clientId'] = self.client_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

