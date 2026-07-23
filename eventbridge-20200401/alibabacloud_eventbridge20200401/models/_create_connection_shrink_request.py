# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConnectionShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_parameters_shrink: str = None,
        connection_name: str = None,
        description: str = None,
        network_parameters_shrink: str = None,
        parameters_shrink: str = None,
        type: str = None,
    ):
        # The authentication configuration.
        self.auth_parameters_shrink = auth_parameters_shrink
        # The connection configuration name. Maximum length: 127 characters. Minimum length: 2 characters.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The description of the connection configuration. Maximum length: 255 characters.
        self.description = description
        # The network configuration.
        # 
        # This parameter is required.
        self.network_parameters_shrink = network_parameters_shrink
        # The data source connection parameters (JSON object). This parameter is required when Type is set to a data source type. This parameter is not required for the Http type. For specific field definitions, call the GetConnectionType operation and refer to ParamsSchema in the response.
        self.parameters_shrink = parameters_shrink
        # The connection type. Valid values: MySQL, PostgreSQL, Elasticsearch, and Http. This parameter is required for data source connections. If this parameter is not specified, the default value Http is used. The Http type is used for HTTP protocol targets such as API Destination. Data source types are used for data connections in the integration marketplace.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_parameters_shrink is not None:
            result['AuthParameters'] = self.auth_parameters_shrink

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.description is not None:
            result['Description'] = self.description

        if self.network_parameters_shrink is not None:
            result['NetworkParameters'] = self.network_parameters_shrink

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthParameters') is not None:
            self.auth_parameters_shrink = m.get('AuthParameters')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NetworkParameters') is not None:
            self.network_parameters_shrink = m.get('NetworkParameters')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

