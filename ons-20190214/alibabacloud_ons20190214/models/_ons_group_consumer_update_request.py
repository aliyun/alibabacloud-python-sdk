# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsGroupConsumerUpdateRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        read_enable: bool = None,
    ):
        # The ID of the consumer group for which you want to configure read permissions.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group you want to configure belongs.
        self.instance_id = instance_id
        # Specifies whether to authorize the consumer group to read messages. Valid values:
        # 
        # *   **true**: The consumer group can read messages.
        # *   **false**: The consumer group cannot read messages.
        # 
        # Default value: **true**.
        # 
        # This parameter is required.
        self.read_enable = read_enable

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

        if self.read_enable is not None:
            result['ReadEnable'] = self.read_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ReadEnable') is not None:
            self.read_enable = m.get('ReadEnable')

        return self

