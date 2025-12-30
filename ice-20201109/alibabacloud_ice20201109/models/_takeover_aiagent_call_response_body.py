# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TakeoverAIAgentCallResponseBody(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        human_agent_user_id: str = None,
        request_id: str = None,
        token: str = None,
    ):
        # The ID of the ARTC channel.
        self.channel_id = channel_id
        # The ID of the human agent.
        self.human_agent_user_id = human_agent_user_id
        # The ID of the request.
        self.request_id = request_id
        # The ARTC token.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.human_agent_user_id is not None:
            result['HumanAgentUserId'] = self.human_agent_user_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('HumanAgentUserId') is not None:
            self.human_agent_user_id = m.get('HumanAgentUserId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

