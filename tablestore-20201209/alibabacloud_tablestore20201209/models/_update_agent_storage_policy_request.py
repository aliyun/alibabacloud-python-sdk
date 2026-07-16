# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentStoragePolicyRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        policy: str = None,
        policy_version: int = None,
    ):
        # The name of the agent storage.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The access control policy of the agent storage in JSON format. For more information, see https://www.alibabacloud.com/help/en/ram/user-guide/policy-structure-and-syntax.
        # 
        # This parameter is required.
        self.policy = policy
        # The version of the agent storage access control policy.
        # 
        # This parameter is required.
        self.policy_version = policy_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        return self

