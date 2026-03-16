# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class DiscoveryEndpoint(DaraModel):
    def __init__(
        self,
        agent_endpoint_configs: List[main_models.AgentEndpointConfig] = None,
        credential_name: str = None,
        name: str = None,
        return_agent_credential_content: bool = None,
    ):
        self.agent_endpoint_configs = agent_endpoint_configs
        # 该发现端点使用的凭证名称
        self.credential_name = credential_name
        self.name = name
        # 是否在发现结果中返回 agent 的凭证内容
        self.return_agent_credential_content = return_agent_credential_content

    def validate(self):
        if self.agent_endpoint_configs:
            for v1 in self.agent_endpoint_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agentEndpointConfigs'] = []
        if self.agent_endpoint_configs is not None:
            for k1 in self.agent_endpoint_configs:
                result['agentEndpointConfigs'].append(k1.to_map() if k1 else None)

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.name is not None:
            result['name'] = self.name

        if self.return_agent_credential_content is not None:
            result['returnAgentCredentialContent'] = self.return_agent_credential_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_endpoint_configs = []
        if m.get('agentEndpointConfigs') is not None:
            for k1 in m.get('agentEndpointConfigs'):
                temp_model = main_models.AgentEndpointConfig()
                self.agent_endpoint_configs.append(temp_model.from_map(k1))

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('returnAgentCredentialContent') is not None:
            self.return_agent_credential_content = m.get('returnAgentCredentialContent')

        return self

