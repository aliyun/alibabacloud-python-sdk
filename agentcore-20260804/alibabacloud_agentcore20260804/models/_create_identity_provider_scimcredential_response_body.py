# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class CreateIdentityProviderSCIMCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateIdentityProviderSCIMCredentialResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code. Combine it with the HTTP status and message for handling upon failure.
        self.code = code
        # The operation result. For the result structure, see the response fields of this operation. The response of an asynchronous write operation indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The HTTP status code of the current request. It is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # Task result message, indicating request acceptance or an error. For asynchronous tasks, check task results by using the corresponding query operation.
        self.message = message
        # The request ID. It is used to associate the current call with troubleshooting. Keep it when a failure occurs.
        self.request_id = request_id
        # Indicates whether the current request is successful. A value of true indicates that the request is processed successfully. For asynchronous writes, you still need to continue querying the task results.
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
            temp_model = main_models.CreateIdentityProviderSCIMCredentialResponseBodyData()
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

class CreateIdentityProviderSCIMCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.CreateIdentityProviderSCIMCredentialResponseBodyDataConfiguration = None,
        credential: main_models.CreateIdentityProviderSCIMCredentialResponseBodyDataCredential = None,
        token: str = None,
    ):
        # The AgentIdentity reception configuration. The actual SAML configuration is read back on demand only in GetIdentityProvider. SCIM queries and preparations return the actual reception status and URL.
        self.configuration = configuration
        # The current credential summary, including credentialId, status, createTime, and expireTime. It does not include the token, which cannot be retrieved repeatedly.
        self.credential = credential
        # The token. The plaintext is returned only when a new credential is created. It is null when prepare reuses a valid credential. It cannot be retrieved again from the list. If the response is lost, query the list first instead of automatically re-issuing it. Do not write it to logs or frontend persistent cache.
        self.token = token

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.CreateIdentityProviderSCIMCredentialResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('credential') is not None:
            temp_model = main_models.CreateIdentityProviderSCIMCredentialResponseBodyDataCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

class CreateIdentityProviderSCIMCredentialResponseBodyDataCredential(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        # The creation time returned by AgentIdentity.
        self.create_time = create_time
        # The credential ID. It must be non-empty when deleting a credential. Use the ID returned in the credential list, not the plaintext token.
        self.credential_id = credential_id
        # The expiration time returned by AgentIdentity. Only credentials that are Enabled and have not expired are considered available.
        self.expire_time = expire_time
        # The AgentIdentity credential status. Only credentials that are Enabled and have not expired are considered available. This field is not the operationStatus of a SCIM task.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.credential_id is not None:
            result['credentialId'] = self.credential_id

        if self.expire_time is not None:
            result['expireTime'] = self.expire_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('credentialId') is not None:
            self.credential_id = m.get('credentialId')

        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateIdentityProviderSCIMCredentialResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        status: str = None,
    ):
        # The URL configured for the external provisioning system. The presence of an address does not mean that the external configuration is completed or AC synchronization is enabled.
        self.base_url = base_url
        # The AgentIdentity reception status. Enabled indicates that SCIM reception is enabled, and Disabled indicates that it is disabled. This is not equivalent to the expected value of syncEnabled in AC.
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

