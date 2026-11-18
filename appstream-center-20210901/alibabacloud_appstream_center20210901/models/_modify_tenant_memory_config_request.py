# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTenantMemoryConfigRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        enabled: bool = None,
    ):
        # The business platform to which the agent belongs. Specify the platform that corresponds to the tenant memory configuration, such as the enterprise platform `ENTERPRISE`.
        # 
        # This parameter is required.
        self.agent_platform = agent_platform
        # The agent provider. Used together with AgentPlatform and BizType to locate the memory configuration. A configured business combination must be used.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The business type code. Used together with the provider and business platform. Common values include `1` (Enterprise Edition), `10` (Personal Edition), and `20` (Commercial Edition).
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # Specifies whether to enable the memory feature for the business combination. A value of `true` enables the feature, and `false` disables it. If this parameter is omitted, the current status is retained.
        self.enabled = enabled

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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

