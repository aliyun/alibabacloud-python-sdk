# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListIdentityProviderSCIMCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListIdentityProviderSCIMCredentialsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business result code. If the request fails, handle the error based on the HTTP status code and the message.
        self.code = code
        # The operation result. For the result structure, see the response fields of this operation. For asynchronous write operations, the response indicates that the request is accepted, but does not guarantee that the background task is completed.
        self.data = data
        # The HTTP status code of the current request. This code indicates the processing status of the request and is not equivalent to the final result of the background task.
        self.http_status_code = http_status_code
        # Task result message, which indicates that the request is accepted or contains an error message. For task results of asynchronous tasks, check the corresponding query operation.
        self.message = message
        # The request ID, which is used to associate the current call with troubleshooting. Retain this ID if the request fails.
        self.request_id = request_id
        # Indicates whether the current request is successful. A value of true indicates that the request is processed successfully. For asynchronous write operations, you still need to query the task results.
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
                temp_model = main_models.ListIdentityProviderSCIMCredentialsResponseBodyData()
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

class ListIdentityProviderSCIMCredentialsResponseBodyData(DaraModel):
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
        # The expiration time returned by AgentIdentity. Only credentials with a status of Enabled that have not expired are considered available.
        self.expire_time = expire_time
        # The credential status of AgentIdentity. Only credentials with a status of Enabled that have not expired are considered available. This field is not the operationStatus of a SCIM task.
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

