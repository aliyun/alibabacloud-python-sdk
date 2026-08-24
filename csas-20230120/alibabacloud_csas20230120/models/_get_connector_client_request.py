# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectorClientRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        dev_tag: str = None,
    ):
        # The connector ID. You can call [ListConnectors](~~ListConnectors~~) to query connectors.
        # 
        # This parameter is required.
        self.connector_id = connector_id
        # The unique device identifier of the ConnectorClient. You can call [ListConnectors](~~ListConnectors~~) to query connectors.
        # 
        # This parameter is required.
        self.dev_tag = dev_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        return self

