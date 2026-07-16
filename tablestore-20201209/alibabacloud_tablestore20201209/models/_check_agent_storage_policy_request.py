# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAgentStoragePolicyRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        policy: str = None,
    ):
        # The agent storage name.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The agent storage access control policy in JSON format.
        # 
        # This parameter is required.
        self.policy = policy

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

