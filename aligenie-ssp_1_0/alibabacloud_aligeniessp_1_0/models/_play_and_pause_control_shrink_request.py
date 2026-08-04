# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PlayAndPauseControlShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_play_and_pause_control_param_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Business parameters
        # 
        # This parameter is required.
        self.open_play_and_pause_control_param_shrink = open_play_and_pause_control_param_shrink
        # User identity information
        # 
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.open_play_and_pause_control_param_shrink is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('OpenPlayAndPauseControlParam') is not None:
            self.open_play_and_pause_control_param_shrink = m.get('OpenPlayAndPauseControlParam')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

