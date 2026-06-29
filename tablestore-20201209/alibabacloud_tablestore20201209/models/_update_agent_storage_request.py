# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAgentStorageRequest(DaraModel):
    def __init__(
        self,
        agent_storage_description: str = None,
        agent_storage_name: str = None,
        alias_name: str = None,
        network: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
    ):
        # agent storage description
        self.agent_storage_description = agent_storage_description
        # agent storage name
        # 
        # This parameter is required.
        self.agent_storage_name = agent_storage_name
        # The alias of the agent storage.
        self.alias_name = alias_name
        # (Deprecated) The network type of the agent storage. Valid values: NORMAL and VPC_CONSOLE. Default value: NORMAL.
        self.network = network
        # The list of network sources allowed for the agent storage. All sources are allowed by default. Valid values:
        # - TRUST_PROXY: console.
        self.network_source_acl = network_source_acl
        # The list of network types allowed for the agent storage. All types are allowed by default. Valid values:
        # - CLASSIC: classic network.
        # - INTERNET: public network.
        # - VPC: VPC network.
        self.network_type_acl = network_type_acl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_storage_description is not None:
            result['AgentStorageDescription'] = self.agent_storage_description

        if self.agent_storage_name is not None:
            result['AgentStorageName'] = self.agent_storage_name

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.network is not None:
            result['Network'] = self.network

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStorageDescription') is not None:
            self.agent_storage_description = m.get('AgentStorageDescription')

        if m.get('AgentStorageName') is not None:
            self.agent_storage_name = m.get('AgentStorageName')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        return self

