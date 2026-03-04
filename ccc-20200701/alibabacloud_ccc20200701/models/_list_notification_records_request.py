# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNotificationRecordsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        notification_keys: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.notification_keys = notification_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.notification_keys is not None:
            result['NotificationKeys'] = self.notification_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NotificationKeys') is not None:
            self.notification_keys = m.get('NotificationKeys')

        return self

