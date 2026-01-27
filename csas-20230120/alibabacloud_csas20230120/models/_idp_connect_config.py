# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IdpConnectConfig(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        use_connector: bool = None,
    ):
        self.connector_id = connector_id
        self.use_connector = use_connector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.use_connector is not None:
            result['UseConnector'] = self.use_connector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('UseConnector') is not None:
            self.use_connector = m.get('UseConnector')

        return self

