# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentIMChannelCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateAgentIMChannelCredentialResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code. The value SUCCESS indicates success.
        self.code = code
        # The summary of the updated IM channel credential.
        self.data = data
        # The HTTP status code. The value 200 indicates success.
        self.http_status_code = http_status_code
        # The result message of the request.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.UpdateAgentIMChannelCredentialResponseBodyData()
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

class UpdateAgentIMChannelCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        configured_secret_fields: List[str] = None,
        non_secret_fields: Dict[str, str] = None,
    ):
        # The list of configured secret field names. Secret values are not included.
        self.configured_secret_fields = configured_secret_fields
        # The non-sensitive credential fields and their values.
        self.non_secret_fields = non_secret_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured_secret_fields is not None:
            result['configuredSecretFields'] = self.configured_secret_fields

        if self.non_secret_fields is not None:
            result['nonSecretFields'] = self.non_secret_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuredSecretFields') is not None:
            self.configured_secret_fields = m.get('configuredSecretFields')

        if m.get('nonSecretFields') is not None:
            self.non_secret_fields = m.get('nonSecretFields')

        return self

