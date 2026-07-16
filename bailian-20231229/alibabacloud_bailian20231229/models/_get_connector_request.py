# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_id: str = None,
        connector_name: str = None,
    ):
        # The ID of the connector. You can find this ID in the [Model Studio console](https://bailian.console.aliyun.com/cn-beijing/?tab=app#/connector/list).
        self.connector_id = connector_id
        # The name of the connector to query. An exact match is required.
        self.connector_name = connector_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        return self

