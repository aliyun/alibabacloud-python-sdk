# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class UpdateApiDestinationRequest(DaraModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        http_api_parameters: main_models.UpdateApiDestinationRequestHttpApiParameters = None,
    ):
        # The name of the API destination. The name must be 2 to 127 characters in length.
        # 
        # This parameter is required.
        self.api_destination_name = api_destination_name
        # The name of the connection. The name must be 2 to 127 characters in length.
        # 
        # Note: Before you configure this parameter, you must call the CreateConnection operation to create a connection. Then, set this parameter to the name of the connection that you created.
        self.connection_name = connection_name
        # The description of the API destination. The description can be up to 255 characters in length.
        self.description = description
        # The parameters that are configured for the API destination.
        self.http_api_parameters = http_api_parameters

    def validate(self):
        if self.http_api_parameters:
            self.http_api_parameters.validate()

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

        if self.http_api_parameters is not None:
            result['HttpApiParameters'] = self.http_api_parameters.to_map()

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
            temp_model = main_models.UpdateApiDestinationRequestHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m.get('HttpApiParameters'))

        return self

class UpdateApiDestinationRequestHttpApiParameters(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination. The endpoint can be up to 127 characters in length.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # - GET
        # - POST
        # - HEAD
        # - DELETE
        # - PUT
        # - PATCH
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.method is not None:
            result['Method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        return self

