# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOrganizationRoleUsersRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        role_id: int = None,
    ):
        # Keyword for the nickname of the organization member.
        self.keyword = keyword
        # Page number.
        # 
        # - Default value is 1.
        self.page_num = page_num
        # Number of items per page.
        # - Default value is 10.
        self.page_size = page_size
        # Organization role ID, including predefined roles and custom roles:
        # 
        # - Organization Administrator (predefined role): 111111111
        # - Permission Administrator (predefined role): 111111112
        # - Regular User (predefined role): 111111113
        # - Custom Role: The corresponding role ID for a custom role
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

