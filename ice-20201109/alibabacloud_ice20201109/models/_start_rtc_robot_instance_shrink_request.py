# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartRtcRobotInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        channel_id: str = None,
        config_shrink: str = None,
        robot_id: str = None,
        user_data: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.auth_token = auth_token
        # This parameter is required.
        self.channel_id = channel_id
        self.config_shrink = config_shrink
        # This parameter is required.
        self.robot_id = robot_id
        self.user_data = user_data
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.config_shrink is not None:
            result['Config'] = self.config_shrink

        if self.robot_id is not None:
            result['RobotId'] = self.robot_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')

        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

