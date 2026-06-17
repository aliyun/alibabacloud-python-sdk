# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindPolarClawAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        channel: str = None,
        channel_account_id: str = None,
    ):
        # The agent ID to unbind.
        # 
        # This parameter is required.
        self.agent_id = agent_id
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The channel plugin ID.
        # 
        # This parameter is required.
        self.channel = channel
        # The channel account ID. Omit this parameter to remove all bindings for the specified agent ID and channel plugin ID.
        self.channel_account_id = channel_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.channel_account_id is not None:
            result['ChannelAccountId'] = self.channel_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ChannelAccountId') is not None:
            self.channel_account_id = m.get('ChannelAccountId')

        return self

