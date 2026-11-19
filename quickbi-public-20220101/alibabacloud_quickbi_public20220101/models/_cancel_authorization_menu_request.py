# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelAuthorizationMenuRequest(DaraModel):
    def __init__(
        self,
        data_portal_id: str = None,
        menu_ids: str = None,
        user_group_ids: str = None,
        user_ids: str = None,
    ):
        # The ID of the data portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The IDs of the leaf node menus in the data portal.
        # 
        # - You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of 100 IDs can be specified at a time.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # The IDs of the user groups.
        # 
        # - You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of 200 IDs can be specified at a time.
        # - UserGroupIds and UserIds cannot be empty at the same time.
        self.user_group_ids = user_group_ids
        # The IDs of the users. These are Quick BI user IDs, not Alibaba Cloud UIDs.
        # 
        # - You can specify multiple IDs. Separate multiple IDs with commas (,). A maximum of 200 IDs can be specified at a time.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_portal_id is not None:
            result['DataPortalId'] = self.data_portal_id

        if self.menu_ids is not None:
            result['MenuIds'] = self.menu_ids

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')

        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

