# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsMessagePushRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        group_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the consumer client. You can call the [OnsConsumerGetConnection](https://help.aliyun.com/document_detail/29598.html) operation to query client IDs.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the consumer group. For information about what a consumer group is, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the ApsaraMQ for RocketMQ instance to which the specified consumer group belongs.
        self.instance_id = instance_id
        # The ID of the message.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic to which the message is pushed.
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
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

