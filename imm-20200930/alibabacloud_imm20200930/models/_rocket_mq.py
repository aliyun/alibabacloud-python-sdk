# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RocketMQ(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        topic_name: str = None,
    ):
        # The ID of the ApsaraMQ for RocketMQ instance. If you want to use ApsaraMQ for RocketMQ for notifications, you must specify this parameter.
        self.instance_id = instance_id
        # The name of the topic in ApsaraMQ for RocketMQ. If you want to use ApsaraMQ for RocketMQ for notifications, you must specify this parameter.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

