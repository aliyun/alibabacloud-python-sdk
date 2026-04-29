# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawAgentsResponseBody(DaraModel):
    def __init__(
        self,
        agents: List[main_models.DescribePolarClawAgentsResponseBodyAgents] = None,
        application_id: str = None,
        code: int = None,
        default_id: str = None,
        main_key: str = None,
        message: str = None,
        request_id: str = None,
        scope: str = None,
    ):
        self.agents = agents
        self.application_id = application_id
        self.code = code
        self.default_id = default_id
        self.main_key = main_key
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.scope = scope

    def validate(self):
        if self.agents:
            for v1 in self.agents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agents'] = []
        if self.agents is not None:
            for k1 in self.agents:
                result['Agents'].append(k1.to_map() if k1 else None)

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.default_id is not None:
            result['DefaultId'] = self.default_id

        if self.main_key is not None:
            result['MainKey'] = self.main_key

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agents = []
        if m.get('Agents') is not None:
            for k1 in m.get('Agents'):
                temp_model = main_models.DescribePolarClawAgentsResponseBodyAgents()
                self.agents.append(temp_model.from_map(k1))

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultId') is not None:
            self.default_id = m.get('DefaultId')

        if m.get('MainKey') is not None:
            self.main_key = m.get('MainKey')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

class DescribePolarClawAgentsResponseBodyAgents(DaraModel):
    def __init__(
        self,
        id: str = None,
        identity: main_models.DescribePolarClawAgentsResponseBodyAgentsIdentity = None,
        name: str = None,
    ):
        # Agent ID
        self.id = id
        self.identity = identity
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Identity') is not None:
            temp_model = main_models.DescribePolarClawAgentsResponseBodyAgentsIdentity()
            self.identity = temp_model.from_map(m.get('Identity'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribePolarClawAgentsResponseBodyAgentsIdentity(DaraModel):
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

