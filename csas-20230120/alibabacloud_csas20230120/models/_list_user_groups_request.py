# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListUserGroupsRequest(DaraModel):
    def __init__(
        self,
        attribute_value: str = None,
        current_page: int = None,
        name: str = None,
        papolicy_id: str = None,
        page_size: int = None,
        user_group_ids: List[str] = None,
    ):
        # The value of a user group property. The value must be 1 to 128 characters in length.
        self.attribute_value = attribute_value
        # The page number of the current page in a paged query. Valid values: 1 to 10000.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the user group. The name must be 1 to 128 characters in length. It can contain letters, digits, periods (.), underscores (_), and hyphens (-). It supports both uppercase and lowercase letters and Chinese characters.
        self.name = name
        # The ID of an internal network access policy. You can get this value from:
        # 
        # - [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): List internal network access policies.
        # 
        # - [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): Create an internal network access policy.
        self.papolicy_id = papolicy_id
        # The number of entries per page in a paged query. Valid values: 1 to 1000.
        # 
        # This parameter is required.
        self.page_size = page_size
        # A collection of user group IDs. You can specify up to 100 IDs.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.name is not None:
            result['Name'] = self.name

        if self.papolicy_id is not None:
            result['PAPolicyId'] = self.papolicy_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PAPolicyId') is not None:
            self.papolicy_id = m.get('PAPolicyId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

