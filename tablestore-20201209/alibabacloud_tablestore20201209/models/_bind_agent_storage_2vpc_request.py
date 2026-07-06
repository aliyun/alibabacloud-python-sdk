# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAgentStorage2VpcRequest(DaraModel):
    def __init__(
        self,
        agent_storage_name: str = None,
        agent_storage_vpc_name: str = None,
        virtual_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The agent storage name.
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The VPC name.
        # 
        # This parameter is required.
        self.agent_storage_vpc_name = agent_storage_vpc_name
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.virtual_switch_id = virtual_switch_id
        # VPC ID
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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

        if self.virtual_switch_id is not None:
            result['VirtualSwitchId'] = self.virtual_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('AgentStorageVpcName') is not None:
            self.agent_storage_vpc_name = m.get('AgentStorageVpcName')

        if m.get('VirtualSwitchId') is not None:
            self.virtual_switch_id = m.get('VirtualSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

