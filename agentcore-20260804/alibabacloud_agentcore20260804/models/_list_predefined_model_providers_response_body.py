# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListPredefinedModelProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListPredefinedModelProvidersResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value is SUCCESS if the request is successful.
        self.code = code
        # The list of predefined model providers.
        self.data = data
        # The HTTP status code. The value is 200 if the request is successful.
        self.http_status_code = http_status_code
        # The message about the request processing result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListPredefinedModelProvidersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListPredefinedModelProvidersResponseBodyData(DaraModel):
    def __init__(
        self,
        default_endpoint: str = None,
        default_protocol: str = None,
        display_name: str = None,
        provider_type: str = None,
    ):
        # The default model service endpoint of the provider.
        self.default_endpoint = default_endpoint
        # The default model invocation protocol of the provider.
        self.default_protocol = default_protocol
        # The display name of the model provider.
        self.display_name = display_name
        # The model provider type.
        self.provider_type = provider_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_endpoint is not None:
            result['defaultEndpoint'] = self.default_endpoint

        if self.default_protocol is not None:
            result['defaultProtocol'] = self.default_protocol

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.provider_type is not None:
            result['providerType'] = self.provider_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultEndpoint') is not None:
            self.default_endpoint = m.get('defaultEndpoint')

        if m.get('defaultProtocol') is not None:
            self.default_protocol = m.get('defaultProtocol')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')

        return self

