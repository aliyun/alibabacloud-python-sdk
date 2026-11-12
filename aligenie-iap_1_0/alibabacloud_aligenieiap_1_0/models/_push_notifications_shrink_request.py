# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PushNotificationsShrinkRequest(DaraModel):
    def __init__(
        self,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
    ):
        # Input parameter object for message push.
        # 
        # This parameter is required.
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        # Identity information.
        self.tenant_info_shrink = tenant_info_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink

        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')

        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')

        return self

