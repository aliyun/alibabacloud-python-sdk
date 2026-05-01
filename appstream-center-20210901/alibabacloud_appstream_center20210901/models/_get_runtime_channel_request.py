# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRuntimeChannelRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        include_risk_info: bool = None,
        runtime_id: str = None,
        runtime_type: str = None,
    ):
        self.agent_platform = agent_platform
        # This parameter is required.
        self.agent_provider = agent_provider
        self.include_risk_info = include_risk_info
        # This parameter is required.
        self.runtime_id = runtime_id
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

        if self.include_risk_info is not None:
            result['IncludeRiskInfo'] = self.include_risk_info

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('IncludeRiskInfo') is not None:
            self.include_risk_info = m.get('IncludeRiskInfo')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self

