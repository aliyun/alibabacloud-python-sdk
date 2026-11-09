# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBrowserRestrictedURLsRequest(DaraModel):
    def __init__(
        self,
        browser_instance_group_id: str = None,
        browser_instance_group_set_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the browser delivery group. You must specify either this parameter or BrowserInstanceGroupSetId, but not both. If you specify this parameter, the restricted URLs configured for the delivery group are queried.
        self.browser_instance_group_id = browser_instance_group_id
        # The ID of the browser delivery group set. You must specify either this parameter or BrowserInstanceGroupId, but not both.
        self.browser_instance_group_set_id = browser_instance_group_set_id
        # The keyword used to filter access control URLs by using a contains match. The match is case-insensitive for English characters. The keyword can be up to 1,024 characters in length after leading and trailing spaces are removed. If you do not specify this parameter or specify only spaces, no filtering is performed. Special characters are matched literally.
        self.keyword = keyword
        # The page number during paging. Default value: 0. If the value is less than 1, such as 0, the first page is returned. If the value is less than 0, a parameter error is returned. Set this parameter to 1 or greater.
        self.page_number = page_number
        # The number of records to return on each page during paging. Valid values: 1 to 200. Default value: 200. If the value is less than or equal to 0 or greater than 200, a parameter error is returned.
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

