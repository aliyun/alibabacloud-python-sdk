# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCasCertificatesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_keyword: str = None,
        security_token: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.search_keyword = search_keyword
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_keyword is not None:
            result['SearchKeyword'] = self.search_keyword

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchKeyword') is not None:
            self.search_keyword = m.get('SearchKeyword')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

