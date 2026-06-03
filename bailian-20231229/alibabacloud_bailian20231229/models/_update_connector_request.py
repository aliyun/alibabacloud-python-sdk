# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnectorRequest(DaraModel):
    def __init__(
        self,
        connector_name: str = None,
        description: str = None,
    ):
        # This parameter is required.
        self.connector_name = connector_name
        # This parameter is required.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

