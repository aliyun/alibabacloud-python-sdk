# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnectionShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_parameters_shrink: str = None,
        connection_name: str = None,
        description: str = None,
        network_parameters_shrink: str = None,
        parameters_shrink: str = None,
        type: str = None,
    ):
        # The data structure of the authentication parameters.
        self.auth_parameters_shrink = auth_parameters_shrink
        # The name of the connection to be updated. The maximum length is 127 characters. The minimum length is 2 characters.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The description. The maximum length is 255 characters.
        self.description = description
        # The data structure of the network configuration.
        # 
        # This parameter is required.
        self.network_parameters_shrink = network_parameters_shrink
        # The data source connection parameters (JSON object). For specific field definitions, call the GetConnectionType API and refer to the ParamsSchema in the response.
        self.parameters_shrink = parameters_shrink
        # The connection type. Valid values: MySQL, PostgreSQL, Elasticsearch, and Http.
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

