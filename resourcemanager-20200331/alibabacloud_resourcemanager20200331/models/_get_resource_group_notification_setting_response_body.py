# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceGroupNotificationSettingResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_notification_enable_status: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the group event notification is enabled.
        self.resource_group_notification_enable_status = resource_group_notification_enable_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_notification_enable_status is not None:
            result['ResourceGroupNotificationEnableStatus'] = self.resource_group_notification_enable_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupNotificationEnableStatus') is not None:
            self.resource_group_notification_enable_status = m.get('ResourceGroupNotificationEnableStatus')

        return self

