# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolarClawAgentRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        avatar: str = None,
        emoji: str = None,
        restart: bool = None,
        workspace: str = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.application_id = application_id
        self.avatar = avatar
        self.emoji = emoji
        self.restart = restart
        # This parameter is required.
        self.workspace = workspace

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

        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.emoji is not None:
            result['Emoji'] = self.emoji

        if self.restart is not None:
            result['Restart'] = self.restart

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Emoji') is not None:
            self.emoji = m.get('Emoji')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

