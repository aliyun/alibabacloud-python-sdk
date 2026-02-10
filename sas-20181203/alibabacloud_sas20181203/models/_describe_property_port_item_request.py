# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyPortItemRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        force_flush: bool = None,
        page_size: int = None,
        port: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # Specifies whether to forcefully refresh the data that you want to query.
        self.force_flush = force_flush
        # The number of entries to return on each page.
        self.page_size = page_size
        # The port number.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.force_flush is not None:
            result['ForceFlush'] = self.force_flush

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

