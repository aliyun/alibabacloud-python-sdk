# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelMuteGroupUserShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        broad_cast_type: int = None,
        cancel_mute_user_list_shrink: str = None,
        group_id: str = None,
        operator_user_id: str = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The mode in which system messages are broadcasted. Valid values:
        # 
        # *   0: specifies that system messages are not broadcasted. This is the default value.
        # *   1: specifies that system messages are broadcasted to specified users.
        # *   2: specifies that system messages are broadcasted to the message group.
        self.broad_cast_type = broad_cast_type
        # The IDs of the users.
        # 
        # This parameter is required.
        self.cancel_mute_user_list_shrink = cancel_mute_user_list_shrink
        # The ID of the message group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the user who performs the operation.
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

        if self.cancel_mute_user_list_shrink is not None:
            result['CancelMuteUserList'] = self.cancel_mute_user_list_shrink

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.operator_user_id is not None:
            result['OperatorUserId'] = self.operator_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BroadCastType') is not None:
            self.broad_cast_type = m.get('BroadCastType')

        if m.get('CancelMuteUserList') is not None:
            self.cancel_mute_user_list_shrink = m.get('CancelMuteUserList')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('OperatorUserId') is not None:
            self.operator_user_id = m.get('OperatorUserId')

        return self

