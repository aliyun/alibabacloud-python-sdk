# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageChatTextRequest(DaraModel):
    def __init__(
        self,
        aiagent_id: str = None,
        mode: str = None,
        need_archiving: bool = None,
        receiver_id: str = None,
        session_id: str = None,
        text: str = None,
        type: str = None,
    ):
        # The ID of the AI agent.
        # 
        # This parameter is required.
        self.aiagent_id = aiagent_id
        # The mode of message sending. Valid values:
        # - online
        # - offline
        # 
        # Default value: offline.
        self.mode = mode
        # Specifies whether to archive chat records. Default value: true.
        self.need_archiving = need_archiving
        # The ID of the user who receives the message. The ID can be up to 64 bytes in length and can contain letters and digits.
        # 
        # This parameter is required.
        self.receiver_id = receiver_id
        # The ID of the session.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The content of the message.
        # 
        # This parameter is required.
        self.text = text
        # The type of the message. Valid values:
        # 
        # - announcement: notification.
        # - custom: custom message.
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
        if self.aiagent_id is not None:
            result['AIAgentId'] = self.aiagent_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.need_archiving is not None:
            result['NeedArchiving'] = self.need_archiving

        if self.receiver_id is not None:
            result['ReceiverId'] = self.receiver_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentId') is not None:
            self.aiagent_id = m.get('AIAgentId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NeedArchiving') is not None:
            self.need_archiving = m.get('NeedArchiving')

        if m.get('ReceiverId') is not None:
            self.receiver_id = m.get('ReceiverId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

