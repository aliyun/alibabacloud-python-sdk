# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRecommendContentShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Device identification information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Request Parameters
        # 
        # This parameter is required.
        self.request_shrink = request_shrink
        # User identification information
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

        if self.request_shrink is not None:
            result['Request'] = self.request_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

