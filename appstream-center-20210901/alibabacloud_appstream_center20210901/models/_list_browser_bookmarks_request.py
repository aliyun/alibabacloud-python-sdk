# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBrowserBookmarksRequest(DaraModel):
    def __init__(
        self,
        browser_instance_group_id: str = None,
        browser_instance_group_set_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.browser_instance_group_id = browser_instance_group_id
        self.browser_instance_group_set_id = browser_instance_group_set_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_instance_group_id is not None:
            result['BrowserInstanceGroupId'] = self.browser_instance_group_id

        if self.browser_instance_group_set_id is not None:
            result['BrowserInstanceGroupSetId'] = self.browser_instance_group_set_id

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrowserInstanceGroupId') is not None:
            self.browser_instance_group_id = m.get('BrowserInstanceGroupId')

        if m.get('BrowserInstanceGroupSetId') is not None:
            self.browser_instance_group_set_id = m.get('BrowserInstanceGroupSetId')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

