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
        # The agent list.
        self.agents = agents
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The default agent ID.
        self.default_id = default_id
        # The primary agent key name.
        self.main_key = main_key
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The routing scope.
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
        default: bool = None,
        files: List[main_models.DescribePolarClawAgentsResponseBodyAgentsFiles] = None,
        id: str = None,
        identity: main_models.DescribePolarClawAgentsResponseBodyAgentsIdentity = None,
        model: main_models.DescribePolarClawAgentsResponseBodyAgentsModel = None,
        name: str = None,
        skills: List[str] = None,
        workspace: str = None,
    ):
        # Indicates whether this is the default agent.
        self.default = default
        # The agent file list.
        self.files = files
        # Agent ID
        self.id = id
        # The identity information.
        self.identity = identity
        # The model configuration.
        self.model = model
        # The agent display name.
        self.name = name
        # The list of skills available to the agent.
        self.skills = skills
        # The working directory path.
        self.workspace = workspace

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.identity:
            self.identity.validate()
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.identity is not None:
            result['Identity'] = self.identity.to_map()

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.skills is not None:
            result['Skills'] = self.skills

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.DescribePolarClawAgentsResponseBodyAgentsFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Identity') is not None:
            temp_model = main_models.DescribePolarClawAgentsResponseBodyAgentsIdentity()
            self.identity = temp_model.from_map(m.get('Identity'))

        if m.get('Model') is not None:
            temp_model = main_models.DescribePolarClawAgentsResponseBodyAgentsModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

class DescribePolarClawAgentsResponseBodyAgentsModel(DaraModel):
    def __init__(
        self,
        fallbacks: List[str] = None,
        primary: str = None,
    ):
        # The fallback model list.
        self.fallbacks = fallbacks
        # The primary model.
        self.primary = primary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fallbacks is not None:
            result['Fallbacks'] = self.fallbacks

        if self.primary is not None:
            result['Primary'] = self.primary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fallbacks') is not None:
            self.fallbacks = m.get('Fallbacks')

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

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
        # The avatar path or content.
        self.avatar = avatar
        # The avatar URL.
        self.avatar_url = avatar_url
        # The emoji identifier in Unicode format such as U+1F99E, or a direct emoji character.
        self.emoji = emoji
        # The identity name.
        self.name = name
        # The theme.
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

class DescribePolarClawAgentsResponseBodyAgentsFiles(DaraModel):
    def __init__(
        self,
        missing: bool = None,
        name: str = None,
        path: str = None,
        size: int = None,
        updated_at_ms: int = None,
    ):
        # Indicates whether the file is missing.
        self.missing = missing
        # The file name.
        self.name = name
        # The file path.
        self.path = path
        # The file size, in bytes.
        self.size = size
        # The last updated timestamp, in milliseconds.
        self.updated_at_ms = updated_at_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.missing is not None:
            result['Missing'] = self.missing

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.size is not None:
            result['Size'] = self.size

        if self.updated_at_ms is not None:
            result['UpdatedAtMs'] = self.updated_at_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Missing') is not None:
            self.missing = m.get('Missing')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UpdatedAtMs') is not None:
            self.updated_at_ms = m.get('UpdatedAtMs')

        return self

