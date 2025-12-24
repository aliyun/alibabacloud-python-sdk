# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveUserFromDesktopOversoldUserGroupRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        oversold_group_id: str = None,
        user_desktop_id: str = None,
        user_group_id: str = None,
    ):
        self.end_user_id = end_user_id
        self.oversold_group_id = oversold_group_id
        self.user_desktop_id = user_desktop_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

