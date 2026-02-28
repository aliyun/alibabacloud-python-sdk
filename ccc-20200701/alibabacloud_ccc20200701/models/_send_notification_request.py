# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendNotificationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message_body: str = None,
        notification_target: str = None,
        notification_type: str = None,
        sharding_key: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_body = message_body
        # This parameter is required.
        self.notification_target = notification_target
        # This parameter is required.
        self.notification_type = notification_type
        # This parameter is required.
        self.sharding_key = sharding_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_body is not None:
            result['MessageBody'] = self.message_body

        if self.notification_target is not None:
            result['NotificationTarget'] = self.notification_target

        if self.notification_type is not None:
            result['NotificationType'] = self.notification_type

        if self.sharding_key is not None:
            result['ShardingKey'] = self.sharding_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageBody') is not None:
            self.message_body = m.get('MessageBody')

        if m.get('NotificationTarget') is not None:
            self.notification_target = m.get('NotificationTarget')

        if m.get('NotificationType') is not None:
            self.notification_type = m.get('NotificationType')

        if m.get('ShardingKey') is not None:
            self.sharding_key = m.get('ShardingKey')

        return self

