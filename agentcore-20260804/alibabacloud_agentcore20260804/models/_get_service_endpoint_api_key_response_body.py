# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetServiceEndpointApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetServiceEndpointApiKeyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value is SUCCESS when the request succeeds.
        self.code = code
        # The currently active API Key information for the service endpoint.
        self.data = data
        # The HTTP status code. The value is 200 when the request succeeds.
        self.http_status_code = http_status_code
        # The response message. The value is success when the request succeeds.
        self.message = message
        # The request ID, used for troubleshooting and tracing.
        self.request_id = request_id
        # Indicates whether the request was successful. The value is true when the request succeeds.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

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

        if m.get('data') is not None:
            temp_model = main_models.GetServiceEndpointApiKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetServiceEndpointApiKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        api_key_fingerprint: str = None,
        api_key_name: str = None,
        api_key_source: str = None,
        authentication_type: str = None,
        service_endpoint_id: str = None,
        workspace_id: str = None,
    ):
        # The currently active API Key for the service endpoint. The service reads this value from the gateway consumer in real time. AgentCore does not persist the plaintext. When calling the service endpoint, include this value in the request header specified by apiKeyName. Do not log this value or expose it in public configurations.
        self.api_key = api_key
        # The API Key fingerprint, which consists of the first 12 lowercase hexadecimal characters of the SHA-256 digest of the API Key. It can be used to identify the key version but cannot replace the API Key for authentication.
        self.api_key_fingerprint = api_key_fingerprint
        # The name of the HTTP request header used to pass the API Key. The value is currently fixed to x-api-key.
        self.api_key_name = api_key_name
        # The location where the API Key is passed. The value is currently fixed to Header, indicating that the API Key is passed through an HTTP request header.
        self.api_key_source = api_key_source
        # The authentication type of the service endpoint. Valid values:
        # - NONE: Authentication is not enabled.
        # - API_KEY: API Key authentication is used.
        # 
        # This operation succeeds only when the authentication type is API_KEY. Therefore, the value API_KEY is always returned in a successful response.
        self.authentication_type = authentication_type
        # The service endpoint ID.
        self.service_endpoint_id = service_endpoint_id
        # The ID of the workspace to which the service endpoint belongs.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.api_key_fingerprint is not None:
            result['apiKeyFingerprint'] = self.api_key_fingerprint

        if self.api_key_name is not None:
            result['apiKeyName'] = self.api_key_name

        if self.api_key_source is not None:
            result['apiKeySource'] = self.api_key_source

        if self.authentication_type is not None:
            result['authenticationType'] = self.authentication_type

        if self.service_endpoint_id is not None:
            result['serviceEndpointId'] = self.service_endpoint_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('apiKeyFingerprint') is not None:
            self.api_key_fingerprint = m.get('apiKeyFingerprint')

        if m.get('apiKeyName') is not None:
            self.api_key_name = m.get('apiKeyName')

        if m.get('apiKeySource') is not None:
            self.api_key_source = m.get('apiKeySource')

        if m.get('authenticationType') is not None:
            self.authentication_type = m.get('authenticationType')

        if m.get('serviceEndpointId') is not None:
            self.service_endpoint_id = m.get('serviceEndpointId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

