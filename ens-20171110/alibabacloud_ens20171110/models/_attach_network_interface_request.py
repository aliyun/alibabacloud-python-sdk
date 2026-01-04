# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachNetworkInterfaceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        network_interface_id: str = None,
    ):
        # The ID of the instance
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the ENI.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        return self

