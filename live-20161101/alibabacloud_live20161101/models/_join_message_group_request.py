# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JoinMessageGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        broad_cast_statistics: bool = None,
        broad_cast_type: int = None,
        group_id: str = None,
        user_id: str = None,
    ):
        # Interactive message application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to broadcast statistics messages. When enabled, statistics information of the message group will be broadcast after joining the message group, and the client can receive and process this message. Valid values:
        # 
        # - true: Broadcast statistics messages.
        # - false: Do not broadcast statistics messages.
        self.broad_cast_statistics = broad_cast_statistics
        # System message diffusion type. Valid values:
        # 
        # - 0 (default): No diffusion.
        # - 1: Diffusion to specified users.
        # - 2: Diffusion to the group.
        self.broad_cast_type = broad_cast_type
        # The ID of the message group to join. Make sure the GroupId you provide exists.
        # 
        # This parameter is required.
        self.group_id = group_id
        # User ID, which is customized by the user and must be unique under the AppId. It can contain lowercase letters, numbers, underscores (_), and periods (.). The maximum length is 32 characters. Different users must use different UserIds.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.broad_cast_statistics is not None:
            result['BroadCastStatistics'] = self.broad_cast_statistics

        if self.broad_cast_type is not None:
            result['BroadCastType'] = self.broad_cast_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BroadCastStatistics') is not None:
            self.broad_cast_statistics = m.get('BroadCastStatistics')

        if m.get('BroadCastType') is not None:
            self.broad_cast_type = m.get('BroadCastType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

