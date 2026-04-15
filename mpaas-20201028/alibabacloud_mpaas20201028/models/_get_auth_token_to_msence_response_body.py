# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetAuthTokenToMsenceResponseBody(DaraModel):
    def __init__(
        self,
        mpaas_system_oauth_token_response: main_models.GetAuthTokenToMsenceResponseBodyMpaasSystemOauthTokenResponse = None,
        request_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mpaas_system_oauth_token_response = mpaas_system_oauth_token_response
        # Id of the request
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.mpaas_system_oauth_token_response:
            self.mpaas_system_oauth_token_response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpaas_system_oauth_token_response is not None:
            result['MpaasSystemOauthTokenResponse'] = self.mpaas_system_oauth_token_response.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MpaasSystemOauthTokenResponse') is not None:
            temp_model = main_models.GetAuthTokenToMsenceResponseBodyMpaasSystemOauthTokenResponse()
            self.mpaas_system_oauth_token_response = temp_model.from_map(m.get('MpaasSystemOauthTokenResponse'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAuthTokenToMsenceResponseBodyMpaasSystemOauthTokenResponse(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        expires_in: str = None,
        open_id: str = None,
        platform: str = None,
        user_id: str = None,
    ):
        self.auth_token = auth_token
        self.expires_in = expires_in
        self.open_id = open_id
        self.platform = platform
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in

        if self.open_id is not None:
            result['OpenId'] = self.open_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')

        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

