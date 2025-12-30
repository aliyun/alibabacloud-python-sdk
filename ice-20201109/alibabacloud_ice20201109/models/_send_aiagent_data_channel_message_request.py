# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendAIAgentDataChannelMessageRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        message: str = None,
    ):
        # The ID of the AI agent in the conversation.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The DataChannel message you want to send. You must specify a JSON string. The value can be up to 8,192 characters in length.
        # 
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

