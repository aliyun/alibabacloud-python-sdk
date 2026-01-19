# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProcessCustomIMCallbackRequest(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        conversation_id: str = None,
        instance_id: str = None,
        message_content: str = None,
        request_id: str = None,
        sender_avatar_media_id: str = None,
        sender_id: str = None,
        sender_name: str = None,
    ):
        # This parameter is required.
        self.access_channel_id = access_channel_id
        # This parameter is required.
        self.conversation_id = conversation_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_content = message_content
        self.request_id = request_id
        self.sender_avatar_media_id = sender_avatar_media_id
        # This parameter is required.
        self.sender_id = sender_id
        self.sender_name = sender_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_content is not None:
            result['MessageContent'] = self.message_content

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sender_avatar_media_id is not None:
            result['SenderAvatarMediaId'] = self.sender_avatar_media_id

        if self.sender_id is not None:
            result['SenderId'] = self.sender_id

        if self.sender_name is not None:
            result['SenderName'] = self.sender_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageContent') is not None:
            self.message_content = m.get('MessageContent')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SenderAvatarMediaId') is not None:
            self.sender_avatar_media_id = m.get('SenderAvatarMediaId')

        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')

        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')

        return self

