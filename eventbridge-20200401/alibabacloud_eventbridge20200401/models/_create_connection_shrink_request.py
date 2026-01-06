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
    ):
        # The parameters that are configured for authentication.
        self.auth_parameters_shrink = auth_parameters_shrink
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The description of the connection. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the network.
        # 
        # This parameter is required.
        self.network_parameters_shrink = network_parameters_shrink

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

        return self

