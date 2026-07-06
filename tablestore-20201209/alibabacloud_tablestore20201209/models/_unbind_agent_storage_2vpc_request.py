# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindAgentStorage2VpcRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        agent_storage_vpc_name: str = None,
    ):
        # The agent storage name.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The VPC name.
        # 
        # This parameter is required.
        self.agent_storage_vpc_name = agent_storage_vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.agent_storage_vpc_name is not None:
            result['AgentStorageVpcName'] = self.agent_storage_vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('AgentStorageVpcName') is not None:
            self.agent_storage_vpc_name = m.get('AgentStorageVpcName')

        return self

