# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserGroupMemberRequest(DaraModel):
    def __init__(
        self,
        user_group_id: str = None,
        user_id_list: str = None,
    ):
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The ID of the Quick BI user. Separate multiple IDs with commas (,). Example: abc,efg. You can enter a maximum of 1000 entries.
        # 
        # This parameter is required.
        self.user_id_list = user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')

        return self

