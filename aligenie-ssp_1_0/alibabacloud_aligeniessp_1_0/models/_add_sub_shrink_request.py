# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddSubShrinkRequest(DaraModel):
    def __init__(
        self,
        add_subscription_info_request_shrink: str = None,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Subscribe to album request
        self.add_subscription_info_request_shrink = add_subscription_info_request_shrink
        # Device Information
        self.device_info_shrink = device_info_shrink
        # User Information
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_subscription_info_request_shrink is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request_shrink

        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            self.add_subscription_info_request_shrink = m.get('AddSubscriptionInfoRequest')

        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

