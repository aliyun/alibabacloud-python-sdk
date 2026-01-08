# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTlsInspectCACertificatesRequest(DaraModel):
    def __init__(
        self,
        ca_cert_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.ca_cert_id = ca_cert_id
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_id is not None:
            result['CaCertId'] = self.ca_cert_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaCertId') is not None:
            self.ca_cert_id = m.get('CaCertId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

