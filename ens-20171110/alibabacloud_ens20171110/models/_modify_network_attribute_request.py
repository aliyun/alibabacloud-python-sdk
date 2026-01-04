# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNetworkAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        network_id: str = None,
        network_name: str = None,
    ):
        # The description of the network.
        # 
        # The description must be 2 to 256 characters in length. It must start with a letter but cannot start with http:// or https://.
        self.description = description
        # The ID of the network.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The name of the network. The name must meet the following requirements:
        # 
        # *   The name must be 2 to 128 characters in length
        # *   It must start with a letter but cannot start with http:// or https://.
        # *   The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.network_name = network_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        return self

