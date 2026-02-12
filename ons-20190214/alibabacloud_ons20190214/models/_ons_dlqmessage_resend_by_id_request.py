# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsDLQMessageResendByIdRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
    ):
        # The ID of the consumer group in which you want to query dead-letter messages.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance in which the dead-letter message you want to query resides.
        self.instance_id = instance_id
        # The ID of the dead-letter message that you want to send to a consumer group for consumption.
        # 
        # This parameter is required.
        self.msg_id = msg_id

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

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        return self

