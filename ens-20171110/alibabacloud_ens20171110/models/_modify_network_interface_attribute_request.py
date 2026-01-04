# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNetworkInterfaceAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
    ):
        # The description. The description must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The ID of the ENI.
        # 
        # This parameter is required.
        self.network_interface_id = network_interface_id
        # The name of the ENI. The name must be 1 to 128 characters in length, The name cannot start with http:// or https://.
        self.network_interface_name = network_interface_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        return self

