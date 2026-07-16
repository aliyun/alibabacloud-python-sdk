# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBrowsersInput(DaraModel):
    def __init__(
        self,
        browser_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Filters the results by browser name.
        self.browser_name = browser_name
        # The page number of the results to return.
        self.page_number = page_number
        # The maximum number of results to return per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

