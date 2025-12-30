# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateAIAgentCallResponseBody(DaraModel):
    def __init__(
        self,
        aiagent_user_id: str = None,
        channel_id: str = None,
        instance_id: str = None,
        request_id: str = None,
        token: str = None,
        user_id: str = None,
    ):
        # The username of the AI agent in the Alibaba Real-Time Communication (ARTC) channel.
        self.aiagent_user_id = aiagent_user_id
        # The ARTC channel ID.
        self.channel_id = channel_id
        # The ID of the AI agent.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # The ARTC token of the client.
        self.token = token
        # The username in the ARTC channel.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiagent_user_id is not None:
            result['AIAgentUserId'] = self.aiagent_user_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAgentUserId') is not None:
            self.aiagent_user_id = m.get('AIAgentUserId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

