# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteNetworkInterfacesShrinkRequest(DaraModel):
    def __init__(
        self,
        network_interface_ids_shrink: str = None,
    ):
        # The IDs of the elastic network interfaces (ENIs).
        # 
        # This parameter is required.
        self.network_interface_ids_shrink = network_interface_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_ids_shrink is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceIds') is not None:
            self.network_interface_ids_shrink = m.get('NetworkInterfaceIds')

        return self

