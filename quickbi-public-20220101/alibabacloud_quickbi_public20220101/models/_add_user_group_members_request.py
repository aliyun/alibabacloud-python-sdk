# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserGroupMembersRequest(DaraModel):
    def __init__(
        self,
        user_group_ids: str = None,
        user_id: str = None,
    ):
        # The IDs of the user groups. Separate the IDs with commas (,). Example: aGroupId,bGroupId,cGroupIds
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids
        # The user ID of the Quick BI.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

