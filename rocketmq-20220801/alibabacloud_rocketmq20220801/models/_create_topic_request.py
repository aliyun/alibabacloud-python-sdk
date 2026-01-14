# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTopicRequest(DaraModel):
    def __init__(
        self,
        lite_topic_expiration: int = None,
        max_send_tps: int = None,
        message_type: str = None,
        remark: str = None,
    ):
        self.lite_topic_expiration = lite_topic_expiration
        # The maximum TPS for message sending.
        self.max_send_tps = max_send_tps
        # The type of messages in the topic that you want to create.
        # 
        # Valid values:
        # 
        # *   TRANSACTION: transactional messages
        # *   FIFO: ordered messages
        # *   DELAY: scheduled or delayed messages
        # *   NORMAL: normal messages
        # 
        # >  The type of messages in the topic must be the same as the type of messages that you want to send. For example, if you create a topic whose message type is ordered messages, you can use the topic to send and receive only ordered messages.
        # 
        # This parameter is required.
        self.message_type = message_type
        # The description of the topic that you want to create.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lite_topic_expiration is not None:
            result['liteTopicExpiration'] = self.lite_topic_expiration

        if self.max_send_tps is not None:
            result['maxSendTps'] = self.max_send_tps

        if self.message_type is not None:
            result['messageType'] = self.message_type

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('liteTopicExpiration') is not None:
            self.lite_topic_expiration = m.get('liteTopicExpiration')

        if m.get('maxSendTps') is not None:
            self.max_send_tps = m.get('maxSendTps')

        if m.get('messageType') is not None:
            self.message_type = m.get('messageType')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

