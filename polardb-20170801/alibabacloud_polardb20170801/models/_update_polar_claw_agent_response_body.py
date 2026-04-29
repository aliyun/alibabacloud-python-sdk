# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdatePolarClawAgentResponseBody(DaraModel):
    def __init__(
        self,
        agent: main_models.UpdatePolarClawAgentResponseBodyAgent = None,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.agent = agent
        # Agent ID
        self.agent_id = agent_id
        self.application_id = application_id
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.agent:
            self.agent.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.UpdatePolarClawAgentResponseBodyAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdatePolarClawAgentResponseBodyAgent(DaraModel):
    def __init__(
        self,
        id: str = None,
        identity: main_models.UpdatePolarClawAgentResponseBodyAgentIdentity = None,
        name: str = None,
        workspace: str = None,
    ):
        # Agent ID
        self.id = id
        self.identity = identity
        self.name = name
        self.workspace = workspace

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.identity is not None:
            result['Identity'] = self.identity.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Identity') is not None:
            temp_model = main_models.UpdatePolarClawAgentResponseBodyAgentIdentity()
            self.identity = temp_model.from_map(m.get('Identity'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

class UpdatePolarClawAgentResponseBodyAgentIdentity(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        avatar_url: str = None,
        emoji: str = None,
        name: str = None,
        theme: str = None,
    ):
        self.avatar = avatar
        self.avatar_url = avatar_url
        self.emoji = emoji
        self.name = name
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.emoji is not None:
            result['Emoji'] = self.emoji

        if self.name is not None:
            result['Name'] = self.name

        if self.theme is not None:
            result['Theme'] = self.theme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('Emoji') is not None:
            self.emoji = m.get('Emoji')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Theme') is not None:
            self.theme = m.get('Theme')

        return self

