# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceIpWhitelistRequest(DaraModel):
    def __init__(
        self,
        ip_whitelist: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # IP whitelist.
        self.ip_whitelist = ip_whitelist
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_whitelist is not None:
            result['ipWhitelist'] = self.ip_whitelist

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipWhitelist') is not None:
            self.ip_whitelist = m.get('ipWhitelist')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

