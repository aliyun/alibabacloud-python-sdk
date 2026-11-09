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
        # The ID of the cloud browser group. You must specify either this parameter or BrowserInstanceGroupSetId, but not both.
        self.browser_instance_group_id = browser_instance_group_id
        # The ID of the browser delivery group set. You must specify either this parameter or BrowserInstanceGroupId, but not both.
        self.browser_instance_group_set_id = browser_instance_group_set_id
        # The keyword used for substring matching in bookmark names or URLs. The matching is case-insensitive for English characters. The keyword can be up to 1,024 characters in length after leading and trailing spaces are removed. If this parameter is not specified or contains only spaces, no filtering is applied. Special characters are matched literally.
        self.keyword = keyword
        # The page number of the page to return. Pages start from page 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values: 1 to 200.
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

