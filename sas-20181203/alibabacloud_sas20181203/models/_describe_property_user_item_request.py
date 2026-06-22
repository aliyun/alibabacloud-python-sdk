# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyUserItemRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        force_flush: bool = None,
        page_size: int = None,
        user: str = None,
    ):
        # The page number of the current page to display in a paged query.
        self.current_page = current_page
        # Specifies whether to forcefully refresh the data to be queried. Valid values:
        # - **true**: Forcefully refresh.
        # - **false**: Do not forcefully refresh.
        self.force_flush = force_flush
        # The maximum number of entries to display on each page in a paged query.
        self.page_size = page_size
        # The account information of Asset Fingerprints.
        self.user = user

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

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ForceFlush') is not None:
            self.force_flush = m.get('ForceFlush')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

