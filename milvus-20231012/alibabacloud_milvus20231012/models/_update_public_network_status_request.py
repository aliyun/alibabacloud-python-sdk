# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePublicNetworkStatusRequest(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        component_type: str = None,
        instance_id: str = None,
        public_network_enabled: bool = None,
    ):
        # The CIDR blocks.
        self.cidr = cidr
        # The component type. Valid values:
        # 
        # *   Proxy
        # 
        # This parameter is required.
        self.component_type = component_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Enable /disable the Internet.
        # 
        # This parameter is required.
        self.public_network_enabled = public_network_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.public_network_enabled is not None:
            result['PublicNetworkEnabled'] = self.public_network_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicNetworkEnabled') is not None:
            self.public_network_enabled = m.get('PublicNetworkEnabled')

        return self

