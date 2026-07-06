# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAgentStoragePolicyRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        policy_version: int = None,
    ):
        # The name of the agent storage.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The version of the access control policy for agent storage.
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

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        return self

