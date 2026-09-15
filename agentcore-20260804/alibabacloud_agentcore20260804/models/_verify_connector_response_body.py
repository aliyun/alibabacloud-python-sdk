# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class VerifyConnectorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VerifyConnectorResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The validation result.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
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
            temp_model = main_models.VerifyConnectorResponseBodyData()
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

class VerifyConnectorResponseBodyData(DaraModel):
    def __init__(
        self,
        invalid_service_account_keys: List[str] = None,
        valid: bool = None,
    ):
        # The list of Service Account Key names that failed validation. Each element is a key name string. This list is empty if all keys pass validation.
        self.invalid_service_account_keys = invalid_service_account_keys
        # Indicates whether the credentials are valid.
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invalid_service_account_keys is not None:
            result['invalidServiceAccountKeys'] = self.invalid_service_account_keys

        if self.valid is not None:
            result['valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('invalidServiceAccountKeys') is not None:
            self.invalid_service_account_keys = m.get('invalidServiceAccountKeys')

        if m.get('valid') is not None:
            self.valid = m.get('valid')

        return self

