# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePublicNetworkStatusRequest(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        instance_id: str = None,
        node_group_id: str = None,
        public_network_enabled: bool = None,
    ):
        self.component_type = component_type
        # This parameter is required.
        self.instance_id = instance_id
        self.node_group_id = node_group_id
        self.public_network_enabled = public_network_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.public_network_enabled is not None:
            result['PublicNetworkEnabled'] = self.public_network_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('PublicNetworkEnabled') is not None:
            self.public_network_enabled = m.get('PublicNetworkEnabled')

        return self

