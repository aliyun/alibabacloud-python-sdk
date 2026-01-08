# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAckClusterConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        connector_name: str = None,
        ttl: str = None,
    ):
        # This parameter is required.
        self.connector_id = connector_id
        self.connector_name = connector_name
        self.ttl = ttl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        return self

