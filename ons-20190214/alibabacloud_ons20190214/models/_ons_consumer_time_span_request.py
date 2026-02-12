# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsConsumerTimeSpanRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        topic: str = None,
    ):
        # The ID of the consumer group whose reset time range you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The topic to which the consumer group subscribes.
        # 
        # This parameter is required.
        self.topic = topic

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

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

