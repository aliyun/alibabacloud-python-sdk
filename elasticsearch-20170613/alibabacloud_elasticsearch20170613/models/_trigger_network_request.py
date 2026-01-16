# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TriggerNetworkRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        network_type: str = None,
        node_type: str = None,
        client_token: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        # This parameter is required.
        self.network_type = network_type
        # This parameter is required.
        self.node_type = node_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['actionType'] = self.action_type

        if self.network_type is not None:
            result['networkType'] = self.network_type

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionType') is not None:
            self.action_type = m.get('actionType')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

