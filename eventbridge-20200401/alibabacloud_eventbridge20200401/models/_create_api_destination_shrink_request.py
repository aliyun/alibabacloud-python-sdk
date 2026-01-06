# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiDestinationShrinkRequest(DaraModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters_shrink: str = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        # 
        # This parameter is required.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # > 
        # >  Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        # 
        # This parameter is required.
        self.http_api_parameters_shrink = http_api_parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_destination_name is not None:
            result['ApiDestinationName'] = self.api_destination_name

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.description is not None:
            result['Description'] = self.description

        if self.http_api_parameters_shrink is not None:
            result['HttpApiParameters'] = self.http_api_parameters_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiDestinationName') is not None:
            self.api_destination_name = m.get('ApiDestinationName')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HttpApiParameters') is not None:
            self.http_api_parameters_shrink = m.get('HttpApiParameters')

        return self

