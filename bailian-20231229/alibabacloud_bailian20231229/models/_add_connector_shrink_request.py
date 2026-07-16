# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddConnectorShrinkRequest(DaraModel):
    def __init__(
        self,
        connector_name: str = None,
        connector_type: str = None,
        description: str = None,
        file_connector_config_shrink: str = None,
    ):
        # The name of the connector.
        # 
        # This parameter is required.
        self.connector_name = connector_name
        # The type of the connector.
        # 
        # This parameter is required.
        self.connector_type = connector_type
        # The description for the connector.
        # 
        # This parameter is required.
        self.description = description
        # The parameters for the file connector.
        self.file_connector_config_shrink = file_connector_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.connector_type is not None:
            result['ConnectorType'] = self.connector_type

        if self.description is not None:
            result['Description'] = self.description

        if self.file_connector_config_shrink is not None:
            result['FileConnectorConfig'] = self.file_connector_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('ConnectorType') is not None:
            self.connector_type = m.get('ConnectorType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileConnectorConfig') is not None:
            self.file_connector_config_shrink = m.get('FileConnectorConfig')

        return self

