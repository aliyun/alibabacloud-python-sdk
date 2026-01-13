# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        network: str = None,
        network_source_acl: List[str] = None,
        network_type_acl: List[str] = None,
    ):
        # The alias of the instance.
        self.alias_name = alias_name
        # The description of the instance.
        self.instance_description = instance_description
        # The name of the instance whose information you want to update.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # (Deprecated) The network type of the instance. Valid values: NORMAL and VPC_CONSOLE. Default value: NORMAL.
        self.network = network
        # The new sources of the network from which access is allowed. By default, all sources of networks are allowed. Valid value:
        # 
        # TRUST_PROXY: the console
        self.network_source_acl = network_source_acl
        # The new types of the network from which access is allowed. By default, all types of networks are allowed. Valid values:
        # 
        # *   INTERNET: the Internet
        # *   VPC: VPCs
        # *   CLASSIC: the classic network
        self.network_type_acl = network_type_acl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.network is not None:
            result['Network'] = self.network

        if self.network_source_acl is not None:
            result['NetworkSourceACL'] = self.network_source_acl

        if self.network_type_acl is not None:
            result['NetworkTypeACL'] = self.network_type_acl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('NetworkSourceACL') is not None:
            self.network_source_acl = m.get('NetworkSourceACL')

        if m.get('NetworkTypeACL') is not None:
            self.network_type_acl = m.get('NetworkTypeACL')

        return self

