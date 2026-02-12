# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsConsumerResetOffsetRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        reset_timestamp: int = None,
        topic: str = None,
        type: int = None,
    ):
        # The ID of the consumer group whose dead-letter message you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The timestamp to which you want to reset the consumer offset. This parameter takes effect only when the **Type** parameter is set to **1**. Unit: milliseconds.
        self.reset_timestamp = reset_timestamp
        # The name of the topic for which you want to reset the consumer offset.
        # 
        # This parameter is required.
        self.topic = topic
        # The method that you want to use to clear accumulated messages. Valid values:
        # 
        # *   **0:** All accumulated messages are cleared. Messages that are not consumed are ignored. Consumers in the specified consumer group consume only messages that are published to the topic after the specified point in time.
        # 
        # If "reconsumeLater" is returned, the accumulated messages are not cleared because the system is retrying to resend the messages to consumers.
        # 
        # *   **1:** The messages that were published to the topic before the specified point in time are cleared. You must specify a point in time. Consumers in the specified consumer group consume only the messages that are published to the topic after the specified point in time.
        # 
        # You can specify a point in time from the earliest point in time when a message was published to the topic to the most recent point in time when a message was published to the topic. Points in time that are not within the allowed time range are invalid.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reset_timestamp is not None:
            result['ResetTimestamp'] = self.reset_timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResetTimestamp') is not None:
            self.reset_timestamp = m.get('ResetTimestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

