# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendNotificationsShrinkRequest(DaraModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # Input parameter object for message push.
        # 
        # This parameter is required.
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        # Identity information.
        self.tenant_info_shrink = tenant_info_shrink
        # User Identifier information
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

        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink

        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink

        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')

        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')

        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')

        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')

        return self

