# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGroupMemberRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # The ID of the destination group to which the member is added.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The member ID. If member_type is set to user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The type of the member. Set the value to user. When you create a group, you can directly add the group to a parent group.
        # 
        # * user
        # 
        # Note: A group can be added to only one group. A user can be added to multiple groups.
        # 
        # This parameter is required.
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.member_id is not None:
            result['member_id'] = self.member_id

        if self.member_type is not None:
            result['member_type'] = self.member_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('member_id') is not None:
            self.member_id = m.get('member_id')

        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')

        return self

