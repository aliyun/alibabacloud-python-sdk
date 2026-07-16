# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawAgentToolsResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        current_config: main_models.DescribePolarClawAgentToolsResponseBodyCurrentConfig = None,
        groups: List[main_models.DescribePolarClawAgentToolsResponseBodyGroups] = None,
        message: str = None,
        profiles: List[main_models.DescribePolarClawAgentToolsResponseBodyProfiles] = None,
        request_id: str = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The current tool configuration.
        self.current_config = current_config
        # The list of tool groups.
        self.groups = groups
        # The response message.
        self.message = message
        # The list of available profiles.
        self.profiles = profiles
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.current_config:
            self.current_config.validate()
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()
        if self.profiles:
            for v1 in self.profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.current_config is not None:
            result['CurrentConfig'] = self.current_config.to_map()

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        result['Profiles'] = []
        if self.profiles is not None:
            for k1 in self.profiles:
                result['Profiles'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentConfig') is not None:
            temp_model = main_models.DescribePolarClawAgentToolsResponseBodyCurrentConfig()
            self.current_config = temp_model.from_map(m.get('CurrentConfig'))

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribePolarClawAgentToolsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.profiles = []
        if m.get('Profiles') is not None:
            for k1 in m.get('Profiles'):
                temp_model = main_models.DescribePolarClawAgentToolsResponseBodyProfiles()
                self.profiles.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePolarClawAgentToolsResponseBodyProfiles(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
    ):
        # The profile identifier.
        self.id = id
        # The display name.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class DescribePolarClawAgentToolsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        id: str = None,
        label: str = None,
        source: str = None,
        tools: List[main_models.DescribePolarClawAgentToolsResponseBodyGroupsTools] = None,
    ):
        # The group identifier.
        self.id = id
        # The group name.
        self.label = label
        # The source, which is core or a plugin ID.
        self.source = source
        # The list of tools.
        self.tools = tools

    def validate(self):
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.source is not None:
            result['Source'] = self.source

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.DescribePolarClawAgentToolsResponseBodyGroupsTools()
                self.tools.append(temp_model.from_map(k1))

        return self

class DescribePolarClawAgentToolsResponseBodyGroupsTools(DaraModel):
    def __init__(
        self,
        default_profiles: List[str] = None,
        description: str = None,
        id: str = None,
        label: str = None,
        source: str = None,
    ):
        # The list of profiles that include this tool by default.
        self.default_profiles = default_profiles
        # The tool description.
        self.description = description
        # The tool identifier.
        self.id = id
        # The tool name.
        self.label = label
        # The source.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_profiles is not None:
            result['DefaultProfiles'] = self.default_profiles

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultProfiles') is not None:
            self.default_profiles = m.get('DefaultProfiles')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class DescribePolarClawAgentToolsResponseBodyCurrentConfig(DaraModel):
    def __init__(
        self,
        allow: List[str] = None,
        also_allow: List[str] = None,
        deny: List[str] = None,
        profile: str = None,
    ):
        # The list of explicitly allowed tools.
        self.allow = allow
        # The list of additionally allowed tools.
        self.also_allow = also_allow
        # The list of denied tools.
        self.deny = deny
        # The tool profile.
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow is not None:
            result['Allow'] = self.allow

        if self.also_allow is not None:
            result['AlsoAllow'] = self.also_allow

        if self.deny is not None:
            result['Deny'] = self.deny

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Allow') is not None:
            self.allow = m.get('Allow')

        if m.get('AlsoAllow') is not None:
            self.also_allow = m.get('AlsoAllow')

        if m.get('Deny') is not None:
            self.deny = m.get('Deny')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

