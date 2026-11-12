# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderSCIMResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderSCIMResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the request fails, handle the error based on the HTTP status code and the message.
        self.code = code
        # For the result structure, see the response fields of this operation. The response of an asynchronous write operation indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The processing status of this request, which is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # The request acceptance or error message. For asynchronous tasks, verify the task result by using the corresponding query operation.
        self.message = message
        # Used to associate this call with troubleshooting. Retain this ID if the call fails.
        self.request_id = request_id
        # A value of true indicates that the current request is processed successfully. For asynchronous writes, you must continue to query the task results.
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
            temp_model = main_models.GetIdentityProviderSCIMResponseBodyData()
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

class GetIdentityProviderSCIMResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.GetIdentityProviderSCIMResponseBodyDataConfiguration = None,
        operation_status: str = None,
        status: str = None,
        sync_enabled: bool = None,
    ):
        # The actual SAML configuration is read back on demand only in GetIdentityProvider. SCIM queries and preparations return the actual receiving status and URL.
        self.configuration = configuration
        # The original status of the most recent independent SCIM operation task. An empty string ("") is returned if no historical tasks exist.
        self.operation_status = operation_status
        # The SCIM independent configuration status.
        self.status = status
        # Do not pass true during CustomSSO initialization. Subsequently, it can only be updated through UpdateIdentityProviderSCIM, and the result is determined in combination with operationStatus.
        self.sync_enabled = sync_enabled

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status

        if self.status is not None:
            result['status'] = self.status

        if self.sync_enabled is not None:
            result['syncEnabled'] = self.sync_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.GetIdentityProviderSCIMResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('syncEnabled') is not None:
            self.sync_enabled = m.get('syncEnabled')

        return self

class GetIdentityProviderSCIMResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        status: str = None,
    ):
        # The URL configured for the external provisioning system. The presence of a URL does not mean that the external configuration is completed or AgentCore synchronization is enabled.
        self.base_url = base_url
        # Enabled indicates that SCIM receiving is enabled, and Disabled indicates that it is disabled. This is not equivalent to the expected value of syncEnabled in AgentCore.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['baseUrl'] = self.base_url

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baseUrl') is not None:
            self.base_url = m.get('baseUrl')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

