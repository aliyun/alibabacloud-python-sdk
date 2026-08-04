# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class AuthLoginWithAligenieUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.AuthLoginWithAligenieUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        # Response code
        self.code = code
        # Response message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Response Result
        self.result = result
        # Flag indicating whether the invocation succeeded
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.AuthLoginWithAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class AuthLoginWithAligenieUserInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        expired_time_long: int = None,
        login_state_access_token: str = None,
    ):
        # Expiration time of the login state access token (long integer)
        self.expired_time_long = expired_time_long
        # Login state access token
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long

        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')

        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')

        return self

