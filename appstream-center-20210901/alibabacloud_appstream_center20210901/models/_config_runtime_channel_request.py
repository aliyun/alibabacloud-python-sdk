# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigRuntimeChannelRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        code: str = None,
        config: str = None,
        config_mode: str = None,
        name: str = None,
        runtime_ids: List[str] = None,
        runtime_type: str = None,
    ):
        # The Agent platform (such as ENTERPRISE or JVS).
        self.agent_platform = agent_platform
        # The Agent provider.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The third-party channel code.
        # 
        # This parameter is required.
        self.code = code
        # The channel configuration JSON string.
        # 
        # This parameter is required.
        self.config = config
        # The configuration mode.
        self.config_mode = config_mode
        # The channel name.
        # 
        # If you leave this parameter empty, the system automatically uses the value of Code as the name.
        self.name = name
        # The list of runtime IDs.
        # 
        # This parameter is required.
        self.runtime_ids = runtime_ids
        # The Agent runtime type.
        # 
        # This parameter is required.
        self.runtime_type = runtime_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.config_mode is not None:
            result['ConfigMode'] = self.config_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.runtime_ids is not None:
            result['RuntimeIds'] = self.runtime_ids

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConfigMode') is not None:
            self.config_mode = m.get('ConfigMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuntimeIds') is not None:
            self.runtime_ids = m.get('RuntimeIds')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

