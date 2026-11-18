# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTenantMemoryConfigRequest(DaraModel):
    def __init__(
        self,
        agent_instance_id: str = None,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
    ):
        # This parameter is not enabled. Do not specify this parameter. The current API operation queries tenant configurations by provider, business platform, and business type. The example is used to illustrate the field status.
        self.agent_instance_id = agent_instance_id
        # The business platform to which the agent belongs. Specify the platform corresponding to the tenant memory configuration, such as the enterprise platform `ENTERPRISE`.
        self.agent_platform = agent_platform
        # The agent provider. This parameter is used together with AgentPlatform and BizType to locate the memory configuration. You must use a configured business combination.
        self.agent_provider = agent_provider
        # The business type code. This parameter is used together with the provider and business platform. Common values include `1` (Enterprise Edition), `10` (Personal Edition), and `20` (Commercial Edition).
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_instance_id is not None:
            result['AgentInstanceId'] = self.agent_instance_id

        if self.agent_platform is not None:
            result['AgentPlatform'] = self.agent_platform

        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentInstanceId') is not None:
            self.agent_instance_id = m.get('AgentInstanceId')

        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        return self

