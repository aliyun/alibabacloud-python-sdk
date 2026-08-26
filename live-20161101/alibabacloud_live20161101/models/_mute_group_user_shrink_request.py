# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MuteGroupUserShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        broad_cast_type: int = None,
        group_id: str = None,
        mute_time: int = None,
        mute_user_list_shrink: str = None,
        operator_user_id: str = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The system message broadcast type. Valid values:
        # 
        # - 0: no broadcast.
        # 
        # - 1: broadcast to specified users.
        # 
        # - 2: broadcast to the group.
        self.broad_cast_type = broad_cast_type
        # The message group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The mute duration. Unit: seconds.
        # 
        # >If this parameter is not specified or is set to 0, the default mute duration (86400 seconds) is used.
        self.mute_time = mute_time
        # The mute details.
        # 
        # This parameter is required.
        self.mute_user_list_shrink = mute_user_list_shrink
        # The user ID of the operator.
        # > This parameter is required, and the user must be the creator of the group.
        self.operator_user_id = operator_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.broad_cast_type is not None:
            result['BroadCastType'] = self.broad_cast_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time

        if self.mute_user_list_shrink is not None:
            result['MuteUserList'] = self.mute_user_list_shrink

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BroadCastType') is not None:
            self.broad_cast_type = m.get('BroadCastType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')

        if m.get('MuteUserList') is not None:
            self.mute_user_list_shrink = m.get('MuteUserList')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        return self

