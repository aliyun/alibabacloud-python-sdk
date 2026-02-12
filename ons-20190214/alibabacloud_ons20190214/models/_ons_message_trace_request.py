# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsMessageTraceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic to which the message belongs.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

