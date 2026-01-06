# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class GetApiDestinationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetApiDestinationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetApiDestinationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApiDestinationResponseBodyData(DaraModel):
    def __init__(
        self,
        api_destination_name: str = None,
        connection_name: str = None,
        description: str = None,
        gmt_create: int = None,
        http_api_parameters: main_models.GetApiDestinationResponseBodyDataHttpApiParameters = None,
    ):
        # The name of the API destination.
        self.api_destination_name = api_destination_name
        # The connection name.
        self.connection_name = connection_name
        # The description of the API destination.
        self.description = description
        # The time when the API destination was created.
        self.gmt_create = gmt_create
        # The request parameters that are configured for the API destination.
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

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

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('HttpApiParameters') is not None:
            temp_model = main_models.GetApiDestinationResponseBodyDataHttpApiParameters()
            self.http_api_parameters = temp_model.from_map(m.get('HttpApiParameters'))

        return self

class GetApiDestinationResponseBodyDataHttpApiParameters(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        method: str = None,
    ):
        # The endpoint of the API destination.
        self.endpoint = endpoint
        # The HTTP request method. Valid values:
        # 
        # *   POST
        # *   GET
        # *   DELETE
        # *   PUT
        # *   HEAD
        # *   TRACE
        # *   PATCH
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

