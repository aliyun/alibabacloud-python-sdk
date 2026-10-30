# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class PrepareIdentityProviderSCIMResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PrepareIdentityProviderSCIMResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code. If the request fails, handle the error based on the HTTP status code and the message.
        self.code = code
        # The operation result. For the result structure, see the response fields of this API. For asynchronous write APIs, the response indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The processing status of the current request. This status is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # The request acceptance or error message. For asynchronous tasks, you must check the task result by using the corresponding query API.
        self.message = message
        # The request ID. It is used to associate the current call with troubleshooting. Retain this ID if the request fails.
        self.request_id = request_id
        # Indicates whether the current request is processed successfully. A value of true indicates success. For asynchronous write operations, you must continue to query the task result.
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
            temp_model = main_models.PrepareIdentityProviderSCIMResponseBodyData()
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

class PrepareIdentityProviderSCIMResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration: main_models.PrepareIdentityProviderSCIMResponseBodyDataConfiguration = None,
        credential: main_models.PrepareIdentityProviderSCIMResponseBodyDataCredential = None,
        token: str = None,
    ):
        # The actual SAML configuration is read on demand only by using GetIdentityProvider. SCIM query and prepare operations return the actual receiving status and URL.
        self.configuration = configuration
        # The current credential summary, which includes the credentialId, status, createTime, and expireTime fields. This summary does not include the token.
        self.credential = credential
        # The plaintext token is returned only when a new credential is created. If the prepare operation reuses a valid credential, this field is null. The token cannot be retrieved again from the list. If the response is lost, query the list first instead of automatically reissuing the token. Do not write the token to logs or persist it in frontend caches.
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
            temp_model = main_models.PrepareIdentityProviderSCIMResponseBodyDataConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('credential') is not None:
            temp_model = main_models.PrepareIdentityProviderSCIMResponseBodyDataCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

class PrepareIdentityProviderSCIMResponseBodyDataCredential(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        # The creation time returned by AgentIdentity.
        self.create_time = create_time
        # The credential ID. This parameter is required and cannot be empty when you delete a credential. Use the ID returned in the credential list, not the plaintext token.
        self.credential_id = credential_id
        # The expiration time returned by AgentIdentity. Only credentials that are in the Enabled state and have not expired are considered available.
        self.expire_time = expire_time
        # The credential status of AgentIdentity. Only credentials that are in the Enabled state and have not expired are considered available. This field is not the operationStatus of a SCIM task.
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

class PrepareIdentityProviderSCIMResponseBodyDataConfiguration(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        status: str = None,
    ):
        # The URL configured for the external provisioning system. The presence of a URL does not indicate that the external configuration is completed or that access control synchronization is enabled.
        self.base_url = base_url
        # The receiving status of AgentIdentity. Enabled indicates that SCIM receiving is enabled, and Disabled indicates that it is disabled. This status is not equivalent to the expected value of syncEnabled for access control.
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

