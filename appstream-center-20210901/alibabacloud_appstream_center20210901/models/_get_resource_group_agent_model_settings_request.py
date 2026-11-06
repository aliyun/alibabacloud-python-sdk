# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetResourceGroupAgentModelSettingsRequest(DaraModel):
    def __init__(
        self,
        agent_platform: str = None,
        agent_provider: str = None,
        biz_type: int = None,
        resource_group_ids: List[str] = None,
    ):
        # The agent platform type.
        self.agent_platform = agent_platform
        # The agent provider name.
        # 
        # This parameter is required.
        self.agent_provider = agent_provider
        # The business type.
        # 
        # This parameter is required.
        self.biz_type = biz_type
        # The list of resource group IDs.
        # 
        # This parameter is required.
        self.resource_group_ids = resource_group_ids

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

        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPlatform') is not None:
            self.agent_platform = m.get('AgentPlatform')

        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')

        return self

