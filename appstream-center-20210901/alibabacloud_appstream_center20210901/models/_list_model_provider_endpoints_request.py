# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelProviderEndpointsRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        provider_name: str = None,
    ):
        # The agent platform name. This parameter is not processed and is only passed through as a redundant field, such as ENTERPRISE.
        self.agent_platform = agent_platform
        # The agent provider name, such as HermesAgent or OpenClaw. If this parameter is specified, the providerName in the returned endpoints is the alias from the perspective of the specified agent provider.
        self.agent_provider = agent_provider
        # The business type.
        self.biz_type = biz_type
        # The name of the model provider, such as bailian, moonshot, or siliconflow. If this parameter is not specified, the endpoint configurations of all managed providers are returned.
        self.provider_name = provider_name

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

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

