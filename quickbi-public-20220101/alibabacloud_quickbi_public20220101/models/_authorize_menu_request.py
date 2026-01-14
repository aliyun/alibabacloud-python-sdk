# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeMenuRequest(DaraModel):
    def __init__(
        self,
        auth_points_value: int = None,
        data_portal_id: str = None,
        menu_ids: str = None,
        user_group_ids: str = None,
        user_ids: str = None,
    ):
        # Authorizes the permissions of the menu. Valid values:
        # 
        # *   1: view
        # *   3: View + Export (default)
        self.auth_points_value = auth_points_value
        # The ID of the BI portal.
        # 
        # This parameter is required.
        self.data_portal_id = data_portal_id
        # The menu ID of the BI portal leaf node.
        # 
        # *   The directory menu cannot be authorized.
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 100.
        # 
        # This parameter is required.
        self.menu_ids = menu_ids
        # The IDs of the user groups.
        # 
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 200.
        # *   UserGroupIds and UserIds cannot be empty at the same time
        self.user_group_ids = user_group_ids
        # The IDs of the end users. The UserID of the Quick BI is used instead of the UID of Alibaba Cloud.
        # 
        # *   You can upload multiple parameters at a time. Separate multiple IDs with commas (,). The maximum number of parameters that can be modified at a time is 200.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_points_value is not None:
            result['AuthPointsValue'] = self.auth_points_value

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
        if m.get('AuthPointsValue') is not None:
            self.auth_points_value = m.get('AuthPointsValue')

        if m.get('DataPortalId') is not None:
            self.data_portal_id = m.get('DataPortalId')

        if m.get('MenuIds') is not None:
            self.menu_ids = m.get('MenuIds')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

