# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSslCertsRequest(DaraModel):
    def __init__(
        self,
        cert_name_like: str = None,
        domain_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Name matching keyword.
        self.cert_name_like = cert_name_like
        # Domain name.
        self.domain_name = domain_name
        # Page number, default is 1
        self.page_number = page_number
        # Page size, default is 10
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_name_like is not None:
            result['certNameLike'] = self.cert_name_like

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certNameLike') is not None:
            self.cert_name_like = m.get('certNameLike')

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

