# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmNotificationRequest(DaraModel):
    def __init__(
        self,
        notification_request_id: str = None,
    ):
        # This parameter is required.
        self.notification_request_id = notification_request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.notification_request_id is not None:
            result['NotificationRequestId'] = self.notification_request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationRequestId') is not None:
            self.notification_request_id = m.get('NotificationRequestId')

        return self

