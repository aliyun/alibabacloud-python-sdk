# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMusicTypeShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Input parameters for the service request
        self.payload_shrink = payload_shrink
        # User identifier information
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

        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

