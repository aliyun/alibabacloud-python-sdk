# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatConversationRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        content: str = None,
        conversation_id: str = None,
        instance_id: str = None,
    ):
        # The additional information input in JSON format.
        self.config = config
        # The message content.
        # 
        # This parameter is required.
        self.content = content
        # The session ID. If this parameter is not specified, a new session is created. If this parameter is specified, the conversation continues in the context of the existing session.
        self.conversation_id = conversation_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

