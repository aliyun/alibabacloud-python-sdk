# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserPrivateAccessPoliciesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        name: str = None,
        page_size: int = None,
        sase_user_id: str = None,
    ):
        # Current page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Intranet access policy name. Length should be between 1 to 128 characters, supporting Chinese and case-sensitive English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # Number of items per page for pagination. Range: 1~100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # User ID.
        # 
        # This parameter is required.
        self.sase_user_id = sase_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        return self

