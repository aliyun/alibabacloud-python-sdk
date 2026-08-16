# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelTemplateRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        description: str = None,
        name: str = None,
        ref_scope: str = None,
    ):
        # The Agent platform.
        self.agent_platform = agent_platform
        # The Agent provider name.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The description of the model group.
        self.description = description
        # The name of the model group.
        # 
        # This parameter is required.
        self.name = name
        # The authorization scope. This parameter is optional and effective only for Common model groups. Valid values: ALL_USER and USER_MIXED (strictly uppercase). If not specified, the default value is USER_MIXED for Common groups. Non-Common groups ignore this parameter and use RESOURCE_MIXED.
        self.ref_scope = ref_scope

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

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.ref_scope is not None:
            result['RefScope'] = self.ref_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefScope') is not None:
            self.ref_scope = m.get('RefScope')

        return self

