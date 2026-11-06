# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentRuntimeStatisticRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        runtime_type: str = None,
    ):
        # The agent platform, which is used to filter the statistical scope, such as ENTERPRISE_AGENTIC_COMPUTER. If this parameter is not specified, all agent platforms are included in the statistics. If an unsupported value is specified, a parameter error is returned.
        self.agent_platform = agent_platform
        # The agent provider, which is used to filter the statistical scope, such as AgenticComputer. If this parameter is not specified, all agent providers are included in the statistics. If an unsupported value is specified, a parameter error is returned.
        self.agent_provider = agent_provider
        # The business type, which is used to filter runtimes of a specified business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The runtime environment type of the runtime resource.
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

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

